print()
#Start Program

try:
    print("Hello")
except ArithmeticError:
    print("Any Exception !!!")
else:
    print("ABbahd")

for i in range(1, 100):
    print(i)
    if i >= 10:
        raise Exception("Does not suport more than ten !!")
