import pandas as pd
import json

import sakAdminQueries as Queries

class objSakAdminClass():
    def __init__(self):
        # DECLARE FINAL DICTIONARY TO BE USED TO CREATE JSON FROM.
        self.dictFinalDict = {}
        self.readAllActors()
        
    def readAllActors(self):
        df = Queries.getAllActorsData()
       # ADD DATA TO FINAL DICT.
        self.dictFinalDict['Actor'] = df[['first_name', 'last_name']].to_dict(orient='records')
        del df
        self.readAllFilms()
        
    def readAllFilms(self):
        df = Queries.getAllFilmsData()
        # ADD DATA TO FINAL DICT.
        self.dictFinalDict['Films'] = df[['film_id', 'title', 'description']].to_dict(orient='records')
        del df
        self.readAllCustomers()

        
    def readAllCustomers(self):
        df = Queries.getAllCustomersData()
        # ADD DATA TO FINAL DICT.
        self.dictFinalDict['Customers'] = df[['customer_id', 'store_id', 'first_name', 'last_name', 'email']].to_dict(orient='records')
        del df
        self.createJson()        
        
    def createJson(self):
        # CREATE JSON STRING FROM FINAL DICT.
        json_str = json.dumps(self.dictFinalDict)
        # WRITE JSON STRING TO FILE.
        fo = open('C:/Users/User/source/repos/Sakila/static/data/data.json', 'w')
        fo.write(json_str)
        fo.close()
        del self.dictFinalDict
