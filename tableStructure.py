###############################
# buildTableStruct(src, dest)
# getSources(directory)
# updateIndexFile(filename, update)
# getLines(filename)
# convert2DataType(oldline)
# doesExist(ptrn, string)
# getDataType(val)
#####################################

import os, io, re, shutil, ast

desktop = 'c:\\Users\\Joe_User\\Desktop\\'
sourceDir = desktop + 'sourceDir\\'
destDir = desktop + 'appDir_v2\\config_files\\'

def buildTableStruct(src, dest):
    try:
        tableStruct = shutil.copytree(src, dest)

    except FileExistsError:
        tableStruct = dest
    
    sources = getSources(tableStruct)
   
    for source in sources:    
        updateIndexFile(dest + 'tables.txt', source)

        files = os.listdir(dest + source)
       
        for _file in files:            
            lines = getLines(dest + source + '\\' + _file)
           
            for line in lines:               
                updateIndexFile(dest + source + '\\columns.txt', line)
                      
    return 0

def getSources(directory):
    for folder, subfolder, filename in os.walk(directory):
        return subfolder

def updateIndexFile(filename, update):
    try:
        with open(filename, 'x') as fileObj:
            with open(filename, 'r') as fileObj:
                contents = fileObj.read()
        
    except FileExistsError:
        contents = open(filename, 'r').read()
    
    appendObj = open(filename, 'a')
    
    if contents == '':
        appendObj.write(update + '\n')
        appendObj.close()
        return 0
    
    elif doesExist(update, contents):
        appendObj.close()
        return 0

    else:
        appendObj.write(update + '\n')
        appendObj.close()
        return 0
    
def getLines(filename):
    lines = open(filename, 'r').readlines()
    
    convertedLines = []
   
    for line in lines:       
        convertedLines.append(convert2DataType(line))     
        
    return convertedLines

def convert2DataType(oldline):
    lineSplit = oldline.split()
       
    dataType = getDataType(lineSplit[-1])    
    
    lineSplit[-1] = dataType
       
    try: newline = '\t'.join(lineSplit)
        
    except TypeError: pass
    
    return newline

def doesExist(ptrn, string):
    try:
        searchObj = re.search(ptrn, string)
        
        found = searchObj.group()
        
        return True
                
    except AttributeError: return False

def getDataType(val):
    try:
        t = ast.literal_eval(val)
        
    except SyntaxError: return 'string'

    except ValueError: return 'string'
    
    if type(t) == int:
        return 'integer'

    elif type(t) == float:
        return 'real'

    else: return 'string'
    
def main():
    buildTableStruct(sourceDir, destDir)

#main()
