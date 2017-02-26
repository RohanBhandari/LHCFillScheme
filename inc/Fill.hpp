#ifndef FILL_H
#define FILL_H

#include <vector>
#include "TString.h"

class Fill{
public:
  Fill(TString file);

  // Vector of bxs for each bx type
  std::vector<int> isoBxs;     // Isolated bx
  std::vector<int> firstBxs;   // First bx in a train
  std::vector<int> lastBxs;    // Last bx in a train
  std::vector<int> middleBxs;  // Not first or last in a train
  std::vector<int> nonisoBxs;  // Non-isolated bxs (first, last, and middle)
  std::vector<int> allBxs;     // All colliding bxs (first, last, middle and iso)
  std::vector<int> emptyBxs;   // Bx with no collision
  
private:
  std::vector<bool> readFile(TString file);
  void getBxs(std::vector<bool> scheme);

};
  
#endif
