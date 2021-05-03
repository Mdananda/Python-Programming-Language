print()
#Start Program

name = {
    "101":"C",
    "102":"C++",
    "103":"Java"
}

for x, y in name.items():
    print(x, y)

print(name.get("1010", "\nNone"))


dic = {
    "nam":name,
    "10":"ananda"
}
print(dic["nam"])

print()
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)