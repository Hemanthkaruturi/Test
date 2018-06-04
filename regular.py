import re

text = '''
        John is 13 years old
        and Jonathan is 26 years old
        '''

print(text)
age = re.findall(r'\d{1,3}', text, flags=0)

names = re.findall(r'[A-Z][a-z]*', text, flags=0)

print(age)

print(names)
agedict = {}

x = 0

for eachname in names:
    agedict[eachname] = age[x]
    x+=1

print(agedict)
