#! /usr/bin/env python

# Gets the Fill Schemes to be analyzed

import argparse
from argparse import ArgumentDefaultsHelpFormatter
import os

#Downloads one Fill Scheme
def getOneFillScheme(fill, outdir):
    print("Downloading Fill Scheme for Fill "+fill)
    os.system('curl -L -s http://lpc.web.cern.ch/lpc/cgi-bin/schemeInfo.py\?fill\='+fill+'\&fmt\=download -o '+outdir+'fillscheme'+fill+'.txt')

#Checks for errors and if any, outputs them
def errorCheck(outdir):
    os.system('echo "$(grep error fillschemes/* | wc -l) error(s) found"')
    os.system('echo "$(grep error fillschemes/*)"')

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Gets the Fill Schemes to be analyzed", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--fill", help="Fill Scheme(s) to be downloaded. Accepts comma-separated list, e.g. 5501,5502,etc")
    parser.add_argument("-o", "--outdir", default="fillschemes/", help="Directory to save Fill Schemes to.")
#    parser.add_argument("-i", "--indir", default="fillschemes/", help="Directory from which to read the input files.")
    parser.add_argument("-E", "--errorCheck", help="Checks downloaded files for errors. Useful when downloading many files at once.", action="store_true")
    args = parser.parse_args()
    if args.outdir[-1]!='/': args.outdir+='/'

    #Get Fill Schemes
    for fill in args.fill.split(','):
        getOneFillScheme(fill, args.outdir)
    if args.errorCheck: errorCheck(args.outdir)
    
