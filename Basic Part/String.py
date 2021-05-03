print()
#Start Program

name = "   My Name is Md Ananda Mia"
print(name.strip())

print()
name = """My Name is Md Ananda Mia,
My Father name Md Harun- Or-Rashid,
My HomeTown Jamalpur."""
print(name.strip())

name = "\nMD ANANDA mia"
print(name.upper())

name = "Pabna district"
xx = "pabna" in name
print(xx)
print(name.replace("di", "DI"))
print(name.split())

name1 = "\nMd Ananda"
name2 = "Mia"
name = name1+" "+name2
print(name)

age = 20
name = "I am Ananda Mia. I am {}"
print(name.format(age))

name = "My name is \"Md Ananda Mia\" "
print(name)

