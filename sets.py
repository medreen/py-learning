numbers = {1, 2, 3, 4}
print(numbers)
print(type(numbers))

letters = {'k', 'l', 'u', 'm'}
print('k' in letters)
print('y' in letters)

numbers.add('Mexico')
print(numbers)

numbers.update([4, 'uli'])
print(numbers)

my_set = {23, 'ilakam', 903, 'k'}
my_set.remove(23)

print(my_set)

#my_set.remove(3)
#print(my_set)

my_set.discard('il')
print(my_set)

my_set.clear()
print(my_set)