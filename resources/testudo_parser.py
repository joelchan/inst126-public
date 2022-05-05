import urllib # for web scraping
from bs4 import BeautifulSoup # for parsing the html

# get the html page
query = "https://app.testudo.umd.edu/soc/search?courseId=INST&sectionId=&termId=202208&_openSectionsOnly=on&creditCompare=%3E%3D&credits=0.0&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on"
html = urllib.request.urlopen(query).read()

# init parser
soup = BeautifulSoup(html, 'html.parser')

# print all the course names
# TODO: parse out to get info like before, and dump into csv
for course in soup.find_all(class_="course"):
    print(course.get('id'))