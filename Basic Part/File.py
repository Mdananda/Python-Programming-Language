print()
#Start Program

import os
'''
file = open("Ananda.txt", 'r')
print(file.readline()) #print the one by one line
print(file.read()) #print all text file

for x in file:
    print(x, end="")

file.close()
'''

f = open("Ananda.txt", 'w')
f.write("My Name Is Md Ananda\nCSE-PUST")
f.close()
