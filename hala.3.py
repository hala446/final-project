import random
class  Course:

    def __init__(self,course_name,course_class):
        self.course_name=course_name
        self.course_class=course_class
    def add_course_to_list(self, courses):
        self.student_courses.append(courses)

class Student:
            def __init__(self, student_number, student_name, student_class):
                self.student_number = random.randint(1000, 9999)
                self.student_name = student_name
                self.student_class = student_class
                self.student_courses = []

def add_course(self, courses):
 self.student_courses.append(courses)



 def get_courses(self):
    print("Name\t\t||\tclass")
    for i in self.student_courses:
     print(i.course_name, "\t\t\t||\t",i.course_class)


    def get_student_details(self):
        print("id\t\t Name\t\t class")
        print(self.student_number,"\t\t\t\t",self.student_name,"\t\t\t\t" ,self.student_class)
class course:
    def __init__(self ,course_name,course_class):
        self.course_name=course_name
        self.course_class=course_class



def find_course(course_name, course_class):
  index=0
  for i in course:
      if i.course_name in course_name:
          return index
  return -1
course_list=[]
student_list = []

while True:
    x=int(input("select choice please\n" +
                "1.Add new student\n" +
                "2.remove student\n"+
                "3.edit student\n"+
                "4.display all students\n"+
                "5.create new course\n"
                "6.exict\n"))
    if x == 1:
        course_name = input("Enter Course Name")
        course_class = None
        while True:
            course_class = input("Enter Course Class")
            if course_class in ["A", "B", "C"]:
                break
                course = Course(course_name, course_class)
            course_list.append(course_list)
            print("Course Created")
    elif h == 2:
        print("____________________________")
        print("course name /t/t course class")
        student_number=int(input("enter student number"))
        search_result=find_student (student_number,student_list)
        if search_result==-1:
            print("student not exist")
        else:
            student_list[search_result].student_name=input("enter student neme")
            student_class=input("student class")

        for i in course_list:
            print(i.course_name, "/t/t", i.course_class)
            while True:
                if student_class in ("A","B","C"):
                    break
                else:
                    student_class=input("select student class (a,b,c)")
                student_list[search_result].student_class = student_class
                print("student information edited successful")
    elif x==3:
        student_number=int(input("enter student number "))
        student_result=find_student(student_number,student_list)
        if search_result==-1:
            print("student not exist")
        else:
            student_list.pop(search_result)
            print("student romved successful")
    elif x ==4:
        student_number=int(input("enter student number"))
        search_result=find_course(student_number,student_list)
        student_list[student_result].get_student_details()

    elif x ==5:
        course_name= input("enter course name")
        course_class=input("enter course class(a, b,c)")
        course=course(course_name,course_class)
        print("course created successful")
    elif x ==6:
        pass
    else:
        break
















