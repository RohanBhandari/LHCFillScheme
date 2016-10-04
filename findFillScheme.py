#! /usr/bin/env python

# Scrapes the fill scheme from a saved (offline) WBM "Bunch Fill" page
# Needs the following packages: BeautifulSoup4 and lxml

from bs4 import BeautifulSoup
import os.path
import sys

def hasCollision(bunch):
    nTrue=bunch.count("true")

    #Collision if at least Beam 1 and 2 are "true"
    if nTrue>=2:
        return "1"
    else:
        return "0"

def findOneFillScheme(path,filename,outdir):
    
    if not os.path.isfile(path+filename):
        sys.exit("ERROR: WBM file for "+filename+" does not exist!")

    soup = BeautifulSoup(open(path+filename),"lxml")
    
    bunchMap = soup.map
    bunches = [area for area in bunchMap.findAll("area")]

    outfile = filename.strip(".htm*")+".txt"
    
    f = open(outdir+outfile,"w")    
    
    for bunch in bunches:
        bunch_clean = hasCollision(str(bunch))
        f.write(bunch_clean+"\n")
    f.close()
    print("Saved "+outdir+outfile)

###Main Loop###

#Check arguments
if len(sys.argv)>1:
    if "help" in sys.argv[1]:
        print "This script finds fill schemes from WBM \"Bunch Fill\" webpages that have been saved locally."
        print "usage:  ./findFillScheme.py <indir>=./bunchfills/ <outdir>=./fillschemes/"
        sys.exit()
    else:
        indir = sys.argv[1]
else:
    indir = "bunchfills/"

if(len(sys.argv)>2):
    outdir = sys.argv[2]
else:
    outdir = "fillschemes/"

#Run script
fills = [file for file in os.listdir(indir) if ".htm" in file]

for fill in fills:
    findOneFillScheme(indir,fill,outdir)
