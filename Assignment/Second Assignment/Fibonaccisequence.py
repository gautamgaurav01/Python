# fibonacci sequence


def fibonacci(n):
    if n == 0:
        return n
    if n <= 2:
        return n - 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


number = int(input("Enter how many terms you want in the Fibonacci series: "))
for i in range(0, number):
    print(fibonacci(i))
