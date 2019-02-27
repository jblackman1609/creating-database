#################################################
# createTable(tablename)
# insertRecord(tablename, record)
# getRecords(tableDir)
#############################################

import os, tableStructure as ts

top = 'c:\\Users\\Joe_User\\Desktop\\appDir_v2\\config_files\\'
tableIndex = os.path.join(top, 'tables.txt')

def createTable(table):
    columnIndex = os.path.join(top, '{0}columns.txt'.format(table.lower()))

    columns = open(columnIndex).readlines()
    
    primaryKey = '{0}_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL'.format(table.lower())
    
    create = 'CREATE TABLE IF NOT EXISTS {0}({1}, '.format(table.lower(), primaryKey)
   
    for column in columns:
        create = (create + '{0} {1}, ').format(column.split()[0].lower(), column.split()[-1].upper())
    
    create = create[-2] + ');'
    
    return create

def insertRecord(table,record):
    colValPairs = open(record).readlines()   

    insert = 'INSERT INTO {0}('.format(table.lower())

    for colValPair in colValPairs:
        insert = (insert + '{0}, ').format(colValPair.split()[0].lower())

    insert = insert + ') VALUES('

    for colValPair in colValPairs:
        insert = (insert + '{0}, ').format(colValPair.split()[-1].lower())

    insert = insert[:-2] + ');'

    return insert

def getRecords(tableDir):
    files = os.listdir(os.path.join(top, tableDir))
   
    records = []
    for _file in files:
        if _file == 'columns.txt':
            continue

        else: records.append(_file)

    return records  

def main():
    tables = ts.getSources(top)
    
    for table in tables:
        records = getRecords(table)
                
        for record in records:
            print(insertIntoTable(table, top + table + '\\' + record))
                 
    return 0

#main()
    

      

   


