import json

from bs4 import BeautifulSoup

fd = open('xml/students.xml', 'r')

xml_file = fd.read()

soup = BeautifulSoup(xml_file, features="xml")


class Student:
    def __init__(self, name, year, testGrade):
        self.name = name
        self.year = year
        self.testGrade = testGrade

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


Students = dict[str, list[Student]]

students = Students()

for tag in soup.findAll("student"):
    for name in tag.find_all("name"):
        tempStudent = Student(
            name.string, tag.year.string, tag.testgrade.contents[0]
        )
        year = tempStudent.year.strip(",.").lower()
        if year in students.keys():
            students[year].append(tempStudent)
        else:
            students[year] = [tempStudent]

print(students)

studentsXML = BeautifulSoup('<students></students>', features="xml")
for year in students.keys():
    print(year)
    tempXML = BeautifulSoup('<year></year>', features="xml")
    tag = tempXML.year
    tag["nAlunos"] = len(students[year])
    tag["year"] = year

    for student in students[year]:
        tempStudent = BeautifulSoup('<student></student>', features="xml")
        tempTag = tempStudent.student

        nameTag = tempXML.new_tag("name")
        nameTag.string = student.name

        testGrade = tempXML.new_tag("testgrade")
        testGrade = student.testGrade

        tempTag.append(nameTag)
        tempTag.append(testGrade)
        tempXML.year.append(tempStudent)
    studentsXML.students.append(tempXML)

print(studentsXML.prettify())

# TO JSON

with open("json/ex4.json", mode='w') as fl:
    fl.write("{")
    for studentKey in students.keys():
        fl.write('"'+studentKey+'": {')
        # print(json.dumps(students[studentKey]))
        for student in students[studentKey]:
            fl.write(json.dumps(student.__dict__) + ',')
            # print(student.__dict__)
            # print(json.dumps(student.__dict__))
        fl.write('}')
    fl.write("}")


fd.close()
