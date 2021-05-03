print()
#Start Program

x = ("C", "C++", "Java", "Python", "HTML", "BASIC")
print(x[-5:-2])

list = list(x)
list[0] = "CSS"
x = tuple(list)
print(x)

print()
#Error
tpl = ("C++",) #If make a tuple, then must be use comma(,)
print(type(tpl)) #Not a Tuple

print()
#Make tuple another system
tpl = tuple(("C", "BASIC"))
print(type(tpl))