rows = int(input("Enter the number of rows: "))
# Top half
for row in range(0, rows):
    for star in range(0, row ):
        print("*", end=' ')
    print()
# Bottom half
for row in range(rows, 0, -1):
    for star in range(0, row ):
        print("*", end=' ')
    print()
