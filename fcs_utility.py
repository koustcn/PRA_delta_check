import FlowCytometryTools
from FlowCytometryTools import PolyGate
import os
from scipy.stats import kstest
from scipy import stats
import pandas as pd
import numpy as np
from pylab import *
from datetime import datetime
import tempfile
import uuid

class FCSreader:

    def __init__(self, datafile,graph = False):
        """
        Gate for each elements.
        :param datafile:
        :param graph:
        """

        self.graph = graph
        self.datafile = datafile
        self.sample = FlowCytometryTools.FCMeasurement(ID='Test Sample', datafile=self.datafile)
        self.totalbeads =  PolyGate([(6.628e+04, 1.136e+05), (6.628e+04, 5.049e+04),
                               (1.602e+05, 5.191e+04), (1.602e+05, 1.157e+05),
                               (6.678e+04, 1.136e+05), (6.678e+04, 1.136e+05)], ('FSC-A', 'SSC-A'), region='in', name='totalbeads')
        self.control =  PolyGate([(6.734e+03, 5.870e+04), (5.508e+03, 5.883e+04),
                                  (5.683e+03, 1.062e+05), (7.009e+03, 1.058e+05),
                                  (6.734e+03, 5.857e+04), (6.734e+03, 5.857e+04)], ('PE-A', 'SSC-A'), region='in', name='control')
        self.class1 = PolyGate([(4.157e+03, 5.665e+04), (2.042e+02, 5.665e+04),
                        (1.042e+02, 8.545e+04), (4.282e+03, 8.609e+04),
                        (4.157e+03, 5.678e+04), (4.157e+03, 5.678e+04)], ('PE-A', 'SSC-A'), region='in', name='class1')

        self.class2 =  PolyGate([(9.086e+03, 5.921e+04), (7.760e+03, 5.934e+04),
                                 (8.010e+03, 1.080e+05), (9.211e+03, 1.077e+05),
                                 (9.111e+03, 5.896e+04), (9.111e+03, 5.921e+04)], ('PE-A', 'SSC-A'), region='in', name='class2')



        if "SAMPLE DATE" in self.sample.meta:
            try:
                self.sampledate = self.sampledate_parse(self.sample.meta["SAMPLE DATE"])
            except:
                self.sampledate = None
        else:
            self.sampledate = None

        if  "SAMPLE MRN" in self.sample.meta:
            self.sampleMRN = self.sample.meta["SAMPLE MRN"]
        else:
            self.sampleMRN = None

        if "$DATE" in self.sample.meta:
            try:
                self.run_date = self.rundate_parse(self.sample.meta["$DATE"])
            except:
                self.run_date = None
        else:
            self.run_date = None

        if "TUBE NAME" in self.sample.meta:
            self.tubename = self.sample.meta["TUBE NAME"]

        if "SAMPLE NAME" in self.sample.meta:
            """
            Duke special, this is to ingore the test for 1:16 samples
            """

            if str(self.sample.meta["SAMPLE NAME"])[:5].find("16") > 0 and self.sampleMRN != None:
                self.sampleMRN = "116" + self.sampleMRN


    def rundate_parse(self, str):
        """

        :param str:
        :return:
        """
        return  datetime.strptime(str, '%d-%b-%Y').date()

    def sampledate_parse(self, str):
        """

        :param str:
        :return:
        """

        str = self.numberclean(str)

        return datetime.strptime(str, '%m-%d-%y').date()

    def numberclean(self,str):
        """
        remove any non number chars
        :param str:
        :return:
        """
        newStr = ""
        for i in str:
            if i in "1234567890-":
                newStr = newStr + i
        return newStr

    def get_spill(self, text):
        """
        Extracts spillover matrix from FCS text entry.
        :param text: Text value from the $SPILL or $SPILLOVER metadata keyword in an FCS file
        :return: A tuple containing: (spillover matrix new_spill, column headers)
        """
        spill = text.split(',')
        n = int(spill[0])
        markers = spill[1:(n + 1)]
        markers = [item.strip().replace('\n', '') for item in markers]
        items = [item.strip().replace('\n', '') for item in spill[n + 1:]]
        new_spill = np.reshape(list(map(float, items)), (n, n))
        return new_spill, markers

    def custom_compensate(self,original_sample):
        """

        :param original_sample:
        :return:
        """
        # Copy the original sample
        new_sample = original_sample.copy()
        new_data = new_sample.data
        # Our transformation goes here
        spill_matrix, _ = self.get_spill(self.sample.meta["$SPILLOVER"])
        comp_data = new_data[['FITC-A', 'PE-A']]
        comp_data = np.linalg.solve(spill_matrix.T, comp_data.T).T
        new_data[['FITC-A', 'PE-A']] = comp_data
        new_data = new_data.dropna()  # Removes all NaN entries
        new_sample.data = new_data
        return new_sample

    def output(self):

        sample = self.sample.apply(self.custom_compensate)#apply compensate
        tsample = sample.gate(self.totalbeads)#gate
        tsample = tsample.transform('tlog', channels=[ 'PE-A', 'FITC-A'])#log transform
        gatedClass1 = tsample.gate(self.class1)#gate class1
        gatedControl = tsample.gate(self.control)
        gatedClass2 = tsample.gate(self.class2)
        if self.graph:
            gatedClass1.plot(['FITC-A'], color='g')
            plt.show()
            gatedControl.plot(['FITC-A'], color='b')
            plt.show()
            gatedClass2.plot(['FITC-A'], color='r')
            plt.show()
        return {"Class1": gatedClass1.get_data(),"Control":gatedControl.get_data(),"Class2":gatedClass2.get_data()
                ,"tubename":self.tubename,"sampledate":self.sampledate,"sampleMRN":self.sampleMRN,"rundate": self.run_date}


