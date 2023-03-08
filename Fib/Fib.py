n = int(input())
fib1 = 1
fib2 = 1
if n != 1 and n != 2:
    for i in range(n - 2):
        fib1, fib2 = fib2, fib1 + fib2
    print(fib2)
elif n == 0:
    print(0)
elif n < 0:
    print("Неверное значение")
else:
    print(fib2)
