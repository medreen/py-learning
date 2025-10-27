trainees = ["John", [2, ["James","Mary"]]]

#display 2
x = trainees[1][0]
print(x)

#output James
james = trainees[1][1][0]
print(james)

#add 56
trainees.append(56)
print(trainees)

#add mike
trainees[1][1].insert(1, 'Mike')
print(trainees)

#2 - 8
trainees[1].pop(0)
trainees[1].insert(0, 8)
print(trainees)

#remove john and mary
trainees.remove('John')
trainees[0][1].remove('Mary')
print(trainees)

#length of list
print(len(trainees))
print(trainees.count("e"))


