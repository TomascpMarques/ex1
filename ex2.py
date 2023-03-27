import json

import lxml.etree as ET
from bs4 import BeautifulSoup

fd = open('xml/gamelist.xml', 'r')

xml_file = fd.read()

soup = BeautifulSoup(xml_file, features="lxml")


class Game:
    def __init__(self, name, desc, rating, releaseDate, developer, publisher, genre, players):
        self.name = name
        self. desc = desc
        self. rating = rating
        self. releaseDate = releaseDate
        self. developer = developer
        self. publisher = publisher
        self. genre = genre
        self. players = players


Games = list[Game]

games = Games()

for tag in soup.findAll("game"):
    for x in tag.find_all("name"):
        tempGame = Game(
            x.string, tag.desc.string, tag.rating.string, tag.releasedate.string,
            tag.developer.string, tag.publisher.string, tag.genre.string, tag.players.string
        )
        games.append(tempGame)

print(tempGame)

gameXML = BeautifulSoup('<games></games>', features="xml")
for game in games:
    tempXML = BeautifulSoup('<game></game>', features="xml")
    tag = tempXML.game
    tag["playerCount"] = game.players
    tag["released"] = game.releaseDate

    nameTag = tempXML.new_tag("name")
    nameTag.string = game.name

    descTag = tempXML.new_tag("description")
    descTag.string = game.desc[0:100] + '...'

    genreTag = tempXML.new_tag("genre")
    genreTag.string = game.genre

    tag.append(nameTag)
    tag.append(descTag)
    tag.append(genreTag)
    gameXML.games.append(tempXML)

print(gameXML.prettify())

# TO JSON
with open("json/ex2.json", mode='w') as fl:
    fl.write("{")
    for game in games:
        fl.write(json.dumps(game.__dict__) + ',')
    fl.write("}")


fd.close()
