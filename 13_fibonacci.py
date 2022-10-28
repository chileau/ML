n = int(input("Enter no:"))


def fib(n):
    a = 0
    b = 1
    print(a)
    for i in range(3, n+1):
        t = a
        a = b
        b = t+a
        print(a)


fib(n)
