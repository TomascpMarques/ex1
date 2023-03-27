from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
<<<<<<< HEAD
=======
import xmltodict, json
>>>>>>> a36fe9beb575e0a5f145b4e3464217164fb7e8db

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

data = ET.Element('continents')

<<<<<<< HEAD
# criação da tag root
def criar_continente(self, c1):
    self.continente.text = c1

=======
>>>>>>> a36fe9beb575e0a5f145b4e3464217164fb7e8db
# criação das tags children e associoação de valores
for key in dict_continent.keys():
    continente = ET.SubElement(data, 'continente')

    nome = ET.SubElement(continente, 'nome')
    nome.text = dict_continent[key].name

    nPaises = ET.SubElement(continente, 'nPaises')
    nPaises.text = str(len(dict_continent[key].contries))
<<<<<<< HEAD

# criação do documento xml
b_xml = ET.tostring(data)
with open("Exercício1.xml", "wb") as f:
    f.write(b_xml)
=======

# criação do documento xml
b_xml = ET.tostring(data)
with open("Exercício1.xml", "wb") as f:
    f.write(b_xml)

fd2 = open("Exercício1.xml", "r")
xmltopythonFile = fd2.read()
souppy = BeautifulSoup(xmltopythonFile, features="xml")
print(souppy.prettify())
xmlDict = xmltodict.parse(souppy.prettify())
open("Exercício1.json", "w").write(json.dumps(xmlDict))
>>>>>>> a36fe9beb575e0a5f145b4e3464217164fb7e8db
