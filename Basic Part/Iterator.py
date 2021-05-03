print()
#Start Program

name = ["C++", "C", "Python", "Java"] #iterator object
x = iter(name)
print(next(x))
print(next(x)) #iterator

class MyName:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a = x + 1
            return x
        else:
            raise StopIteration

pp = MyName()
p = iter(pp)

for x in p:
    print(x)


