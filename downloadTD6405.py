#!/usr/bin/python2.7.6 -tt

import shutil
import urllib2
from contextlib import closing
import gzip
import os
import sys

def importTD6405(startYear, stopYear, call, pathDir):
    years = range(startYear, stopYear+1)
    
#years = ["2007","2008","2009","2010"]
#USAF = "747808"
#WBAN = "63803"
#pathDir = "gwinnett_KLZU"

    if not os.path.exists(pathDir):
        os.makedirs(pathDir)


    ftpPath = "ftp://ftp.ncdc.noaa.gov/pub/data/asos-onemin/6405-"
    months = range(1,13)
    months = [str(x).zfill(2) for x in months]
    for i in years:
    
        for j in months:
            pathToFile = ftpPath + str(i) + "/64050" + call + str(i) + j + ".dat" 
            localFile = pathDir + "/64050" + call  + str(i) + j+ ".dat"
            print pathToFile
            with closing(urllib2.urlopen(pathToFile)) as r:
                with open(localFile, 'wb') as f:
                    shutil.copyfileobj(r, f)


def main():
    startYear = int(sys.argv[1])
    stopYear = int(sys.argv[2])
    call = sys.argv[3]
    pathDir = sys.argv[4]
    importTD6405(startYear, stopYear, call, pathDir)

# standard boilerplate:

if __name__ == '__main__':
    main()
    
    



