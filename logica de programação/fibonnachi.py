#criar funçaõ
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a,b = 0,1
    for i in range (2, n+1):
        aux = b
        b = a + b
        a = aux
    return b

#main

x = int(input("insira um valor: "))
for _ in range (x):
    n = int(input("insira: "))

    print(f"Fib({n}) = {fib(n)}")
