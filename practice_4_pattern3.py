def pattern(n):
    space = n - 1
    for i in range(0, n):
        for j in range(0, space):
            print(end=" ")
        space = space - 1
        for j in range(0, i+1):
            print("* ", end="")
        print()


pattern(int(input("Enter the no of rows:")))
