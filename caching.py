import requests
import json
import os.path
print "******** Welcome to saral*************"
url = 'http://saral.navgurukul.org/api/courses'

fileData = ""
# by writing function we we will write file Name and  file Data
def writingFile(fileName, fileData):
    file = open(fileName, "w")
    dumps_data = json.dumps(fileData)
    file.write(dumps_data)
    file.close()

# By reading function we will read filedata and fileName
def readingfile(fileName):
    file = open(fileName, "r")
    data_file = file.read()
    load_file = json.loads(data_file)  # dict type
    return load_file

course_id_list = []
def api1Calling(url):
    fileName = "courses.json"
    if os.path.exists(fileName):
        data = readingfile(fileName)
        inside_data = data['availableCourses']
        j = 0
        for course in inside_data:
            course_id_list.append(course["id"])
            print j+1, course["name"], "exercise id ", course["id"]
            j = j+1
        return inside_data
    else:
        getData = requests.get(url)
        json_data = getData.json()
        data = writingFile(fileName, json_data)
        inside_data = json_data['availableCourses']
        j = 0
        for course in inside_data:
            course_id_list.append(course["id"])
            print j+1, course["name"], "exercise id ", course["id"]
            j = j+1
        return inside_data
url1 = 'http://saral.navgurukul.org/api/courses'
all_data = api1Calling(url1)
user_input = input("-----select course name = ")  # Here user select one course
course_id = course_id_list[user_input-1]


ID_list = []
def api2Calling(url2):
    fileName = "exerciseFolder/excersice"+str(course_id)+".json"
    if os.path.exists(fileName):
        load_exercise = readingfile(fileName)
        inside_course_data = load_exercise["data"]
        i = 0
        for course in inside_course_data:
            print i+1, course["name"], course["id"]
            ID_list.append(course["id"])
            inside_childexercise_data = course["childExercises"]
            if inside_childexercise_data == []:
                print "[]"
            else:
                j = 0
                for index in inside_childexercise_data:
                    print "\t", "\t", j+1, index["name"]
                    j = j+1
            i = i+1
        return ID_list
    else:
        get_exercise_data = requests.get(url2)
        dict_data = get_exercise_data.json()  # dict type data
        inside_course_data = writingFile(fileName, dict_data)
        load_exercise = readingfile(fileName)
        inside_course_data = load_exercise["data"]
        i = 0
        for course in inside_course_data:
            print i+1, course["name"], course["id"]
            ID_list.append(course["id"])
            inside_childexercise_data = course["childExercises"]
            if inside_childexercise_data == []:
                print "[]"
            else:
                j = 0
                for index in inside_childexercise_data:
                    print "\t", "\t", j+1, index["name"]
                    j = j+1
            i = i+1
        return ID_list

url2 = "http://saral.navgurukul.org/api/courses/"+str(course_id)+"/exercises"
a = api2Calling(url2)

up_input = raw_input(
    "----if you want to up so enter (up) and you don't want enter (n) = ")
if up_input == "up":
    data = api1Calling(url)
else:
    user_input2 = input("select exercise number")
    user_slug = a[user_input2-1]
   
    slug = []
    slug_id_list = []
    dic = {}
    def getData():
        fileName = "exerciseFolder/excersice"+str(user_slug)+".json"
        if  os.path.exists(fileName):
            load_exercise = readingfile(fileName)  # reading file data in file

            inside_course_data = load_exercise["data"]
            i = 0
            for course in inside_course_data:
                if user_slug == course["id"]:
                    i = 0
                    print i+1, course["name"], course["id"]
                    slug.append(course["slug"])
                    slug_id_list.append(course["id"])
                    inside_childexercise_data = course["childExercises"]
                    j = 1
                    for index in inside_childexercise_data:
                        slug.append(index["slug"])
                        slug_id_list.append(index["id"])
                        print "\t", "\t", j+1, index["name"]
                        j = j+1
                i = i+1
        else:
            get_exercise_data = requests.get(url2)
            dict_data = get_exercise_data.json()  # dict type data
            exercise_data = writingFile(fileName, dict_data)
            
            load_exercise = readingfile(fileName)  # reading file data in file
            inside_course_data = load_exercise["data"]
            i = 0
            for course in inside_course_data:
                if user_slug == course["id"]:
                    i = 0
                    print i+1, course["name"], course["id"]
                    slug.append(course["slug"])
                    slug_id_list.append(course["id"])
                    inside_childexercise_data = course["childExercises"]
                    j = 1
                    for index in inside_childexercise_data:
                        slug.append(index["slug"])
                        slug_id_list.append(index["id"])
                        print "\t", "\t", j+1, index["name"]
                        j = j+1
                i = i+1
        dic["slug"] = slug
        dic["child_id"] = slug_id_list
        return dic
    b = getData()
    user_input3 = input("-----which exercise you want choose number = ")
    choose_id = b["child_id"][user_input3-1]
    choose_slug = b["slug"][user_input3-1]
    

    def api3(url3):
        fileName = "contenFolder/content"+str(choose_id)+".json"
        if os.path.exists(fileName):
            containData = readingfile(fileName)
            inside_cotentData = containData["content"]
            print inside_cotentData
            return inside_cotentData
        else:
            get_contain_data = requests.get(url3)
            dict_contain_data = get_contain_data.json()
            fileData = dict_contain_data
            inside_cotentData = writingFile(fileName, fileData)
            read_data = readingfile(fileName)
            inside = read_data["content"]
            print inside
            return inside
        
    url3 = "http://saral.navgurukul.org/api/courses/" + \
        str(choose_id)+"/exercise/getBySlug?slug="+str(choose_slug)
    api3(url3)
# urla = "http://saral.navgurukul.org/api/courses/" + \
    #                 str(chose_id)+"/exercise/getBySlug?slug="+str(chose_slug)        
    while True:
            previous_input = raw_input("----enter p if you want previous and if you want next so enter n = ")
            if previous_input == "p":
                  if user_input3 == 1:
                        print "---sorry their is no page-----"
                        break
                  else:
                        user_input3=user_input3-1
                        choose_slug = b["slug"][(user_input3-1)]
                        choose_id = b["child_id"][(user_input3)]
                        print chose_slug
                        urla = "http://saral.navgurukul.org/api/courses/" + \
                        str(choose_id)+"/exercise/getBySlug?slug="+str(choose_slug)
                        previous_data = api3(urla)
                        
            elif previous_input == "n":
                  if user_input3 == (len(slug)):
                        print "sorry page is not found"
                        break
                  else:
                        user_input3=user_input3+1
                        chose_slug = b["slug"][(user_input3-1)]
                        choose_id = b["child_id"][(user_input3-1)]
                        urlb = "http://saral.navgurukul.org/api/courses/" + \
                        str(user_slug)+"/exercise/getBySlug?slug="+str(chose_slug)
                        previous_data = api3(urlb)
                        
                  

