name=input("Enter a string: ")
countOfLetter=0
countOfDigit=0
for i in name:
    # print(i,end=" ")
    if i.isalpha():
        countOfLetter+=1
    elif i.isdigit():
        countOfDigit+=1
print(countOfLetter,countOfDigit)            
