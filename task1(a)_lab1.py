try:
    n = int(input('Потрібно ввести ціле число, для якого буде шукатись дільник: '))

    while n <= 0:
        n = int(input('Недопустиме значення змінної, будь ласка введіть інше число: '))

    c1 = 1
    print(f"Дільники числа {n}:")
    while c1 <= n:
        if n % c1 == 0:
            print (c1)
        c1 += 1

except:
    print('Недопустиме значення змінної, потрібно ввести ціле число: ')

    print('Hello GitHub')