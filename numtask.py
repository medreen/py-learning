#convert to int
temp = 56.8926
temp_int = round(temp)
print(temp_int)

#convert to 2dp
temp_float = round(temp, 2)
print(temp_float)

#convert to 3dp
temp_3dp = round(temp, 3)
print(temp_3dp)

#to 8.926
temp_str = str(temp)
index_str = temp_str.index("8")
print(index_str)

new_temp1 = temp_str[4:]
new_temp1 = temp_str[3] + '.' + new_temp1
new_temp = float(new_temp1)
print(new_temp)
