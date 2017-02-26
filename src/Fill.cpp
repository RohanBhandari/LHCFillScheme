#include <fstream>
#include <iostream>

#include "TString.h"

#include "../inc/Fill.hpp"

using namespace std;

Fill::Fill(TString file){
  vector<bool> scheme = readFile(file);
  getBxs(scheme);
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

void Fill::getBxs(vector<bool> scheme){

  //Account for first bx (always empty)
  emptyBxs.push_back(0);

  bool prevBx, bx, nextBx;
  for(unsigned int ibx=1; ibx<3563; ibx++){
    prevBx = scheme[ibx-1];
    bx = scheme[ibx];
    nextBx = scheme[ibx+1];

    if(bx                      ){ allBxs.push_back(ibx);                              }
    if(bx && !prevBx && !nextBx){ isoBxs.push_back(ibx);                              }
    if(bx && !prevBx && nextBx ){ firstBxs.push_back(ibx);  nonisoBxs.push_back(ibx); }
    if(bx && prevBx  && !nextBx){ lastBxs.push_back(ibx);   nonisoBxs.push_back(ibx); }
    if(bx && prevBx  && nextBx ){ middleBxs.push_back(ibx); nonisoBxs.push_back(ibx); }
    if(!bx                     ){ emptyBxs.push_back(ibx);                            }
  }  
  //Account for last bx (always empty)
  emptyBxs.push_back(3563);
}
