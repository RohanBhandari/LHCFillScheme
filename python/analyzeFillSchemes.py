#! /usr/bin/env python

# Analyzes a Fill Scheme file and outputs a txt file with the Bunch Map

import argparse
from argparse import ArgumentDefaultsHelpFormatter
import os


def findOneFillScheme(indir, filename, outdir):

    #List to hold bunch map
    bunches = ['0'] * 3564

    #Open Fill Scheme file 
    with open(indir+filename,'r') as input:
        #Skip to relevant information in file
        for line in input:
            if 'BEAM 1' in line: break

        for line in input:
            #Store info
            if line.strip():
                info = line.split(',')
                if info[4] == '1':
                    bunches[int(info[1])+1] = '1'
            #End of relevant information
            else: break

    #Write bunch map to file
    with open(outdir+filename,'w') as output:
        for i in range(0,len(bunches)):
            output.write(bunches[i]+'\n')

    print("Saved "+outdir+filename)

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Analyzes a Fill Scheme file and outputs a txt file with the Bunch Map", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--indir", default="fillschemes/", help="Directory from which to read the input files.")
    parser.add_argument("-o", "--outdir", default="bunchmaps/", help="Directory to save output files to.")
    args = parser.parse_args()
    if args.indir[-1]!='/': args.indir+='/'
    if args.outdir[-1]!='/': args.outdir+='/'

    #Analyzes fill schemes for all files in input directory
    fills = [file for file in os.listdir(args.indir) if ".txt" in file]
    for fill in fills:
        findOneFillScheme(args.indir, fill, args.outdir)
