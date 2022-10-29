a=0
b=1
c=a+b
def fib(x):
    
    if(x>0):
        a=b
        b=c
        c=a+b
    print(a)
fib(5)