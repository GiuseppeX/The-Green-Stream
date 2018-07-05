import pandas as pd
import pymysql

# use this function to get a database connection then run a query
def runQuery(paramQry):
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd='codddd69', db='sakila') 
    df = pd.read_sql(sql=paramQry, con=conn)
    conn.close()
    return df







