string = input('Enter a string: ')

def reverse_string(string):    
    return string[:: -1]

revr = reverse_string(string)
print(revr)

lst = [1, 2, 3, 4, 5, 6]

def get_even(lst):
    results = []
    for i in lst:        
        if i % 2 == 0:
         results.append(i)   

    return results

evn = get_even(lst)
print(evn)

square = []
def get_squares():
    for j in range(1, 31):
        x = j ** 2
        square.append(x)
    return square

sqr = get_squares()
print(sqr)