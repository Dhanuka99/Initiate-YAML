#Doctionary 
#key value pairs 




#print(person['name'])
#print(person['shirt'])
#print(person['laptop'])


def netWorth():
    return person['asset'] - person['debt']


def introducer():
    person = {
        'name':'Dhanuka',
        'shirt':'black',
        'laptop':'apple',
        'asset' : 100,
        'debt': 50,
        'networth' : lambda : person['asset'] - person['debt'],
        'fruits': ['apple', 'mango', 'orange', 'banana']
        
    }

    

    print(f"Hi I am {person['name']}, I am wearing a {person['shirt']} color shirt, my laptop is {person['laptop']}  model and my networth is {person['networth']()} and I like {person['fruits']}")

introducer()