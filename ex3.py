from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import xmltodict, json

fd = open("xml/livros.xml", "r")

xml_file = fd.read()

soup = BeautifulSoup(xml_file, features="xml")
dict_genre = {}

for book in soup.find_all("book"):
    if book.find("genre").text not in dict_genre.keys():
       dict_genre[book.find("genre").text] = [book.find("title").text]
    else:
        dict_genre[book.find("genre").text].append(book.find("title").text)

print (dict_genre)

data = ET.Element('biblioteca')

for key in dict_genre.keys():
    book = ET.SubElement(data, "book")
    nome = ET.SubElement(book, "nome")
    nome.text = str(dict_genre[key])
    book.set("genre", key)
    book.set("nLivros", str(len(dict_genre[key])))

# criação do documento xml
b_xml = ET.tostring(data)
with open("Exercício3.xml", "wb") as f:
    f.write(b_xml)

#xml to json
fd2 = open("Exercício3.xml", "r")
xmltopythonFile = fd2.read()
souppy = BeautifulSoup(xmltopythonFile, features="xml")
xmlDict = xmltodict.parse(souppy.prettify())
open("Exercício3.json", "w").write(json.dumps(xmlDict))

#xml to xsl
fd3 = open("teste.xml", "r")

dom = ET.parse(fd2)
xslt = ET.parse(fd3)
transform = ET.XSLT(xslt)
newdom = transform(dom)
print(ET.tostring(newdom, pretty_print=True))

