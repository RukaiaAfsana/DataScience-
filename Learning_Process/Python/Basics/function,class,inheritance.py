
def account(name, amount):
    ID = name+"123Bank"
    return ID, amount+200
print(account( "afsana" , 200))

##multiple arguments:
def food(*fruits):
    print("name of first fruit is:"+fruits[0])
    print("name of 3rd fruit is:" + fruits[2])
food("mango","banana","apple")

def student(name,roll,result):
    print("student name is :" + name)
    print("student roll is :" + roll)
    print("student result is :{}".format(result))
student(name="kola", roll="1234",result=3.30)

##multiple keyword arguments
#example 01
def students(**results):
   print("bangla result is :" +results["bangla"])
   print("english result is :" +results["eng"])
   print("math result is :"+results["math"])
students(bangla = "A+",eng ="C+", math ="D+",bio ="B+")
#example 02
def books(**details):
    print("book name is :"+ details["name"])
    print("book price is :"+details["price"])
    print("book's page number is: {}".format(details["pagenumber"]))
books(name = "introduction to married life", price ="30000tk", pagenumber = 4000000)

##passing a list
def fruits(mangos):
    for x in mangos:
        print(x)
mangos = ["mohonbho","lengra"]
fruits(mangos)

def flowers(flower):
    for x in flower:
        print(x)

flower = ["rose","waterlily","lily"]
flowers(flower)
##for loop
for x in range(2,7,2):
    print(x)

class students:
    def __init__(self,name,id,cgpa):
        self.name = name
        self.id = id
        self.cgpa = cgpa
    def student_result(self):
        print(self.name+"'s result of this semi is:"+self.cgpa)
s1 = students("afsana" , "2323" , "3.30")
s1.student_result()
s2 = students("prattay","2222","fail")
s2.student_result()
##INHERITENCE
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def person(self):
        print("the person's name is:" +self.name)
        print("the person's Age is: {}".format(self.age))
class Student(Person):
    def __init__(self,name,age,year, school, ID):
        super().__init__(name, age)
        self.year = year
        self.school = school
        self.ID = ID
    def studentDetails(self):
        print("student name:"+self.name)
        print("student age: {}".format(self.age))
        print("student year:{}".format(self.year))
        print("student school :"+self.school)
        print("student ID:"+self.ID)
p1=Person("rukaia",28)
p1.person()
Stu1 = Student("rukaia", 26, 2009, "south point", "14-2995-3")
#Stu1.person()
Stu1.studentDetails()
##ITERATOR
fruits = ["mango", "apple", "banana"]
it = iter(fruits)
i=0
while i<3:
    print(it.__next__())
    i=i+1




