name = "JOhn"
new_name = name.lower()
print(new_name)

sentence_one = "The Dog Breed is German Shepherd" #only display 'Breed is German'
new_sentence_one = sentence_one[8:-9]
print(new_sentence_one)

sentence_two = 'Defeats for the Clinton forces, this was her moment of triumph' #display 'Clinton forces'
print(sentence_two.find(","))
print(sentence_two[16:30])

sentence_three = 'The lazy dog; ran so fast; it hit the wall.'
split_snt = sentence_three.split(";")
print(split_snt) #returns a list of strings
print(len(split_snt))

first_name = 'Joh.n'
last_name = 'Do,e'

clean_first_name = first_name.replace(".", '')
clean_last_name = last_name.replace(',', '')
print(clean_first_name, clean_last_name)

arr = ['E', 'W', 'C'] #display EWC
new_r = ''.join(arr)
print(new_r)