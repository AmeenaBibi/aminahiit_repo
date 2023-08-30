# covert a tuple to a list
atuple = ('here', 'there', 'inside', 'outside', 32, 56)
x = list(atuple)
atuple = tuple(x)
print(x)

# set
items = {'me', 'you', 'him', 'her', 576, 23.76, False}
items.add(100.0)
items.update(['it', 'go'])
print(items)

# dictionary
designer = {
    'Brand' : 'Chanel',
    'Type' : 'Bag',
    'Price' : 60000
    }
designer.update({'Season' : 2015})
designer['Demand'] = 'High' # add
designer['Brand'] = 'LV' # change
print(designer)