def trimValue(inputArray):
    """
    remove the outliner, in this case only keep the 1 to 99 % of the beads , some of the outliner will affect the AD test

    :param inputArray:
    :return:
    """
    minValue=np.percentile(inputArray, 1.0)
    maxValue = np.percentile(inputArray, 99.0)
    return np.clip(inputArray, minValue, maxValue)

def getMID(str):
    """

    :param str:
    :return:
    """
    newStr=""
    for i in str:
        if i in "1234567890 ":
            newStr=newStr+i
    list_str=newStr.split(" ")
    return max(list_str, key=len)



dataStorage={
    "sampledate":[],
    "tubename":[],
    "rundate":[],
    "sampleMRN":[],
    "mean_class1":[],
    "std_class1":[],
    "anderson_class1":[],
    "mean_control":[],
    "std_control":[],
    "anderson_control":[],
    "mean_class2":[],
    "std_class2":[],
    "anderson_class2":[],
    "filename":[]
}


if __name__ == "__main__":
    # the code below can run to generate statics for a group of FCS file not use in software

    for root, dirs, files in os.walk("C:\FCS Files", topdown=False):
        for name in files:
            file = os.path.join(root, name)
            if file.endswith('.fcs'):

                fullname =  file
                print(fullname)
                try:
                    a=FCSreader(fullname).output()
                    class1_value = 0
                    control_value = 0
                    class2_value = 0

                    try:
                        class1_value = trimValue(a["Class1"]['FITC-A'][a["Class1"]['FITC-A'] > 10].values)
                        control_value = trimValue(a["Control"]['FITC-A'][a["Control"]['FITC-A'] > 10].values)
                        class2_value = trimValue(a["Class2"]['FITC-A'][a["Class2"]['FITC-A'] > 10].values)

                        dataStorage["sampledate"].append(a["sampledate"])
                        dataStorage["tubename"].append(a["tubename"])
                        dataStorage["sampleMRN"].append(a["sampleMRN"])
                        dataStorage["rundate"].append(a["rundate"])

                        dataStorage["mean_class1"].append(mean(class1_value))
                        dataStorage["std_class1"].append(std(class1_value))
                        andersonStat = stats.anderson(trimValue(class1_value), dist="norm")[0]
                        dataStorage["anderson_class1"].append(andersonStat)
                        dataStorage["mean_control"].append(mean(control_value))
                        dataStorage["std_control"].append(std(control_value))
                        andersonStat = stats.anderson(trimValue(control_value), dist="norm")[0]
                        dataStorage["anderson_control"].append(andersonStat)
                        dataStorage["mean_class2"].append(mean(class2_value))
                        dataStorage["std_class2"].append(std(class2_value))
                        andersonStat = stats.anderson(trimValue(class2_value), dist="norm")[0]
                        dataStorage["anderson_class2"].append(andersonStat)
                        dataStorage['filename'].append(fullname)
                    except:
                        pass



                except:
                    pass

    results = pd.DataFrame.from_dict(dataStorage)
    results.to_csv (r'finaldata_lyrics_strict_anderson.csv', index = False, header=True)
