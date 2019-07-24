import requests
import json
def writingFile(fileName,fileData):
      file=open(fileName,"w")  
      file.write(fileData)
      file.close()

# In this function we are reading a file.
def readingFile(fileName):
      file=open(fileName ,"r")
      data_file = file.read()
      loded_file = json.loads(data_file)
      return loded_file


#Api calling
def apiCalling(url):
    getData = requests.get(url)
    json_data = getData.json()
    json_string = json.dumps(json_data)

    fileName="courses.json"
    fileData=json_string
    writingFile(fileName,fileData)
    data=readingFile(fileName)
    return data

url = 'http://saral.navgurukul.org/api/courses'
saralData=apiCalling(url)   #Function Calling

#List of Saral courses
def courseList(saralData):
     for index in range(0,len(saralData['availableCourses'])):
         courseName= saralData["availableCourses"][index]["name"]
         print index+1 , ":",courseName 
courseList(saralData)

 #select course by user with help of id which is front of courses.
user_input=int(raw_input("Enter courseId:"))
Particular_courseName=saralData["availableCourses"][user_input-1]["name"]
courseId= saralData["availableCourses"][user_input-1]["id"]

print "Course Name:", Particular_courseName,", Course Id:", courseId

# def get_exercise(api2):
#         get_exerciseData=requests.get(api2)
#         exercise_data =  get_exerciseData.json()
#         stringFrom_exercise_data = json.dumps(exercise_data) #exercise data change to json string format
#         #print stringFrom_exercise_data

#         fileName = json.loads(stringFrom_exercise_data)
#         for index in range(0,len(fileName["data"])):
#                 particular_exercise_name = fileName["data"][index]["name"]
#                 print index+1,":",particular_exercise_name

               
# url2=" http://saral.navgurukul.org/api/courses"+"/"+str(courseId)+"/"+"exercises"
# get_exercise(url2)

# def get_exercise(api2,user_input):
#         get_exerciseData=requests.get(api2)
#         exercise_data =  get_exerciseData.json()
#         stringFrom_exercise_data = json.dumps(exercise_data) #exercise data change to json string format
#         print stringFrom_exercise_data

#         fileName = json.loads(stringFrom_exercise_data)
#         for index in range(0,len(fileName["data"])):
#                 particular_exercise_name = fileName["data"][index]["childExercises"]
#                 # y=fileName["data"][user_input]["name"]["childExercises"]
#                 if particular_exercise_name==[]:
#                         print []
#                 # print particular_exercise_name
                
# url2=" http://saral.navgurukul.org/api/courses"+"/"+str(courseId)+"/"+"exercises"
# user_input2 = int(raw_input("enter number"))               
# get_exercise(url2,user_input2-1)
