# collect lists from user
list_1 = input("Enter items separated by a comma: ")
list_2 = input("Enter items separated by a comma: ")

set_1 = set(list_1.split(","))
set_2 = set(list_2.split(","))

combine_set = set_1.union(set_2)

sorted_tuple = tuple(combine_set)

print(f"Dad, this is the list:")

for idx, item in enumerate(sorted_tuple):
    print(idx, item)