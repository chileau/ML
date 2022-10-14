n=int(input("Enter limit:"))
i=0
max=0
while i<n:
    num=int(input("Enter the no: "))
    if num>max:
        max=num
    i+=1
print("Maximum value entered is:", max)