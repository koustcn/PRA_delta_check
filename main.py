from ui.PRAChecker_ui import *
from ui.folder_monitor_setting_ui import *
from ui.folder_output_setting_ui import *
from ui.acquire_fcs_data_ui import *
import sys
from PyQt5 import QtCore, \
    QtGui, \
    QtWidgets
from database_utility import *
from fcs_utility import *
import os
import json
import seaborn as sb
from output_files_utility import *
"""
command to generate ui.py
pyuic5 prachecker.ui -o PRAChecker_ui.py
"""



class Windows(QtWidgets.QMainWindow):
    """

    """
    def __init__(self, parent = None):
        """
        
        :param parent:
        """
        super(Windows, self).__init__(parent =  parent)
        self.ui = Ui_PRAChecker()
        self.ui.setupUi(self)
        self.ui.menu_folder_monitor.triggered.connect(self.monitor_folder_setting)
        self.ui.menu_ouput_folder.triggered.connect(self.output_folder_setting)
        self.ui.menu_database_rebuilder.triggered.connect(self.rebuild_database)
        self.ui.menu_acquire_FCS_Files.triggered.connect(self.acquire_fcs_files)
        self.dict_parameters = {}
        self.ui.pb_status.setValue(0)
        DataBaseInit().create_database()
        load_parameters = DataBaseQuerySetting()
        self.dict_parameters = json.loads(load_parameters.retrive_settings("delta_parameters").replace("\'", "\""))
        self.load_delta_parameters()
        self.insert_new_record = DataBaseInsert()

        """
        monitor changes of spinbox or checkbox update all if anyone of them changed
        """
        self.ui.spin_box_mean_class1.valueChanged.connect(self.update_settings)
        self.ui.spin_box_mean_class2.valueChanged.connect(self.update_settings)
        self.ui.spin_box_mean_control.valueChanged.connect(self.update_settings)
        self.ui.spin_box_ad_class1.valueChanged.connect(self.update_settings)
        self.ui.spin_box_ad_class2.valueChanged.connect(self.update_settings)
        self.ui.spin_box_ad_control.valueChanged.connect(self.update_settings)
        self.ui.spin_box_min_ad_class1.valueChanged.connect(self.update_settings)
        self.ui.spin_box_min_ad_class2.valueChanged.connect(self.update_settings)
        self.ui.spin_box_min_ad_control.valueChanged.connect(self.update_settings)
        #self.ui.checkbox_rollingmean.stateChanged.connect(self.update_settings)
        self.ui.checkbox_ks_testing.stateChanged.connect(self.update_settings)
        self.ui.spin_box_min_ad_ks_class1.valueChanged.connect(self.update_settings)
        self.ui.spin_box_min_ad_ks_class2.valueChanged.connect(self.update_settings)
        self.ui.spin_box_min_ad_ks_control.valueChanged.connect(self.update_settings)
        self.ui.spin_box_ks_control.valueChanged.connect(self.update_settings)
        self.ui.spin_box_ks_class1.valueChanged.connect(self.update_settings)
        self.ui.spin_box_ks_class2.valueChanged.connect(self.update_settings)

        self.ui.btn_check_sample.clicked.connect(self.delta_check)


    def monitor_folder_setting(self):
        """
        click to pop folder monitoring
        :return:
        """
        Monitor_Folder_Selection_UI().exec_()

    def output_folder_setting(self):
        """
        click to pop folder monitoring
        :return:
        """
        Output_Folder_Selection_UI().exec_()

    def acquire_fcs_files(self):
        """

        :return:
        """
        Acquire_FCS_Files_UI().exec_()

    def rebuild_database(self):
        """

        delete the database and create a new one.

        :return:
        """
        qm = QtWidgets.QMessageBox

        ret = qm.question(self, 'Remove the database?', "Do you want to remove and rebuilt the database?",
                          qm.Yes | qm.No)

        if ret == qm.Yes:
            try:
                DataBaseRemove().remove_databasefile()
                DataBaseInit().create_database()
                qm.question(self,"New database","New database created",qm.Yes)

            except:
                qm.warning(self,"Unable to delete the datebase","Unable to delete the datebase",qm.Yes)


    def load_delta_parameters(self):


        self.ui.spin_box_mean_class1.setValue(self.dict_parameters["mean_class1"])
        self.ui.spin_box_mean_class2.setValue(self.dict_parameters["mean_class2"])
        self.ui.spin_box_mean_control.setValue(self.dict_parameters["mean_control"])
        self.ui.spin_box_ad_class1.setValue(self.dict_parameters["anderson_class1"])
        self.ui.spin_box_ad_class2.setValue(self.dict_parameters["anderson_class2"])
        self.ui.spin_box_ad_control.setValue(self.dict_parameters["anderson_control"])
        self.ui.spin_box_min_ad_class1.setValue(self.dict_parameters["min_ad_class1"])
        self.ui.spin_box_min_ad_class2.setValue(self.dict_parameters["min_ad_class2"])
        self.ui.spin_box_min_ad_control.setValue(self.dict_parameters["min_ad_control"])
        #self.ui.checkbox_rollingmean.setChecked(json.loads(self.dict_parameters["rolling_mean"].lower()))
        self.ui.checkbox_ks_testing.setChecked(json.loads(self.dict_parameters["ks_enable"].lower()))
        self.ui.spin_box_min_ad_ks_class1.setValue(self.dict_parameters["ks_ad_min_class1"])
        self.ui.spin_box_min_ad_ks_class2.setValue(self.dict_parameters["ks_ad_min_class2"])
        self.ui.spin_box_min_ad_ks_control.setValue(self.dict_parameters["ks_ad_min_control"])
        self.ui.spin_box_ks_class1.setValue(self.dict_parameters["ks_class1"])
        self.ui.spin_box_ks_class2.setValue(self.dict_parameters["ks_class2"])
        self.ui.spin_box_ks_control.setValue(self.dict_parameters["ks_control"])


    def update_settings(self):
        """

        :return:
        """
        self.dict_parameters["mean_class1"] = int( self.ui.spin_box_mean_class1.text())
        self.dict_parameters["mean_class2"] =  int (self.ui.spin_box_mean_class2.text())
        self.dict_parameters["mean_control"] =  int (self.ui.spin_box_mean_control.text())
        self.dict_parameters["anderson_class1"] = int(self.ui.spin_box_ad_class1.text())
        self.dict_parameters["anderson_class2"] =  int(self.ui.spin_box_ad_class2.text())
        self.dict_parameters["anderson_control"] =  int(self.ui.spin_box_ad_control.text())
        self.dict_parameters["min_ad_class1"] = int(self.ui.spin_box_min_ad_class1.text())
        self.dict_parameters["min_ad_class2"] =  int(self.ui.spin_box_min_ad_class2.text())
        self.dict_parameters["min_ad_control"] = int(self.ui.spin_box_min_ad_control.text())
        self.dict_parameters["rolling_mean"] = str(self.ui.checkbox_rollingmean.isChecked())
        self.dict_parameters["ks_enable"] =  str(self.ui.checkbox_ks_testing.isChecked())
        self.dict_parameters["ks_ad_min_class1"] = int(self.ui.spin_box_min_ad_ks_class1.text())
        self.dict_parameters["ks_ad_min_class2"] = int(self.ui.spin_box_min_ad_ks_class2.text())
        self.dict_parameters["ks_ad_min_control"] = int(self.ui.spin_box_min_ad_ks_control.text())
        self.dict_parameters["ks_class1"] =  int(self.ui.spin_box_ks_class1.text())
        self.dict_parameters["ks_class2"] = int(self.ui.spin_box_ks_class2.text())
        self.dict_parameters["ks_control"] = int(self.ui.spin_box_ks_control.text())

        parameters_update = DataBaseQuerySetting()
        parameters_update.update_settings("delta_parameters", str(self.dict_parameters))





    def number_checker(self, a, b, threshold, igore_minimun = 0, fold=False):
        """

        :param a: number a
        :param b: number b
        :param threshold: threshold to check could be n% or n fold
        :param igore_minimun: if 0 return False
        :param fold: % or fold checker
        :return: if number and number b out of % range
        """
        if threshold == 0:
            return False

        if not fold:
            if abs((b - a) / a) <= threshold/100:
                return False
            else:
                return True
        else:
            if a <= igore_minimun and b <= igore_minimun:
                return False

            if a / b < threshold and b / a < threshold:
                return False
            else:
                return True
    def generate_graph(self, FCS_data):
        """

        :param class1_value:
        :param control_value:
        :param class2_value:
        :return:
        """
        #plt.xlim(0, 10000)
        class1_value = trimValue(FCS_data["Class1"]['FITC-A'][FCS_data["Class1"]['FITC-A'] > 10].values)
        control_value = trimValue(FCS_data["Control"]['FITC-A'][FCS_data["Control"]['FITC-A'] > 10].values)
        class2_value = trimValue(FCS_data["Class2"]['FITC-A'][FCS_data["Class2"]['FITC-A'] > 10].values)
        fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(20, 5))
        sb.distplot (class1_value, bins = 200,hist = True, ax = ax[0], axlabel = "Class 1 MFI", color = 'g', hist_kws={"range": [0,10000]})
        sb.distplot (control_value, bins = 200,hist = True, ax = ax[1], axlabel = "Control MFI", color = 'b', hist_kws={"range": [0,10000]})
        sb.distplot (class2_value, bins = 200,hist = True, ax = ax[2], axlabel = "Class 2 MFI", color = 'r', hist_kws={"range": [0,10000]})
        tmp = tempfile.gettempdir()
        #plt.show()
        file_to_save = tmp + "/" + str(uuid.uuid1()) +".png"
        plt.savefig(file_to_save)
        plt.clf()

        return file_to_save

    def normalize(self, arr, t_min = 0, t_max = 1):

        """

        :param arr:
        :param t_min:
        :param t_max:
        :return:
        """
        """norm_arr = []
        diff = t_max - t_min
        diff_arr = max(arr) - min(arr)
        for i in arr:
            temp = (((i - min(arr)) * diff) / diff_arr) + t_min
            norm_arr.append(temp)
        return norm_arr"""


        return (arr - np.min(arr)) / (np.max(arr) - np.min(arr))



    def delta_check(self):
        """

        :return:
        """
        datetime_stamp = datetime.now()
        str_timestample = datetime_stamp.strftime("%d_%b_%Y_%H%M")
        doc = GenerateReport(str_timestample+".docx")
        doc.add_title()

        query_folder = DataBaseQuerySetting()
        folder = query_folder.retrive_settings("monitor_folder")

        query_files = DataBaseFCSFileManger()
        query_files.clean_file_path()
        fcs_files = []
        """for root, dirs, files in os.walk(folder, topdown=False):
            for name in files:
                file = os.path.join(root, name)
                if file.endswith('.fcs'):
                    fcs_files.append(file)"""
        for root, dirs, files in os.walk(folder, topdown = False):
            full_list = [os.path.join(root, i) for i in files]
            full_list.sort(key=os.path.getmtime)
            for name in full_list:
                if name.endswith('.fcs'):
                    fcs_files.append(name)
        query_files.insert_files_path(fcs_files)
        fcs_files = query_files.get_new_file_path()
        files_count = len(fcs_files)
        """
        Get new files information
        """



        """
        Get setting parameters.
        """
        #print(self.dict_parameters)


        for k, i in enumerate(fcs_files):
            self.ui.pb_status.setValue(int((100/files_count)*k))
            dict_info = {
                "sampledate": "",
                "tubename": "",
                "rundate": "",
                "sampleMRN": "",
                "mean_class1": 0,
                "std_class1": 0,
                "anderson_class1": 0,
                "mean_control": 0,
                "std_control": 0,
                "anderson_control": 0,
                "mean_class2": 0,
                "std_class2": 0,
                "anderson_class2": 0,
                "filename": i # save fcs file location
            }
            try:
                FCS_data = FCSreader(i).output()
                dict_info["sampledate"] = FCS_data["sampledate"]
                dict_info["tubename"] = FCS_data["tubename"]
                dict_info["rundate"] = FCS_data["rundate"]
                dict_info["sampleMRN"] = FCS_data["sampleMRN"]

                class1_value = trimValue(FCS_data["Class1"]['FITC-A'][FCS_data["Class1"]['FITC-A'] > 10].values)
                control_value = trimValue(FCS_data["Control"]['FITC-A'][FCS_data["Control"]['FITC-A'] > 10].values)
                class2_value = trimValue(FCS_data["Class2"]['FITC-A'][FCS_data["Class2"]['FITC-A'] > 10].values)


                dict_info["mean_class1"] = mean(class1_value)
                dict_info["std_class1"]= std(class1_value)
                andersonStat = stats.anderson(trimValue(class1_value), dist="norm")[0]
                dict_info["anderson_class1"] = andersonStat
                dict_info["mean_control"] = mean(control_value)
                dict_info["std_control"] = std(control_value)
                andersonStat = stats.anderson(trimValue(control_value), dist="norm")[0]
                dict_info["anderson_control"] = andersonStat
                dict_info["mean_class2"] = mean(class2_value)
                dict_info["std_class2"] = std(class2_value)
                andersonStat = stats.anderson(trimValue(class2_value), dist="norm")[0]
                dict_info["anderson_class2"] = andersonStat

            except:
                pass
            mean_to_compare = ["mean_class1", "mean_control", "mean_class2"]
            anderson_to_compare = ["anderson_class1", "anderson_control", "anderson_class2"]
            delta_check_result = []

            if dict_info["sampleMRN"] != "" and dict_info["sampleMRN"] != None and dict_info["sampleMRN"] != "None" \
                    and dict_info["sampleMRN"].find(" ") < 0  :
                ## check if the MRN is real or not if contain non-MRN values ignore
                """
                check to see if FCS get the MRN or not if not ignore
                """
                get_hx_data = DataBaseQuery()
                hx_data = get_hx_data.query_hx_pra(dict_info["sampleMRN"])
                """
                Query the database get the MRN
                """
                if len(hx_data) > 0:
                    """
                    if history data present
                    """
                    hx_data = hx_data[0]
                    """
                    Read the most current one
                    """
                    for element in mean_to_compare: # mean check
                       if self.number_checker(hx_data[element], dict_info[element],self.dict_parameters[element], fold = False):
                           delta_check_result.append({"rule": element, "hx_value": hx_data[element], "current_value":dict_info[element]})

                    if self.number_checker(hx_data["anderson_class1"],dict_info["anderson_class1"],
                                           self.dict_parameters["anderson_class1"], igore_minimun = self.dict_parameters ["min_ad_class1"], fold = True):
                        delta_check_result.append(
                            {"rule": "anderson_class1", "hx_value": hx_data["anderson_class1"], "current_value": dict_info["anderson_class1"]})
                    if self.number_checker(hx_data["anderson_control"],dict_info["anderson_control"],
                                           self.dict_parameters["anderson_control"], igore_minimun = self.dict_parameters["min_ad_control"], fold = True):
                        delta_check_result.append(
                            {"rule": "anderson_control", "hx_value": hx_data["anderson_control"], "current_value": dict_info["anderson_control"]})
                    if self.number_checker(hx_data["anderson_class2"],dict_info["anderson_class2"],
                                           self.dict_parameters["anderson_class2"], igore_minimun = self.dict_parameters["min_ad_class2"], fold = True):
                        delta_check_result.append(
                            {"rule": "anderson_class2", "hx_value": hx_data["anderson_class2"], "current_value": dict_info["anderson_class2"]})
                    """
                    Anderson test above. 
                    
                    """

                    print(i, delta_check_result)

                    """
                    
                    KS testing if the anderson test is too large for some samples 
                    
                    KS compare the sample shape all values will be normalized before testing
                    """

                    ks_testing = []
                    if self.dict_parameters["ks_enable"]:
                        if self.dict_parameters["ks_ad_min_class1"] <= dict_info["anderson_class1"]:
                            ks_testing.append("Class1")
                        if self.dict_parameters["ks_ad_min_class2"] <= dict_info["anderson_class2"]:
                            ks_testing.append("Class2")
                        if self.dict_parameters["ks_ad_min_control"] <= dict_info["anderson_control"]:
                            ks_testing.append("Control")


                    if len(delta_check_result) != 0 or len(ks_testing) != 0:
                        """
                        Any number exceed threold will triger to write report
                        
                        """


                        hx_FCS_data = FCSreader(hx_data["file_path"]).output()
                        for i in ks_testing:
                            """
                            KS testing
                            1. normalized the value
                            2. check the ks score only not the p value
                            3. if exceed add to delta check result, write to word document
                            
                            """

                            current_value = trimValue(FCS_data[i]['FITC-A'][FCS_data[i]['FITC-A'] > 10].values)
                            hx_value = trimValue(hx_FCS_data[i]['FITC-A'][hx_FCS_data[i]['FITC-A'] > 10].values)
                            ks_stat_result = kstest(self.normalize(current_value), self.normalize(hx_value))[0]
                            print(ks_stat_result * 100)
                            if self.dict_parameters["ks_" + i.lower()] <= ks_stat_result * 100:
                                delta_check_result.append({"k S-testing for " + i : str(ks_stat_result) })
                            #add ks testing
                        if len(delta_check_result) > 0:
                            doc.add_sample_info(FCS_data)
                            for i in delta_check_result:
                                doc.add_delta_check_info(i)
                            graph_location = self.generate_graph(FCS_data)
                            doc.add_graph(graph_location)
                            hx_graph_location = self.generate_graph(hx_FCS_data)
                            doc.add_sample_info(hx_FCS_data, hx = True)
                            doc.add_graph(hx_graph_location)
                else:

                    """
                    if new sample tell the user the sample is new. 
                    """
                    doc.add_sample_info(FCS_data)
                    doc.add_as_newsample()

            self.insert_new_record.insert_new_data(dict_info)

        save_to_folder = query_folder.retrive_settings("output_folder")
        query_folder.con.close()
        doc.save_document(save_to_folder)

        self.insert_new_record.con.commit()
        self.ui.pb_status.setValue(int(100))

        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("FCS files check complete")
        msg.setWindowTitle("FCS check complete")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()


