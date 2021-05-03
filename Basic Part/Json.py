print()
#Start Program

import json

name= '["C", "C++", "Python", "Java"]' #Json Type data
x = json.loads(name) #Json convert to list
print(x[0])

name = ["C", "C++", "OOP", "Data"]
x = json.dumps(name) #list convert to json
print(x)