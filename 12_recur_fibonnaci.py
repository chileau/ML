def r_fib(n):
    if n <= 1:
        return n
    else:
        return r_fib(n-1)+r_fib(n-2)


n = int(input("Enter no:"))
for i in range(n):
    print(r_fib(i))
