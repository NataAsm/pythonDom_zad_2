#3.	Используйте функцию map() и перепишите код

#numbers = [1, 2, 3, 4, 5]
#squared = []
#for num in numbers:
#      squared.append(num ** 2)
#print(squared)


numbers = [1, 2, 3, 4, 5]
mapped_numbers = list(map(lambda x: x ** 2, numbers))

print(mapped_numbers)