class Monitor_Folder_Selection_UI(QtWidgets.QDialog):
    """

    """

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """

        super().__init__(*args, **kwargs)
        self.ui = Ui_folder_to_monitor_setting()
        self.ui.setupUi(self)
        self.ui.btn_select_folder.clicked.connect(self.select_folder)
        self.ui.btn_confirm_folder.clicked.connect(self.confirm_selection)
        self.ui.btn_confirm_folder.clicked.connect(self.close)
        self.get_folder_setting()

    def select_folder(self):
        """

        :return:
        """

        self.ui.txt_folder_select.setText(QtWidgets.QFileDialog.getExistingDirectory())
        self.ui.btn_select_folder.clicked.connect(self.select_folder)

    def confirm_selection(self):
        """

        :return:
        """
        update_folder = DataBaseQuerySetting()
        update_folder.update_settings("monitor_folder",self.ui.txt_folder_select.text())

    def get_folder_setting(self):
        """

        :return:
        """
        query_folder = DataBaseQuerySetting()
        self.ui.txt_folder_select.setText(query_folder.retrive_settings("monitor_folder"))
        query_folder.con.close()



class Output_Folder_Selection_UI(QtWidgets.QDialog):
    """

    """

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """

        super().__init__(*args, **kwargs)
        self.ui = Ui_folder_output_setting()
        self.ui.setupUi(self)
        self.ui.btn_select_folder.clicked.connect(self.select_folder)
        self.ui.btn_confirm_folder.clicked.connect(self.confirm_selection)
        self.ui.btn_confirm_folder.clicked.connect(self.close)
        self.get_folder_setting()

    def select_folder(self):
        """

        :return:
        """

        self.ui.txt_folder_select.setText(QtWidgets.QFileDialog.getExistingDirectory())
        self.ui.btn_select_folder.clicked.connect(self.select_folder)

    def confirm_selection(self):
        """

        :return:
        """
        update_folder = DataBaseQuerySetting()
        update_folder.update_settings("output_folder",self.ui.txt_folder_select.text())

    def get_folder_setting(self):
        """

        :return:
        """
        query_folder = DataBaseQuerySetting()
        self.ui.txt_folder_select.setText(query_folder.retrive_settings("output_folder"))
        query_folder.con.close()

