#this is a comment
text = ''''This is a multiline string
 It traverses the next line 
 when the sentences used are too long'''
print(text)

first_name = 'Mariah'
second_name = 'The'
last_name = 'Scientist'

print(first_name + " " + second_name + " " + last_name)

#indexing
print(last_name[4])
print(last_name[-2])

#length
print(len(first_name))

#slicing
name = 'jane doe'
txt5 = 'JACK BROWN'
slice_name = name[5:] #without specifying it goes upto the end
print(slice_name)

#uppercase & lowercase
print(name.upper())
print(txt5.lower())

#strip
name = "    Killian    .   "
clean_name = name.strip()
print(clean_name)
print(len(clean_name))
print(name.find("K"))
print(name.count('l'))

print(f'{first_name} {second_name} {last_name} is a student!!')
