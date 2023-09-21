#Задача 2-1

n = int(input("n = "))

for i in range(0, 10):
    print(f"{n}*{i} = {n * i}")

#Задача 2-2

lst = [45, 78, 3, 5, 92, 1, 129, 509]

def lstminimal(lst):
    m = lst[0]
    for i in lst:
        if i < m:
            m = i
    return m
print(lstminimal(lst))

#Задача 2-3

n = int(input("n = "))

factorial = 1

for i in range(2, n + 1):
    factorial = factorial * i

print(factorial)

