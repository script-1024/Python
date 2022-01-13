print("* 輸入「0」可以結束此程式")

def fib(n):
    a, b = 0, 1
    result = []
    while a<n:
        result.append(a)
        a, b = b, a+b
    return result

while 1:
    n = int(input('> '))
    if n == 0: exit()
    print(f'{fib(n)}')