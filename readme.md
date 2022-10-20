![ashibanner](banner.png)


# PRA Delta Checker (PDC)

PDC is software run with the flow cytometer to monitor the changes of PRA results for HLA lab. 

## installation 

1. for the programmer, please pip install -r requirements.txt. 

   Please note each lab will name the meta element in FCS file differently.  Make sure variable sampleMRN = to the identifier of the patient

   variable sampledate = to the sample date of the sample. Parse to date correctly, string will not able to compare. 

2. for users, please compile the software to executable. 


## usage 

Please see ASHI annual meeting 2022 Poster P118

https://www.sciencedirect.com/science/article/pii/S019888592200163X

1. settings
   
   1. folder to monitor, select the folder where your flowcytometer output the FCS files, refer to flow software manual. 
   
   2. database rebuild, delete the current database and create a new one. 
   
   3. output folder, where the docx reports deposit to
   
   4. acquire FCS file, if you only want the software to read the FCS files to local database without checking, this is the function to use. 

2. cut off for delta check setting. 
   
   1. mean should be in 10% range
   
   2. anderson darling should be in 5 - 10 fold. 
   
   3. minimum value for anderson darling delta check should be greater than 30, otherwise, many false alert will be generated for small architectures. 
   
   4. Kolmogorov–Smirnov test only, if the PRA architecture is out of bell shape, should set at least 30 
    
3. check new samples
    
    By clicking, the software will check new samples and output report.
 
![poster](ashi_poster_PRA_Delta_Check.png)

## License

[GPL] (https://opensource.org/licenses/GPL-3.0)