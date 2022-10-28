fact=1
def fact_n(num):
    if num==1 or num==0:
        return 1
    else:
        return num*fact_n(num-1)

n = int(input("Enter the no for which you need a factorial: "))
print(fact_n(n))
