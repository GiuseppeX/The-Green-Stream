import pandas as pd
import json

from mysqlConn import run_query

class objAdminClass():
    def __init__(self):
        self.createDict(run_query("SELECT * FROM CONS_TYPES"))

    # DECLARE FINAL DICTIONARY TO BE USED TO CREATE JSON FROM.
    def createDict(self, param_df):    
        dict = {}
        # ADD CONS_SUBTYPES DATA TO FINAL DICT.
        dict['CONS_TYPES'] = param_df.to_dict(orient='records')
        del param_df
        self.createJson(dict)
        
    # CREATE JSON STRING FROM FINAL DICT.
    def createJson(self, param_dict):    
        json_str = json.dumps(param_dict)
        # WRITE JSON STRING TO FILE.
        fo = open('C:\\Users\\User\\source\\repos\\The-Green-Stream\\static\\js\\data\\admin_data.json', 'w')
        fo.write(json_str)
        fo.close()


