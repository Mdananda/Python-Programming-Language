print()
#Start program

X = 10
x = "Ananda"
print("The Number is",X)

a, b, c = "A", "B", 10
print(a, b, c)

#Local Vs Global Variable- 01
print()
p = "My Name is Md Ananda Mia"

def Numberprint():
    p = 101835
    print("The Number is",p," =Date Type", type(p))

Numberprint();
print("The String is "+p)

#Local Vs Global Variable- 02
print()
name = "Md Ananda Mia"
def Name_print():
    global name
    name = "Shati akhter"
    print("Name "+name)

Name_print()
print("Name : "+name)
