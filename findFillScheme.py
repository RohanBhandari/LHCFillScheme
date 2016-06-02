from bs4 import BeautifulSoup

soup = BeautifulSoup(open("/Users/rohan/Desktop/Bunch4961Fill.html"),"lxml")

bunchMap = soup.map

bunches = [area for area in bunchMap.findAll("area")]

for bunch in bunches:
    print(bunch)
