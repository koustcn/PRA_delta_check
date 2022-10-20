import sqlite3
from os import path, \
    remove
import pyodbc


class DataBase():
    """
    store the path of sqllite, super class for sql

    """

    def __init__(self):
        """

        """
        self.databasepath = ""


class DataBaseInit(DataBase):

    def __init__(self):
        super().__init__()
    """
    This is to create the database and check if database exist or not

    """


    def is_databaseexits(self):
        """
        check to see if the database file exist or not
        :return: boolen
        """

        return path.isfile((self.databasepath + "PRA_delta_checker.db"))

    def create_database(self):
        """
        if no datebase create a new one
        :return:
        """
        dict_setting_parameter = {
                                    "mean_class1":0,
                                    "mean_control":0,
                                    "mean_class2":0,
                                    "anderson_class1":0,
                                    "anderson_control":0,
                                    "anderson_class2":0,
                                    "min_ad_class1":0,
                                    "min_ad_control":0,
                                    "min_ad_class2":0,
                                    "rolling_mean":"false",
                                    "ks_enable":"false",
                                    "ks_ad_min_class1":0,
                                    "ks_ad_min_control":0,
                                    "ks_ad_min_class2":0,
                                    "ks_class1":0,
                                    "ks_class2":0,
                                    "ks_control":0
                                    }

        if self.is_databaseexits() == False:
            con = sqlite3.connect('PRA_delta_checker.db')
            cur = con.cursor()
            cur.execute ('create table pra_data (index_id INTEGER PRIMARY KEY,'
                        'sample_date datetime,'
                        'tubename string,'
                        'run_date datetime,'
                        'MRN string,'
                        'mean_class1 double,'
                        'std_class1 double,'
                        'anderson_class1 double,'
                        'mean_control double,'
                        'std_control double,'
                        'anderson_control double,'
                        'mean_class2 double,'
                        'std_class2 double,'
                        'anderson_class2 double,'
                        'file_path string'
                         ' );')
            cur.execute('create table settings (setting_id string,'
                        'parameter string);')
            cur.execute('create table path (file_path string);')
            cur.execute("insert into settings (setting_id, parameter) "
                        "values ('monitor_folder','\')")
            cur.execute("insert into settings (setting_id, parameter) "
                        "values ('output_folder','\')")
            cur.execute("insert into settings (setting_id, parameter) "
                        "values ('delta_parameters',:setting_parameter)",
                        {"setting_parameter":str(dict_setting_parameter)})

            con.commit()
            con.close()

class DataBaseQuerySetting(DataBase):
    """
    Database Query

    """
    def __init__(self):
        super().__init__()
        """
        for close connection just call class.con.close()
        """

        self.con = sqlite3.connect('PRA_delta_checker.db')
        self.cur = self.con.cursor()


    def update_settings(self, setting_id, parameter):
        """

        :param setting_id: see define for each id
        :param parameter: parameters
        :return: null
        """
        self.cur.execute("update settings set parameter = :parameter"
                         " where setting_id = :setting_id",
                         {"parameter":parameter, "setting_id":setting_id})
        self.con.commit()


    def retrive_settings(self, setting_id):
        """
        get the setting from litedb

        :param setting_id:setting id
        :return: setting parameters
        """
        self.cur.execute("select parameter from settings where setting_id=:"
                         "setting_id", {"setting_id": setting_id})

        return self.cur.fetchone()[0]

class DataBaseRemove(DataBase):
    """
    To remove the exist database, if error make sure that the db file is not kept.locked by other threshold

    """
    def __init__(self):
        super().__init__()

        """

        """
        #self.databasepath = ""

    def remove_databasefile(self):
        """

        :return:
        """
        remove(self.databasepath + 'PRA_delta_checker.db')

class DataBaseFCSFileManger():
    """

    handle the path for FCS

    """

    def __init__(self):
        super().__init__()
        """
        for close connection just call class.con.close()
        """
        #self.databasepath = ""
        self.con = sqlite3.connect('PRA_delta_checker.db')
        self.con.row_factory = lambda cursor, row: row[0] # generate list not tuple for SQLlite output
        self.cur = self.con.cursor()

    def insert_files_path(self,list_path):
        """

        :param list_path:
        :return:
        """
        for i in list_path:
            self.cur.execute("insert into path (file_path) values (:path)",{"path": i})
        self.con.commit()

    def clean_file_path(self):
        """

        :return:
        """

        self.cur.execute("delete from path")
        self.con.commit()

    def get_new_file_path(self):
        """

        :return:
        """

        self.cur.execute("select path.file_path from path left join pra_data on path.file_path = pra_data.file_path "
                         "where pra_data.file_path IS NULL")

        return self.cur.fetchall()

class DataBaseInsert(DataBase):
    """
    generate new row..
    """
    def __init__(self):
        super().__init__()
        """
        for close connection just call class.con.close()
        """

        self.con = sqlite3.connect('PRA_delta_checker.db')
        self.con.row_factory = lambda cursor, row: row[0] # generate list not tuple for SQLlite output
        self.cur = self.con.cursor()

    def insert_new_data(self, dict_info):
        """

        :param dict_info:
        :return:
        """
        pass

        self.cur.execute("insert into pra_data "
                         "(sample_date, "
                         "tubename,"
                         "run_date,"
                         "MRN,"
                         "mean_class1,"
                         "std_class1,"
                         "anderson_class1,"
                         "mean_control,"
                         "std_control,"
                         "anderson_control,"
                         "mean_class2,"
                         "std_class2,"
                         "anderson_class2,"
                         "file_path) "
                         "values "
                         "(:sampledate,"
                         ":tubename,"
                         ":rundate,"
                         ":sampleMRN,"
                         ":mean_class1,"
                         ":std_class1,"
                         ":anderson_class1,"
                         ":mean_control,"
                         ":std_control,"
                         ":anderson_control,"
                         ":mean_class2,"
                         ":std_class2,"
                         ":anderson_class2,"
                         ":filename)",dict_info)


class DataBaseQuery(DataBase):

    def __init__(self):
        super().__init__()

        self.con = sqlite3.connect('PRA_delta_checker.db')
        #self.con.row_factory = lambda cursor, row: row  # generate list not tuple for SQLlite output
        self.con.row_factory =  lambda C, R: { c[0]: R[i] for i, c in enumerate(C.description) }
        self.cur = self.con.cursor()

    def query_hx_pra(self, mrn):
        """

        :param mrn:
        :return: dict for the query
        """

        self.cur.execute("select sample_date, tubename, run_date, MRN, mean_class1, std_class1, anderson_class1, "
                         "mean_control, std_control, anderson_control, mean_class2, std_class2, anderson_class2, "
                         "file_path from pra_data where MRN = :MRN order by run_date desc, sample_date desc limit 1",{"MRN":mrn} )

        return  self.cur.fetchall()








if __name__ == "__main__":

    # class test if needed.
    pass