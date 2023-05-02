# print("Hello",end=" ")
# print("World")

n=int(input("Enter a number: "))

i=0

while i<n:
    y=0
    while y<i:
        print("*",end=" ")
        y=y+1

    i=i+1
    print()


while i>0:
    y=0
    while y<i:
        print("*",end=" ")
        y=y+1

    i=i-1
    print()
