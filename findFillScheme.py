# Scrapes the fill scheme from a saved (offline) WBM "Bunch Fill" page
# Needs the following packages: BeautifulSoup4 and lxml

from bs4 import BeautifulSoup

def hasCollision(bunch):
    idx_true=bunch.find("true")
    idx_false=bunch.find("false")

    #Only collision if all are true (i.e. no false)
    if idx_false==-1:
        return "True"
    else:
        return "False"

dir = "/Users/rohan/Desktop/"
fill = "BunchFill4961"

soup = BeautifulSoup(open(dir+fill+".html"),"lxml")

bunchMap = soup.map
bunches = [area for area in bunchMap.findAll("area")]

f = open(fill+".txt","w")

for bunch in bunches:
    bunch_clean = hasCollision(str(bunch))
    
    f.write(bunch_clean+"\n")

