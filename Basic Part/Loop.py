print()
#Start Program

#While loop...
i = 1
while i <= 6:
    print(i, end=", ")
    i += 1
else:
    print("\nmore than 6")
#For loop...
print()

name = ["C", "C++", "Java"]
Book = ["Bangla", "English"]

for nm in name:
    for nn in Book:
        print(nm, nn)