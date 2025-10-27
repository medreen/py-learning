items = ['Magaret', 23, 45.786, False, 'This is the last item']
print(items)
print(items[0][5])
print(len(items))
print(type(items))

items[1] = 'Ramoh'
print(items)

#nested lists
value = [1, 2, 3, [4, 5, 6], [34, 56, 76], 10]
print(len(value))
print(value[3][1])
print(value[2:4]) #does not include the last index value

#append - adds a single item
value.append(11)
print(value)

#extend - adds multple values
value.extend(['Medreen', False, 45])
print(value)

#insert - adds a value at a specified index
value.insert(6, "pear")
print(value)

#remove 
value.remove('Medreen')
print(value)

#pop
value.pop()
print(value)

value.pop(4)
print(value)

#clear
value.clear()
print(value)
