#! /usr/bin/env python

# Finds the fill scheme from a saved (offline) WBM "Bunch Fill" page

import argparse
from argparse import ArgumentDefaultsHelpFormatter
import os.path
import sys
from bs4 import BeautifulSoup

def hasCollision(bunch):
    nTrue=bunch.count("true")

    #Collision if at least Beam 1 and 2 are "true"
    if nTrue>=2:
        return "1"
    else:
        return "0"

def findOneFillScheme(path,filename,outdir):
    
    soup = BeautifulSoup(open(path+filename),"lxml")
    
    bunchMap = soup.map
    if not bunchMap:
        print("No bunch map for "+filename+". Skipping.")

    else:
        outfile = os.path.splitext(filename)[0]+".txt"    
        f = open(outdir+outfile,"w")    

        bunches = [area for area in bunchMap.findAll("area")]    
        for bunch in bunches:
            isbx = hasCollision(str(bunch))
            f.write(isbx+"\n")
        f.close()
        print("Saved "+outdir+outfile)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Finds the fill scheme from a saved (offline) WBM \"Bunch Fill\" page", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--indir", default="bunchfills/", help="Directory from which to read the input files.")
    parser.add_argument("-o", "--outdir", default="fillschemes/", help="Directory to save output files.")
    args = parser.parse_args()
    if args.indir[-1]!="/": args.indir+="/" 
    if args.outdir[-1]!="/": args.outdir+="/" 

    fills = [file for file in os.listdir(args.indir) if ".htm" in file]
    for fill in fills:
        findOneFillScheme(args.indir, fill, args.outdir)
