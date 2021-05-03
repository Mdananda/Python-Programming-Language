print()
#Start Program

name = "My Name Is Md Ananda Mia"
print(name.capitalize()) #Only first character Upper case convert
print(name.casefold()) #All character convert lower Case
print(name.encode())
print(name.endswith("Mia", 10 ,len(name)))


name = "my name is ..."
print(name.index('is ...', 0, len(name)))
