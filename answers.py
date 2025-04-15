# Create an empty list
my_list = []

# Appending elements 10,20,30 and 40 to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# This part of code inserts 15 at the second position (index 1)
my_list.insert(1, 15)

# This section extends the list with another list
my_list.extend([50, 60, 70])

# This part of code removes the last element
my_list.pop()

# This section sorts the list in ascending order
my_list.sort()

# This section of code finds and prints the index of the value 30
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)
