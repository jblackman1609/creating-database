import sql, tableStructure as ts, os, sqlite3

sourceDir = 'c:\\Users\\Joe_User\\Desktop\\sourceDir'
destDir = 'c:\\Users\\Joe_User\\Desktop\\appDir_v2\\config_files\\'
tableIndex = os.path.join(destDir, 'tables.txt')

def main():
    ts.buildTableStruct(sourceDir, destDir)
    
    tables = open(tableIndex).read().split()
    records = sql.getRecords(destDir)
    
    connection = sqlite3.connect('database1.db')
    
    c = connection.cursor()
    
    for table in tables:
        c.execute(sql.createTable(table))

        for record in records:
            c.execute(sql.insertRecord(table, record))

    c.execute('show databases')
        
    connection.commit()
    
    connection.close()

    

    return 0

main()


        
