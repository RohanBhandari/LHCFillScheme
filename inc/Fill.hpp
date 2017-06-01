#ifndef FILL_H
#define FILL_H

#include <vector>
#include "TString.h"

class Fill{
public:
  Fill(TString file);

  // Vector of BXs for each BX type
  std::vector<int> isoBXs;     // Isolated BX
  std::vector<int> firstBXs;   // First BX in a train
  std::vector<int> lastBXs;    // Last BX in a train
  std::vector<int> middleBXs;  // Not first or last in a train
  std::vector<int> nonisoBXs;  // Non-isolated BXs (first, last, and middle)
  std::vector<int> allBXs;     // All colliding BXs (first, last, middle and iso)
  std::vector<int> emptyBXs;   // BX with no collision
  
private:
  std::vector<bool> readFile(TString file);
  void getBXs(std::vector<bool> scheme);

};
  
#endif
