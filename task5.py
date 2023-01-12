#5 Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.
from random import randint
import itertools

from task4 import get_ratios
from task4 import get_polynomial

k = randint(2, 7)

ratios1 = get_ratios(k)
polynom1 = get_polynomial(k, ratios1)
print(polynom1)

with open('Polynomial1.txt', 'w') as data:
    data.write(polynom1)
    

