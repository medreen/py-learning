my_ds = [23, "Jane", (560), ["Lesson", "Maths", {"currency" : "KES"}], 987, (76,"John")]

#print KES
print(my_ds[3][2]['currency'])

#print 560
print(my_ds[2])

#print Maths
print(my_ds[3][1])

#add a currency key
my_ds[3][2]["amount"] = 90
print(my_ds)

#reverse 987
my_ds[4] = str(my_ds[4])[::-1]
print(my_ds)

#change Jane to John
my_ds[5] = list(my_ds[5])
my_ds[5][1] = 'Jane'
my_ds[5] = tuple(my_ds[5])
print(my_ds)
