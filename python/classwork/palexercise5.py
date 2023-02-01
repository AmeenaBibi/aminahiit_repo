# python program that prints the first two characters
# last two characters and middle characters
# using list slicing


msg = "Enzo Fernandez"
print("First 2 characters:", msg[0:2])
print("Last 2 characters:", msg[12:])
mid = len(msg)//2
print("MIddle characters:", msg[mid:mid+2])
