def greet(name,age):
    print('My name is '+name+' and Age is '+str(age))

greet('Dhanuka',24)

def greeting(name,greet='Aloha'):
    print(f"{greet} {name}!")

greeting('Dhanuka')


#named argument

def printInfo(name,age):
    print(f'{name} {age}')

printInfo(name='Dhanuka',age=24)

#return value
def sum(a,b):
    '''
    Takes 2 integers, return their sum
    >>> sum(1,2)

    '''
    return a+b


print('Sum = '+ str(sum(1,2)))


def tipCalculate():
    foodAmount = float(input("Enter Food amount : "))
    return foodAmount+ foodAmount* 0.10


print("Food Tip Amount is : "+str((tipCalculate())))

def weatherReport(value):

    if(value=='cloudy'):
        return 'cool'
    elif(value=='sunny'):
        return 'hot'
    else:
        return 'nothing'

print(weatherReport('cloudy'))
    

def bigger_guy(a : int , b :int):
  """
  Given 2 numbers, return the bigger one.
  >>> bigger_guy(2, 3)
  3
  """
  if a>b:
    return a
  else:
    return b


print(bigger_guy(1,0))

#lembda function (implicit return)


sum2 = lambda a, b : a+b
print(sum2(5,10))