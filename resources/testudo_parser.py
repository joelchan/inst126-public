import urllib # for web scraping
from bs4 import BeautifulSoup # for parsing the html
import pandas as pd

# params 
# TODO: can make into command-line args or params for a function
outputname = "INST_Fall2022.csv"
query = "https://app.testudo.umd.edu/soc/search?courseId=INST&sectionId=&termId=202208&_openSectionsOnly=on&creditCompare=%3E%3D&credits=0.0&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on"

print("Getting the data from testudo...")
# get the html page
html = urllib.request.urlopen(query).read()

print("Initializing html parser")
# init parser
soup = BeautifulSoup(html, 'html.parser')

# to hold the course data
courses = []

print("Parsing all the courses...")
# grab all the divs that have class 'course' (these are all the courses)
# and iterate through them
for course in soup.find_all(class_="course"):
    # code is the id of this div
    code = course.get('id')
    # title is in text of div that has class 'course-title'
    title = course.find(class_="course-title").text

    # grab the description and prereqs
    # all are of class `approved-course-text` with only in-text (not html) distinctions of type :/
    # so we gotta iterate through all the course texts and check for the prereq
    description = ""
    prereq = "None"
    # get all the divs that have class `approved-course-text` 
    # and iterate through them
    for descr in course.find_all(class_="approved-course-text"):
        # get the text of the div
        d_text = descr.text
        # it's prereq if it has `Prerequisite:` in it
        if "Prerequisite:" in d_text:
            # if it is, then set the value of prereq to this text
            prereq = d_text
        else: 
            # otherwise, add to the general course description text bundle
            description += d_text
    # credits in text of div that has class `course-min-credits`
    credits = course.find(class_="course-min-credits").text

    # ok now stitch all the data together into a dict to add 
    # as an entry for this course to our course data list
    courses.append({
        'Code': code,
        'Title': title,
        'Description': description,
        'Prereqs': prereq,
        'Credits': credits
    })

# and convert to dataframe!
courses = pd.DataFrame(courses)

print(f"Done! Saving the data to {outputname}...")
# save the resulting dataframe to csv
courses.to_csv(outputname)