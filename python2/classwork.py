alist = ['mango', 'pear', 56, 'indomie', 567, 1000, 'move', 'come']
# 5th item
print(alist[5])

# from index 3 to end
print(alist[3:])

# from end to index 2
from_end = alist[-1:2:-1]
print(from_end)

# change item 4
alist[4] = 'run'
print(alist)

# append item
alist.append(5)
print(alist)

# extend another list to exixting list
blist = ['apple', 34, 21]
alist.extend(blist)
print(alist)

# remove a list item
alist.remove('indomie')
print(alist)

