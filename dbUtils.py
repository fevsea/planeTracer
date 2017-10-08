import sqlite3

import adsbReceiver
import settings


def createRawTable(decodedData):
    conn = sqlite3.connect(settings.dbName)
    cursor = conn.cursor()
    sql = """ CREATE TABLE IF NOT EXISTS {0} ( 
                flight TEXT, 
                altitude INTEGER, 
                speed INTEGER, 
                track INTEGER,
                vert_rate INTEGER,
                lat REAL,
                lon REAL,
                squawk TEXT,
                seen INTEGER,
                validposition INTEGER,
                messages INTEGER,
                validtrack INTEGER,
                hex TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
                trace INTEGER DEFAULT NULL,
                pk INTEGER PRIMARY KEY AUTOINCREMENT);
 """.format(settings.rawTableName)
    print(sql)
    cursor.execute(sql)
    try:
        conn.commit()
    except:
        pass
    conn.close()





def initDB(decodedData):
    createRawTable(decodedData)


def insert(plane, traceID):
    conn = sqlite3.connect('testDB.db')
    cursor = conn.cursor()
    keys = "'trace', "
    values = "'" + traceID + "', "
    for key, value in plane.items():
        keys += "'" + str(key) + "' ,"
        values += "'" + str(value) + "' ,"

    sql = "INSERT INTO " + settings.rawTableName + "( " + keys[:-1] + ") VALUES (" + values[:-1] + ");"
    print(sql)
    cursor.execute(sql)
    cursor.close()
    try:
        conn.commit()
    except:
        pass
    conn.close()
    