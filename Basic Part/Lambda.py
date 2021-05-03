print()
#Start Program

x = lambda a, b:a + 5*b
print(x(10, 5))

def name(n):
    return lambda x:x+n

nmm = name(10)
print(nmm(5))