class Acquire_FCS_Files_UI(QtWidgets.QDialog):
    """

    """

    def __init__(self, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """

        super().__init__(*args, **kwargs)
        self.ui = Ui_acquire_fcs_data()
        self.ui.setupUi(self)
        self.ui.progressBar.setValue(0)
        self.ui.button_exit.clicked.connect(self.close)
        self.insert_new_record = DataBaseInsert()
        self.ui.button_start.clicked.connect(self.acquire_FCS)

    def acquire_FCS(self):
        """
        """
        self.ui.label_current_file.setText("Preparing.....")
        query_folder = DataBaseQuerySetting()
        folder = query_folder.retrive_settings("monitor_folder")
        query_folder.con.close()
        query_files =  DataBaseFCSFileManger()
        query_files.clean_file_path()
        fcs_files = []
        self.ui.label_current_file.setText("Reading the files.....")
        for root, dirs, files in os.walk(folder, topdown=False):
            for name in files:
                file = os.path.join(root, name)
                if file.endswith('.fcs'):
                    fcs_files.append(file)
        query_files.insert_files_path(fcs_files)
        fcs_files = query_files.get_new_file_path()
        self.ui.label_current_file.setText("Finding the new files.....")
        files_count = len(fcs_files)

        for k, i in enumerate(fcs_files):
            self.ui.progressBar.setValue(int((100/files_count)*k))
            self.ui.label_current_file.setText(i)
            dict_info = {
                "sampledate": "",
                "tubename": "",
                "rundate": "",
                "sampleMRN": "",
                "mean_class1": 0,
                "std_class1": 0,
                "anderson_class1": 0,
                "mean_control": 0,
                "std_control": 0,
                "anderson_control": 0,
                "mean_class2": 0,
                "std_class2": 0,
                "anderson_class2": 0,
                "filename": i
            }
            try:
                FCS_data = FCSreader(i).output()
                dict_info["sampledate"] = FCS_data["sampledate"]
                dict_info["tubename"] = FCS_data["tubename"]
                dict_info["rundate"] = FCS_data["rundate"]
                dict_info["sampleMRN"] = FCS_data["sampleMRN"]

                class1_value = trimValue(FCS_data["Class1"]['FITC-A'][FCS_data["Class1"]['FITC-A'] > 10].values)
                control_value = trimValue(FCS_data["Control"]['FITC-A'][FCS_data["Control"]['FITC-A'] > 10].values)
                class2_value = trimValue(FCS_data["Class2"]['FITC-A'][FCS_data["Class2"]['FITC-A'] > 10].values)


                dict_info["mean_class1"] = mean(class1_value)
                dict_info["std_class1"]= std(class1_value)
                andersonStat = stats.anderson(trimValue(class1_value), dist="norm")[0]
                dict_info["anderson_class1"] = andersonStat
                dict_info["mean_control"] = mean(control_value)
                dict_info["std_control"] = std(control_value)
                andersonStat = stats.anderson(trimValue(control_value), dist="norm")[0]
                dict_info["anderson_control"] = andersonStat
                dict_info["mean_class2"] = mean(class2_value)
                dict_info["std_class2"] = std(class2_value)
                andersonStat = stats.anderson(trimValue(class2_value), dist="norm")[0]
                dict_info["anderson_class2"] = andersonStat

            except:
                pass
            self.insert_new_record.insert_new_data(dict_info)
        self.insert_new_record.con.commit()
        self.ui.progressBar.setValue(int(100))
        self.ui.label_current_file.setText("Done!!!")
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("FCS files acquire complete")

        msg.setWindowTitle("FCS files acquire complete")

        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msg.exec_()
        self.close()




def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Windows()
    w.show()
    sys.exit(app.exec())
    #app.exec_()

if __name__ == '__main__':
    main()


