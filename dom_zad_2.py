#2.	Используйте функцию reduce() и перепишите код

#product = 1
#list = [1, 2, 3, 4]
#for num in list:
 #   product = product * num

from functools import reduce

list = [1, 2, 3, 4]
print(reduce(lambda x, y: x * y, list))
