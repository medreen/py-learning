def reverse_string(string):
    string = list(string)
    string.sort(reverse = True)
    string = ' '.join(string).replace(' ', '')
    string = str(string)
    return (string)

revr = reverse_string('eat')
print(revr)

lst = [1, 2, 3, 4, 5, 6]

def get_even(lst):
    for i in lst:        
        if i % 2 == 0:
            return f'{i} is an even number.'
        else:
            return f'{i} is an odd number.'
        

evn = get_even(lst)
print(evn)

square = []
def get_squares():
    for i in range(1, 30):
        x = i ** 2
        square.append(x)
        return square

sqr = get_squares()
print(sqr)