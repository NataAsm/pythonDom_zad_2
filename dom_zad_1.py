# 1.	Используя функцию map() переписать функцию
# items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
# squared.append(i**2)


def process_items(num):
    squared = num ** 2
    return squared

items = [1, 2, 3, 4, 5]
new_items = list(map(process_items, items))
print(new_items)

