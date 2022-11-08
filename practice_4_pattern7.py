rows = int(input("Enter the number of rows: "))
# Top half
for row in range(0, rows):
    for num in range(0, row + 1):
        print(row+1, end='')
    print()
# Bottom half
for row in range(rows-1, 0, -1):
    for num in range(0, row):
        print(row, end='')
    print()
