a = 0

def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

for x in range(1,4000000):
    if fib(x)%2 == 0:
        a = fib(x)+a
    elif fib(x)>4000000:
        break
print a
