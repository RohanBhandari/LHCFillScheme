# Scrapes the fill scheme from a saved (offline) WBM "Bunch Fill" page
# Needs the following packages: BeautifulSoup4 and lxml

from bs4 import BeautifulSoup
import os.path
import sys

def hasCollision(bunch):
    nTrue=bunch.count("true")

    #Collision if at least Beam 1 and 2 are "true"
    if nTrue>=2:
        return "1"
    else:
        return "0"

def findOneFillScheme(path,filename,outdir):
    
    if not os.path.isfile(path+filename+".html"):
        sys.exit("ERROR: WBM file for "+filename+" does not exist!")

    soup = BeautifulSoup(open(path+filename+".html"),"lxml")
    
    bunchMap = soup.map
    bunches = [area for area in bunchMap.findAll("area")]
    
    f = open(outdir+filename+".txt","w")    
    
    for bunch in bunches:
        bunch_clean = hasCollision(str(bunch))
        f.write(bunch_clean+"\n")
    f.close()
    print("Saved "+outdir+filename+".txt")

#Main Loop
dir = "/Users/rohan/Desktop/"
outdir = "fillschemes/"

#2016
fills = [
    #Run2016B
    "BunchFill4888","BunchFill4889","BunchFill4890","BunchFill4892","BunchFill4895",
    "BunchFill4896","BunchFill4905","BunchFill4906","BunchFill4910","BunchFill4915",
    "BunchFill4919","BunchFill4924","BunchFill4925","BunchFill4926","BunchFill4930",
    "BunchFill4935","BunchFill4937","BunchFill4942","BunchFill4945","BunchFill4947",
    "BunchFill4953","BunchFill4954","BunchFill4956","BunchFill4958","BunchFill4960",
    "BunchFill4961","BunchFill4964","BunchFill4965","BunchFill4976","BunchFill4979",
    "BunchFill4980","BunchFill4984","BunchFill4985","BunchFill4988","BunchFill4990",
    "BunchFill5005","BunchFill5013","BunchFill5017","BunchFill5020","BunchFill5021",
    "BunchFill5024","BunchFill5026","BunchFill5027","BunchFill5028","BunchFill5029",
    "BunchFill5030",

    #Run2016C
    "BunchFill5038","BunchFill5043","BunchFill5045","BunchFill5048","BunchFill5052",
    "BunchFill5056","BunchFill5059","BunchFill5060","BunchFill5069","BunchFill5071",

    #Run2016D
    "BunchFill5072","BunchFill5073","BunchFill5076","BunchFill5078","BunchFill5080",
    "BunchFill5083","BunchFill5085","BunchFill5091","BunchFill5093","BunchFill5095",

    #Run2016E
    "BunchFill5096","BunchFill5097","BunchFill5101","BunchFill5102","BunchFill5105",
    "BunchFill5106","BunchFill5107","BunchFill5108","BunchFill5109","BunchFill5110",
    "BunchFill5111","BunchFill5112","BunchFill5116","BunchFill5117",

    #Run2016F
    "BunchFill5149","BunchFill5151","BunchFill5154","BunchFill5161","BunchFill5162",
    "BunchFill5163"
    ]

for fill in fills:
    findOneFillScheme(dir,fill,outdir)
