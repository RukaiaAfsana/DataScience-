
name = 'rukaia'
age = 25
print('my name is ' + name )
print('my age is ' + str(age))
print(float(age))
import random
print(random.randrange(10, 20))
txt = "i love safin"
if "hate" not in txt:
  print('NO')
else:
  print('YES')
print (txt[3:])
txt2 = "yellow blue"
print(txt2[0:2])
print(txt2[1:2])
age = 27
txt3 = ' i am rukaia my age is {}'
print(txt3.format(age))
quantity = 28
price = 23
total = quantity*price
print('I brought {} apples ,per pis price {} and total= {}'.format(quantity,price,total))
 ###lists
thislist1 = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist1)
print(thislist1[1])
print(thislist1[:3])
print(thislist1[2:])
print(thislist1[-3:])
thislist1[1] = "melon"
print(thislist1)
thislist1.append("blueberry") #append
print(thislist1)
thislist1.insert(1,"guava")
print(thislist1)
mango = ["lengra", "mohonbhog"]
thislist1.extend(mango)
print(thislist1)
thislist1.append("papaya")
print(thislist1)
thislist1.remove("apple") #remove
print(thislist1)
thislist1.pop(3) #pop
print(thislist1)

#while loop
i = 0
while i < len(thislist1):
    print(thislist1[i])
    i = i+1
    ##comprehensive
newlist1 = []
for x in thislist1:
    if "a" in x:
        newlist1.append(x)

print(newlist1)
fruits = [ x for x in thislist1 if "a" not in x]
print(thislist1)
print(fruits)
listnumber = [1,2,3,4,5,6,7,8,9,10]
print(listnumber)
newlistnumber = [ x for x in listnumber if x%2 == 0]
print(newlistnumber)
 ## range can be used as an iterable function
newliatnumber2 = [ x for x in range(11)]
print(newliatnumber2)
fruitsUpper = [x.upper() for x in thislist1]
print(thislist1)
print(fruitsUpper)
newfruit = [ x if x !="cherry" and x !="papaya" else "banana" for x in thislist1]
print(newfruit)
newfruit.sort()
print(newfruit)
newlistnumber.sort(reverse=True)
print(newlistnumber)
## values that are closeer to 50
def function01(n):
    return abs(n - 50)
testnumberlist = [30,90,45,60,10,35]
testnumberlist.sort(key = function01)
print(testnumberlist)
## append()	Adds an element at the end of the list
##clear()	Removes all the elements from the list
##copy()	Returns a copy of the list
##count()	Returns the number of elements with the specified value
##extend()	Add the elements of a list (or any iterable), to the end of the current list
##index()	Returns the index of the first element with the specified value
##insert()	Adds an element at the specified position
##pop()	Removes the element at the specified position
##remove()	Removes the item with the specified value
##reverse()	Reverses the order of the list
##sort()	Sorts the list


##TUPLES---------> 1.ordered meangs cannot be sort 2, unchangeable 3.allow duplicates
# to sort or update a tuple we need to create a list first and the pass the this by
# calling constructor tuple()
friutsTuple = ("apple","banana")
print(friutsTuple)
newfruitsTuple = ("apple",) #only one element of a tuple a " , "
print(newfruitsTuple)       # shuould be included

#dictionaries
thisdic = {
    "name" :"rukaia",
    "age" : 25,
    "mobile" : "01626416393"
}
print(thisdic)
thisdic.pop("mobile")
thisdic.popitem()
print(thisdic)
thisdic2 = {
    "name" : "prttay",
    "age" : "27",
    "mobile" : "01711267698"
}
x = thisdic2.keys()
print(x)
y = thisdic2.values()
print(y)
z = thisdic + thisdic2
print(z)
###nested
myfamily = {
    "child1" : {

    },
    "child2" : {

    },
    "child3" :{

    }
}
#####list and loop


myfamily = ["aysha","afsana","rubaya","noshin"]
versionfa = [x for x in myfamily ]
print(versionfa)
fruits = [ x for x in thislist1 if "a" not in x]
print(thislist1)
print(fruits)