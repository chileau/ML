def pattern(n):
    for i in range(n):
        print("  "*i, " *"*(n-i), "* "*(n-i-1)," "*i)


pattern(int(input("Enter no. of rows: ")))
