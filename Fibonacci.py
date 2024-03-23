# Write a program to generate the Fibonacci sequence up to 100.
def fib(n):

    a=0
    b=1

    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print (c);
fib(100)