import os, glob, sys, time, datetime, pprint
from datetime import date

def purgeFilter(inputPath:str, retention:int):
    '''
    filters through files through one directory deep that are older that x amount of days
    '''
    print("File Path: {}".format(inputPath))

    path = inputPath
    allPath = path + "/*"

    fullPaths = glob.glob(allPath)

    older = list()
    oldDates = list()
    totalSize = 0

    #Retention Policies
    todayDate = date.today()
    deltaDate = datetime.timedelta(int(retention))
    dateAfterDelta = todayDate - deltaDate
    print("Retention Policy: {}".format(dateAfterDelta))
    print('\n')

    #Folders and Dates
    for folder in fullPaths:
        fileInfo = os.stat(folder)
        fileTime = fileInfo.st_birthtime
        creation = time.strftime('%m %d %Y', time.gmtime(fileTime))
        dateCreation = datetime.datetime.strptime(creation, '%m %d %Y').date()

        if dateCreation < dateAfterDelta:
            older.append(folder)
            oldDates.append(str(dateCreation))
    
    #File Size
    for folders in older:
        for files in glob.glob(folders + "/**/*.*" , recursive=True):
            filesize = os.path.getsize(files)
            totalSize = totalSize + filesize
    sizeGB = totalSize / (1024*1024*1024)
    formatted_size = "{:.2f}".format(sizeGB)

    #Print Statements
    pprint.pprint(older)
    pprint.pprint(oldDates)
    print("Total Size of Directory: {} GB".format(formatted_size))

if __name__ == "__main__":
    purgeFilter(sys.argv[1], sys.argv[2])



