# def add(a, b):
#     result = a + b
#     print(result)
# a = int(input())
# b = int(input())

# add(a,b)


import random


a = int(input())
b = int(input())
c = int(input())

lotto = random.sample(range(a,b),c)
print(lotto)




