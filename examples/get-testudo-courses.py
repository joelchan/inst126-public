"""
Use BeautifulSoup library to take directory of HTML files as input and spit out a giant text file that lists all of the course entries.

Initial use case: enable fun final projects for INST 126.
"""

from bs4 import BeautifulSoup
import os
import pandas as pd

def html_to_course_list(filepath):
    """
    Get html page and parse out course info and dump into list of course entries
    Params: filepath: path to html page
    Returns: courses: list of course entries, which can then be printed
    """

    # initialize beautifulsoup object for course html page
    soup = BeautifulSoup(open(filepath).read(), 'html.parser')

    courses = []
    # for every course (we know it's a course entry if it's a div with class = "course")
    for item in soup.find_all(attrs={"class":"course"}):
        approved_course_text = item.find_all(attrs={"class": "approved-course-text"})
        coursedetails = {
            'code': item['id'],
            'title': item.find(attrs={"class": "course-title"}).text,
        }
        # only process if there is a course description
        if len(approved_course_text) > 1:
            coursedetails['prerequisite'] = "None"
            requirements = approved_course_text[0].find_all('div')
            for requirement in requirements:
                if "Prerequisite" in requirement.text:
                    coursedetails['prerequisite'] = requirement.text.replace("Prerequisite: ", "")
            coursedetails['description'] = approved_course_text[1].text
            coursedetails['credits'] = item.find(attrs={"class": "course-min-credits"}).text
            courses.append(coursedetails)
        # # no course description
        # else:
        #     print("\nno approved course text for %s: %s" %(coursedetails['code'], coursedetails['title']))
        #     print(approved_course_text)
        #     print("\n")
        #     courses_special.append(coursedetails)
        # courses_all.append(coursedetails)
    #print(BeautifulSoup(item, 'html.parser').prettify())
    return courses

def course_d_to_text(course):
    """
    Convert a course entry (in dictionary form) to a string that can be printed more easily
    Params: course: dictionary that contains info about a course entry
    Returns: course_str: string that contains info about a course entry
    """
    course_str = "%s || %s || %s || %s || %s\n" %(course['code'], course['title'], course['description'], course['prerequisite'], course['credits'])
    return course_str

# get input directory path
INPUT_DIR = "data/fall2020-courses"

# list to hold all course info
courses_all = []

# iterate over files in directory
# assume each file is an html page that lists all courses for a given area
print("processing html pages in %s" %INPUT_DIR)
for FILENAME in os.listdir(INPUT_DIR):
    if FILENAME.endswith(".html"):
        print("Processing courses for %s" %FILENAME.replace(".html", ""))
        # get filepath
        FILEPATH = os.path.join(INPUT_DIR, FILENAME)
        # parse html to course list
        this_course_list = html_to_course_list(FILEPATH)
        # add to master course list
        courses_all += this_course_list

# write to master text file
## open file to write
OUTPUT_F = "data/testudo-courses-large.txt"
print("writing %i courses to output txt file to %s" %(len(courses_all), OUTPUT_F))
to_write = open(OUTPUT_F, 'w')
for course in courses_all:
    to_write.write(course_d_to_text(course))
to_write.close()
# # print out
# for course in courses_all[:50]:
#     print(course_d_to_text(course))

df = pd.DataFrame(courses_all)
df.to_json()