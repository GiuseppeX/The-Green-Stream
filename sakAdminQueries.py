from mysqlConn import runQuery

def getAllActorsData():
    ###  SQL QUERY DATA #########
    strQry = """SELECT
    *
    FROM
    ACTOR"""

    return runQuery(strQry)

def getAllFilmsData():
    ###  SQL QUERY DATA #########
    strQry = """SELECT
    *
    FROM
    FILM"""

    return runQuery(strQry)
    
def getAllCustomersData():
    ###  SQL QUERY DATA #########
    strQry = """SELECT
    *
    FROM
    CUSTOMER"""

    return runQuery(strQry)

