from bs4 import BeautifulSoup


class Coutry:
    def __init__(self, code, handle, continent, iso):
        self.code = code
        self.handle = handle
        self.continent = continent
        self.iso = iso

class Continent:
    def __init__(self, name, contryNumber, contries):
        self.name = name
        self.contryNumber = contryNumber
        self.contries = contries

fd = open("xml/countries.xml", "r")

xml_file = fd.read()

soup = BeautifulSoup(xml_file, features="xml")

dict_continent = {}

for tag in soup.find_all("country"):
     if tag["continent"] not in dict_continent.keys():
         continentX = Continent(tag["continent"], 1, [Coutry(tag["code"], tag.text, tag["continent"], tag["iso"])])
         dict_continent[tag["continent"]] = continentX
     else:
         continentX = dict_continent[tag["continent"]]
         continentX.contries.append(Coutry(tag["code"], tag.text, tag["continent"], tag["iso"]))


