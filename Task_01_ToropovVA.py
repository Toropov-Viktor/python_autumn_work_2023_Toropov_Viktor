#Задача 1-1

x = int(input("Введите число  "))

y = int(input("Введите число  "))

print(x+y)

print(x*y)

#Задача 1-2

x = int(input("Введите число  "))

y = int(input("Введите число  "))

res1 = x + y
res2 = x - y
res3 = x*y
res4 = x/y
res5 = x//y

if res1 > res2 and res1 > res3 and res1 > res4 and res1 > res5:
    print(res1)
elif res2 > res1 and res2 > res3 and res2 > res4 and res2 > res5:
    print(res2)
elif res3 > res1 and res3 > res2 and res3 > res4 and res3 > res5:
    print(res3)
elif res4 > res1 and res4 > res2 and res4 > res3 and res4 > res5:
    print(res4)
else:
    print(res5)

#Задача 1-3

x = int(input("Введите число  "))

y = int(input("Введите число  "))

res1 = x + y
res2 = x - y
res3 = x*y
res4 = x/y
res5 = x//y

if res1 < res2 and res1 > res3 and res1 > res4 and res1 > res5:
    print(res1)
elif res1 > res2 and res1 < res3 and res1 > res4 and res1 > res5:
    print(res1)
elif res1 > res2 and res1 > res3 and res1 < res4 and res1 > res5:
    print(res1)
elif res1 > res2 and res1 > res3 and res1 > res4 and res1 < res5:
    print(res1)
elif res2 < res1 and res2 > res3 and res2 > res4 and res2 > res5:
    print(res2)
elif res2 > res1 and res2 < res3 and res2 > res4 and res2 > res5:
    print(res2)
elif res2 > res1 and res2 > res3 and res2 < res4 and res2 > res5:
    print(res2)
elif res2 > res1 and res2 > res3 and res2 > res4 and res2 < res5:
    print(res2)
elif res3 < res1 and res3 > res2 and res3 > res4 and res3 > res5:
    print(res3)
elif res3 > res1 and res3 < res2 and res3 > res4 and res3 > res5:
    print(res3)
elif res3 > res1 and res3 > res2 and res3 < res4 and res3 > res5:
    print(res3)
elif res3 > res1 and res3 > res2 and res3 > res4 and res3 < res5:
    print(res3)
elif res4 < res1 and res4 > res2 and res4 > res3 and res4 > res5:
    print(res4)
elif res4 > res1 and res4 < res2 and res4 > res3 and res4 > res5:
    print(res4)
elif res4 > res1 and res4 > res2 and res4 < res3 and res4 > res5:
    print(res4)
elif res4 > res1 and res4 > res2 and res4 > res3 and res4 < res5:
    print(res4)
elif res5 < res1 and res5 > res2 and res5 > res3 and res5 > res4:
    print(res5)
elif res5 > res1 and res5 < res2 and res5 > res3 and res5 > res4:
    print(res5)
elif res5 > res1 and res5 > res2 and res5 < res3 and res5 > res4:
    print(res5)
elif res5 > res1 and res5 > res2 and res5 > res3 and res5 < res4:
    print(res5)
















