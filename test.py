my_list = [1, 2, 'Lenox', '2', 'KBee', 2, 6, 78.223, True]

#count
print(my_list.count(2))

#index 
print(my_list.index(2))
print(my_list.index(78.223))

#sort
list2 = ['Ken', 'Janet', 'Wendy', 'Andrew', 'Carl']
list2.sort()
print(list2)

#reverse
my_list.reverse()
print(my_list)

list2.reverse()
print(list2)

#max 
nums = [1.7, 89, 7374, 982, 9]
maximum_value = max(nums)
print(maximum_value)

#min 
minimum_value = min(nums)
print(minimum_value)

#copy
copied = nums.copy()
print(copied)

#join
new_list = nums + my_list
print(new_list)

fruits = ['Watermelon', 'Banana', 'Pineapple', 'Orange']
vegetables = ['Cabbage', 'Tomato', 'Lettuce', 'Kales']

for x in fruits:
    vegetables.append(x)

print(vegetables)  


