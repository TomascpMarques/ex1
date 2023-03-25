from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET


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

# data = ET.Element('biblioteca')
#
# for key in dict_genre.keys():
#     book = ET.SubElement(data, "book")
#     nome = ET.SubElement(book, "nome")
#     nome.text = str(dict_genre[key])
#     book.set("genre", key)
#     book.set("nLivros", str(len(dict_genre[key])))
#
# # criação do documento xml
# b_xml = ET.tostring(data)
# with open("Exercício3.xml", "wb") as f:
#     f.write(b_xml)