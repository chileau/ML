def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*", end="")
        print()

pattern(int(input("Enter the no of rows:")))