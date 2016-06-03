# Scrapes the fill scheme from a saved (offline) WBM "Bunch Fill" page
# Needs the following packages: BeautifulSoup4 and lxml

from bs4 import BeautifulSoup

def hasCollision(bunch):
    idx_true=bunch.find("true")
    idx_false=bunch.find("false")

    #Only collision if all are true (i.e. no false)
    if idx_false==-1:
        return "1"
    else:
        return "0"

def findOneFillScheme(path,filename,outdir):

    soup = BeautifulSoup(open(path+filename+".html"),"lxml")
    
    bunchMap = soup.map
    bunches = [area for area in bunchMap.findAll("area")]
    
    f = open(outdir+fill+".txt","w")
    
    for bunch in bunches:
        bunch_clean = hasCollision(str(bunch))
        f.write(bunch_clean+"\n")
    f.close()
    print("Saved "+outdir+fill+".txt")

#Main Loop
dir = "/Users/rohan/Desktop/"
fills = ["BunchFill4919","BunchFill4924","BunchFill4961","BunchFill4964"]
outdir = "fillschemes/"

for fill in fills:
    findOneFillScheme(dir,fill,outdir)
