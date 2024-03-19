#List Array

fruits = ['apple', 'mango', 'orange', 'banana']

fruits.append('blue berry')
for i in range(0,len(fruits)):
    print(fruits[i])


#slicing 
print('-----------------------')
print(fruits[-1])
print('-----------------------')
print(fruits[0:2]) # first inclusive, second inclusive
print('-----------------------')
print(fruits[:2]) # first inclusive, second inclusive
print('-----------------------')
print(fruits[::2])

print(len(fruits))

