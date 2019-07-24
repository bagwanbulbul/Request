import requests
import json
url = 'http://saral.navgurukul.org/api/courses'
# by writing function we write file Name file Data
def writingFile(fileName,fileData):
      file = open(fileName,"wb")
      dumps_data = json.dumps(fileData)
      file.write(dumps_data)
      file.close()
# By reading function we read file data
def readingfile(fileName):
      file = open(fileName,"r")
      data_file = file.read()
      load_file = json.loads(data_file) #dict type
      return load_file

course_id_list = []      
def api1Calling(url):
      getData = requests.get(url)
      json_data = getData.json()
      json_string = json.dumps(json_data) #str type
      inside_data = json_data['availableCourses']
      j = 0
      for course in inside_data:
            course_id_list.append(course["id"])
            print j+1,course["name"],"exercise id ",course["id"]
            j = j+1

      fileName = "courses.json"
      fileData = json_string
      writingFile(fileName,fileData)
      data = readingfile(fileName)
      return data
url = 'http://saral.navgurukul.org/api/courses'
all_data =  api1Calling(url)
# Here user select one course
user_input = input("select course name")
course_id = course_id_list[user_input-1]

def api2Calling(url2):
      get_exercise_data = requests.get(url2)
      dict_data = get_exercise_data.json() # dict type data 
      jsonFileData="excersice"+str(course_id)+".json"

      #write second url data by calling writingfile functon 
      exercise_data=writingFile(jsonFileData,dict_data)
      # reading file data in file
      load_exercise=readingfile(jsonFileData)

      inside_course_data = load_exercise["data"]
      i = 0
      for course in inside_course_data:
            print i+1,course["name"],course["id"]
            inside_childexercise_data = course["childExercises"]
            j=0
            for index in inside_childexercise_data:
                  print  "\t",j+1,index["name"],index["id"]
                  j=j+1

                  # inside_exercise_slug = index["slug"]
                  # a = 0
                  # for exercise in inside_exercise_slug:
                  #       print "\t",a+1,exercise
                  #       a = a+1

            i=i+1
url2 = "http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercises"
api2Calling(url2)
print url2

url_2 = "http://saral.navgurukul.org/course?id=18&slug=python__WhatDoComputersDo"