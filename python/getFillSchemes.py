#! /usr/bin/env python

# Gets the fill schemes to be analyzed

import argparse
from argparse import ArgumentDefaultsHelpFormatter
import os

#Downloads one fill scheme
def getOneFillScheme(fill, outdir):
    os.system('curl -L -s http://lpc.web.cern.ch/lpc/cgi-bin/schemeInfo.py\?fill\='+fill+'\&fmt\=download -o '+outdir+'fillscheme'+fill+'.txt')
    print("Downloaded "+outdir+'fillscheme'+fill+'.txt')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Downloads the fill schemes to be analyzed", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("fills", help="Fill scheme(s) to be downloaded. Accepts comma-separated list, e.g. 5501,5502,etc")
    parser.add_argument("-o", "--outdir", default="fillschemes/", help="Directory to save fill schemes to")
    args = parser.parse_args()
    if args.outdir[-1]!='/': args.outdir+='/'

    #Get fill schemes
    for fill in args.fills.split(','):
        getOneFillScheme(fill, args.outdir)
    
