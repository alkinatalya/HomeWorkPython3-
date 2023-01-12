# 2 Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.
n = int(input('Введите число: ')) 
factor= list()
number = 2
while number <= n:
    if n % number == 0:
        factor.append(number)
        n //= number
    else:
        number +=1
print(factor)

    