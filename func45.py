def reverse_string(string):
    string = list(string)
    string.sort(reverse = True)
    string = ' '.join(string).replace(' ', '')
    string = str(string)
    return (string)

revr = reverse_string('eat')
print(revr)

lst = [1, 2, 3, 4, 5, 6]

def get_even(list1):
    results = []
    for i in list1:        
        if i % 2 == 0:
            return results.append[i]
        else:
            return results.append[i]
        
    return results

evn = get_even(lst)
print(evn)

square = []
def get_squares():
    for j in range(1, 30):
        x = j ** 2
        square.append(x)
    return square

sqr = get_squares()
print(sqr)