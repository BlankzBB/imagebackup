from os import listdir
from os.path import isfile, join
import zipfile
import time

seconds = 600 # Default is 10 minutes (10 * 60)
picDir = "xxx/" #if you edit this, make sure there is a / at the end
archiveDir = "xxx/"#if you edit this, make sure there is a / at the end of archiveDir or at the beginning of archiveName
archiveName = "Default.zip"
compression = True #True or False.
archive = archiveDir+archiveName

def main():
    while 1 > 0:
        check = archiveCheck() #checking if the archive exists
        pics = fileCheck(check) #making a list of images that arent in the archive
        cType = compress() #if compression is on or not
        archiveWrite(pics, check, cType) #the good stuff
        print('sleeping for '+str(seconds/60) +" minutes")
        time.sleep(seconds)#zzz

def archiveCheck():
    if zipfile.is_zipfile(archive) is True:#checking if archive is a zipfile.
        print('Archive exists')
        return True
    else:
        print("Archive does not exist")
        return False

def fileCheck(check):
    if check is True:#if check is true, getting ready to compare images to the ones in the zip
        r = zipfile.ZipFile(archive, 'r')
        archivedFiles = r.namelist()#making a list of files in the archive
        r.close()

    files = [i for i in listdir(picDir) if isfile(join(picDir, i))]#grabbing file names with extentions
    pics = []
    for i in files:
        if i.find(".png") != -1 or i.find(".jpg") != -1:#if .png or .jpg is included in the file (ex file: aasdf.jpg)
            if check is True:
                if i in archivedFiles:#checking if it is in the zip
                    print(i +" is in archive")
                else:
                    print(i+ ' is not in archive')
                    pics.append(i)
            else:
                print("Adding "+i +" to a new archive")
                pics.append(i)
    return pics

def compress():#making a variable for compression type depending on the variable above
    if compression is True:
        print("Compression is on")
        cType = zipfile.ZIP_DEFLATED
    if compression is False:
        print("Compression is off")
        cType = zipfile.ZIP_STORED
    return cType

def archiveWrite(pics, check, cType):

    if check is True:#if the archive exists, we append
        zip = zipfile.ZipFile(archive, 'a', cType)
        print("Appending to archive")
    else:#if the archive does not exist, we can write a new one
        zip = zipfile.ZipFile(archive, 'w', cType)
        print("Creating and writing to archive")

    for i in pics:
        file = picDir+i
        zip.write(file, arcname=i)#writing the file to the zip
        print("Added "+i +" to archive")
    zip.close()
    print("The archive is located at "+archive)
main()#starting the program