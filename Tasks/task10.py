prods = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'], ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]
i = 0
total_stock = 0

while i < len(prods):    
    total_stock += float(prods[i][2])    
    i = i + 1
print(total_stock)