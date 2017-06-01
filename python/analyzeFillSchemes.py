#! /usr/bin/env python

# Analyzes a fill scheme file and outputs a txt file with the bunch pattern
import argparse
from argparse import ArgumentDefaultsHelpFormatter
import os

def analyzeOneFillScheme(indir, filename, outdir):

    #List to hold bunch pattern
    bunches = ['0'] * 3564

    noErrors = True
    with open(indir+filename,'r') as input:
        #Check for errors
        if 'error' in input.readline():
            noErrors = False

        for line in input:
            #Skip to relevant information in file
            if 'BEAM 1' not in line: 
                continue
           
            #Store info
            for line in input:           
                if line.strip():
                    info = line.split(',')
                    if info[4] == '1':
                        bunches[int(info[1])+1] = '1'
                #End of relevant information
                else: break

    #Write bunch pattern to file
    if noErrors:
        outfile = filename.replace('fillscheme','bunchpattern')
        with open(outdir+outfile,'w') as output:
            for i in range(0,len(bunches)):
                output.write(bunches[i]+'\n')
        print("Saved "+outdir+outfile)
    else:
        print("\033[31m"+"Error with "+filename+". Please check file."+"\033[0m")

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Analyzes a fill scheme file and outputs a txt file with the bunch pattern", formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--indir", default="fillschemes/", help="Directory from which to read the input files")
    parser.add_argument("-o", "--outdir", default="bunchpatterns/", help="Directory to save output files to")
    args = parser.parse_args()
    if args.indir[-1]!='/': args.indir+='/'
    if args.outdir[-1]!='/': args.outdir+='/'

    #Analyzes fill schemes for all files in input directory
    for fill in [file for file in os.listdir(args.indir) if file.endswith('.txt')]:
        analyzeOneFillScheme(args.indir, fill, args.outdir)
