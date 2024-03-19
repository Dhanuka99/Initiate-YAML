#touples
#immiutable - can not change data
number = (1,2,3)

print(number)
print(number[0])


#SETS  used for getting unique elements (ignores duplicate values)


list1 = ['ruby','python', 'javascript']
list2 = ['ruby', 'sql', 'java', 'javascript']

###Special ketywords ###
#list, len, max, min. dict, set

programmingLanguages = list1+list2
print(programmingLanguages)

print({1,2,2,2,2,1,1,3,3})
things = (1,2,3,1,1,1)
print(1 in things)
print(5 in things)

print(set(programmingLanguages))


def unique(languages):
    return set(languages)


print(unique(['ruby, ruby, JS, JS, Python']))
