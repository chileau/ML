def pattern(n):
    for row in range(1, n+ 1):
        print(" " * (n - row)* 2 +"* " * row)

pattern(int(input("Enter the no of rows:")))
