print()
#Start Progranm

def name(*nm):
    print(type(nm))
name("C", "C++", "Java")

def my_function(**kid):
  print("His last name is " + kid["an"])
my_function(nm = 1001, an = "10002")

def Rakib(nam1, nam2, nam3):
    print("name = ",nam2)
Rakib(nam1="Sakib", nam2="Shati", nam3="Ujjal")


def Jog(nm):
    if nm > 0:
        sum = nm;
        print(sum)
        Jog(nm-1)

print(Jog(4))


