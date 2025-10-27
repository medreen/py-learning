#tuples
numbers = (10, 20, 30, 40)
numbers_list = list(numbers)
numbers_list.append(60)
numbers_list[2] = 35

numbers_clean = tuple(numbers_list)
print(numbers_clean)

#ascending order
values = (15, 5, 30, 25, 10)
values_list = list(values)
values_list.reverse()
values_cleaned = tuple(values_list)

print(values_cleaned)

#remove bananas
fruits = ('apple', 'banana', 'cherry', 'banana', 'mango', 'banana')
fruits_list = list(fruits)
print(fruits_list.count('banana'))
print(fruits_list)

#reverse order using sort
names = ('Alice', 'Bob', 'Charlie', 'David')
names_list = list(names)
names_list.sort(reverse=True)
names_cleaned = tuple(names_list)
print(names_cleaned)

#extend
colors = ("red", "blue", "green")
colors_list = list(colors)
colors_list.append('yellow')
colors_list.extend(['purple', 'orange'])
colors_clean = tuple(colors_list)
print(colors_clean)