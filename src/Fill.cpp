#include <fstream>
#include <iostream>

#include "TString.h"

#include "../inc/Fill.hpp"

using namespace std;

Fill::Fill(TString file){
  vector<bool> scheme = readFile(file);
  getBXs(scheme);
}

vector<bool> Fill::readFile(TString filename){

  vector<bool> scheme;
  ifstream file(filename);
  if(!file.is_open()){ 
    cout<<"\n\e[31mERROR:\e[0m File "<<filename<<" does not exist!"<<endl; 
    exit(0);
  }
  string str;
  while(getline(file,str))
    if(str=="1") scheme.push_back(true);
    else scheme.push_back(false);

  file.close();

  return scheme;
}

void Fill::getBXs(vector<bool> scheme){

  // Loop over BXs between [1,3562], the last two require special treatment
  bool prevBX, bx, nextBX;
  for(unsigned int ibx=1; ibx<3563; ibx++){
    prevBX = scheme[ibx-1];
    bx = scheme[ibx];
    nextBX = scheme[ibx+1];

    if(bx                      ){ allBXs.push_back(ibx);                              }
    if(bx && !prevBX && !nextBX){ isoBXs.push_back(ibx);                              }
    if(bx && !prevBX && nextBX ){ firstBXs.push_back(ibx);  nonisoBXs.push_back(ibx); }
    if(bx && prevBX  && !nextBX){ lastBXs.push_back(ibx);   nonisoBXs.push_back(ibx); }
    if(bx && prevBX  && nextBX ){ middleBXs.push_back(ibx); nonisoBXs.push_back(ibx); }
    if(!bx                     ){ emptyBXs.push_back(ibx);                            }
  }  

  // Add BX 3563, which is part of the abort gap and is always empty
  emptyBXs.push_back(3563);

  // Add last BX, which is the last bunch of the abort gap and is always empty
  // In the CMS numbering scheme this is BX=0, but HCAL PFG tuples follows the LHC numbering scheme in which this is BX=3564
  emptyBXs.push_back(3564);
}
