print()
#Start Program
BookName = ["Bangla", "C++", "Algorithm", "Python"]
Books = ["Java", "Basic", "ICT"]

BookName.reverse()
len = len(BookName)-1
for i in range(len, -1, -1):
    print(BookName[i], end=" ")

