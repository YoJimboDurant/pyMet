#!/usr/bin/python2.7.6 -tt

import shutil
import urllib2
from contextlib import closing
import gzip
import os
import sys

def importTD3505(startYear, stopYear, USAF, WBAN, pathDir):
    years = range(startYear, stopYear)
    
#years = ["2007","2008","2009","2010"]
#USAF = "747808"
#WBAN = "63803"
#pathDir = "gwinnett_KLZU"

    if not os.path.exists(pathDir):
        os.makedirs(pathDir)


    ftpPath = "ftp://ftp.ncdc.noaa.gov/pub/data/noaa/"
    for i in years:
    
        pathToFile = ftpPath + str(i) + "/" + USAF + "-" + WBAN + "-" + str(i) + ".gz"
        localFile = pathDir + "/SF" + USAF + "_" + WBAN + "_" + str(i) + ".gz"
        extractedFile = pathDir + "/SF" + "_" + USAF + "_" + WBAN + str(i) + ".sfc"
        print pathToFile

        with closing(urllib2.urlopen(pathToFile)) as r:
            with open(localFile, 'wb') as f:
                shutil.copyfileobj(r, f)

# Extract lines
        f = gzip.open(localFile, 'rb')
        file_content = f.read()
        f.close()
        f_out = open(extractedFile, 'wb')
        f_out.writelines(file_content)
        f_out.close()
   
def main():
    startYear = int(sys.argv[1])
    stopYear = int(sys.argv[2])
    USAF = sys.argv[3]
    WBAN = sys.argv[4]
    pathDir = sys.argv[5]

    importTD3505(startYear, stopYear, USAF, WBAN, pathDir)

# standard boilerplate:

if __name__ == '__main__':
    main()
    
    



