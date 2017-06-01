#! /usr/bin/env python

# Downloads and analyzes a fill scheme

import argparse
from argparse import ArgumentDefaultsHelpFormatter
from python.getFillSchemes import *
from python.analyzeFillSchemes import *

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Downloads and analyzes a fill scheme", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("fills", help="Fill scheme number(s). Accepts comma-separated list, e.g. 5501,5502,etc")
    parser.add_argument("-i", "--indir", default="fillschemes/", help="Directory to save the fill schemes to")
    parser.add_argument("-o", "--outdir", default="bunchpatterns/", help="Directory to save the analyzed output to")
    args = parser.parse_args()
    if args.indir[-1]!='/': args.indir+='/'
    if args.outdir[-1]!='/': args.outdir+='/'

    #Process fill schemes
    for fill in args.fills.split(','):
        getOneFillScheme(fill, args.indir)
        filename = 'fillscheme'+fill+'.txt'
        analyzeOneFillScheme(args.indir, filename, args.outdir)
        print('')
 
