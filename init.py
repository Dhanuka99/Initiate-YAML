#hello world

print("Hello world")

#Data Types

print(123)
print(2.123)
print("Hello")
print('good morning')
print(True)
print(False)
#complex number
print(2 +3j)

print("Hello")
print("world")
print("Hello \nworld")

print("name\t: Dhanuka")
print("Address\t: Kurunegala")

print("Dhanuka said \"Good Morning\"")
print("Dhanuka said \'Good morning\'")

print("special character \\n gives us a new line")

#variables

name = "Dhanuka"
print("Customer name\t:"+name)

a = 10
b = 3

print(a+b)
print(a-b)
print(a*b)
print(a/b)
#modules
print(a%b)
#flor division
print(a//b)
print(a**b)
print(str(a))

#Boolean Operation
c = True
d = False

age = 50

is_young = age < 18

print(is_young)

print(c and d)
print(c or d)

print(not d)

print(type(c))

e , f = 12, 32

#TYPE conversion 

m = "10"
n = 5

print(n+int(m))

#name = input("Enter your name : ")
#print("your name is "+name)


#Data Structures

#List
x = [10,20,30,40,50]

print(x)
print(x[0])

print(x[4])
x.append(120)
print(x)
x.insert(2,500)
print(x)

x.remove(10)
print(x)
x.pop(0)
print(x)

y = [1,2,3,4]
z = [5,6,7,8]

print(y+z)

is_10_in_x = 10 in x
print(is_10_in_x)

print(not 10 in x)


#Dictionary 

w = {'1000' : "Kurunegala", '1500' : "Badulla", '2000' : "horana"}

print(w)
print(w.keys())
print(w.values())

r = {1:'A', 2: 'B', 3 : 'C'}
print(r.get(1,0))

w['1255'] = "Panadura"
print(w)

#Sets
#no duplicate values. we can not use index for when data adding or removing 
z = {"Hello", "World","Hello","1","1"}
t = {"Hello"}
print(z)
z.add("hello")
print(z)
print(z-t)
print("1" in z)


#Tuple

Dhanuka = ("Dhanuka",24,"Kurunegala", 176, "Dhanuka")

print(type(Dhanuka))
print(Dhanuka)

fname = Dhanuka[0]
print(fname)

print(Dhanuka.count("Dhanuka"))

lname, age , city , height , nickname = Dhanuka

print(lname,age,city,height,nickname)