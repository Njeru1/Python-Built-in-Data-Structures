# Create an Empty List
my_list = []

# Append the values to the List
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

print(my_list)

# Second Position insert No. 15
my_list.insert(1, 15)

print(my_list)

# Extend the list
my_list.extend([50, 60, 70])
print(my_list)

# Remove the lst elelment
my_list.remove(70)
print(my_list)  

# Sort the list in an ascending order
my_list.sort()
print(my_list)

# Print index of the value 30
index_of_30 = my_list.index(30)
print(index_of_30)