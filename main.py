from bs4 import BeautifulSoup

fd = open('xml/example.xml', 'r')

xml_file = fd.read()

soup = BeautifulSoup(xml_file, 'lxml')

for tag in soup.findAll("item"):
    # print(tag)
    print(tag["name"])
    print(tag.text)

fd.close()
