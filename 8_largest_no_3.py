a=int(input("Enter first no:"))
b=int(input("Enetr second no:"))
c=int(input("Enetr third no:"))
if a>b and a>c:
    print("Largest no is", a)
elif b>c and b>a:
    print("Largest no is", b)
else:
    print("Largest no is", c)