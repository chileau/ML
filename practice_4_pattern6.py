rows = int(input("Enter the number of rows: "))
# Top half
for row in range(0, rows+1):
    for star in range(0, row + 1):
        print("*", end=' ')
    print()
# Bottom half
for row in range(rows + 1, 0, -1):
    for star in range(0, row - 1):
        print("*", end=' ')
    print()
