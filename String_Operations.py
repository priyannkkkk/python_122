# String Operations

# Define a string for demonstration
text = "Hello, World!"

# Slicing the string with various indices
substring1 = text[0:5]       # Positive index slicing (start to 5)
substring2 = text[-6:]       # Negative index slicing (last 6 characters)
substring3 = text[7:100]     # End index greater than string length
substring4 = text[:]         # Entire string

print("Substring 1 (0:5):", substring1)
print("Substring 2 (-6:):", substring2)
print("Substring 3 (7:100):", substring3)
print("Substring 4 (:):", substring4)

# Splitting string into chunks of length 3 using list comprehension
chunks = [text[i:i+3] for i in range(0, len(text), 3)]
print("Chunks of length 3:", chunks)

# Splitting the string with a specific character
split_string = text.split(',')
print("Split string by ',':", split_string)

# Iterate over the words in the string
for word in text.split():
    print("Word:", word)

# Applying various string methods
trimmed_text = text.strip()          # Trim whitespace
upper_text = text.upper()            # Convert to uppercase
lower_text = text.lower()            # Convert to lowercase
replaced_text = text.replace("World", "Python")  # Replace substring
title_text = text.title()            # Convert to title case
joined_text = '-'.join(text)         # Join string with '-'

print("Trimmed Text:", trimmed_text)
print("Uppercase Text:", upper_text)
print("Lowercase Text:", lower_text)
print("Replaced Text:", replaced_text)
print("Title Case Text:", title_text)
print("Joined Text:", joined_text)

# Set Operations

# Define two sets for demonstration
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Add an element to set_a
set_a.add(6)
print("After adding 6 to set_a:", set_a)

# Union of two sets
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)

# Intersection of two sets
intersection_set = set_a.intersection(set_b)
print("Intersection of set_a and set_b:", intersection_set)

# Difference of two sets
difference_set = set_a.difference(set_b)
print("Difference of set_a and set_b:", difference_set)

# Symmetric Difference of two sets
symmetric_diff_set = set_a.symmetric_difference(set_b)
print("Symmetric Difference of set_a and set_b:", symmetric_diff_set)

# Update set_a with the intersection of set_a and set_b
set_a.intersection_update(set_b)
print("After intersection_update on set_a with set_b:", set_a)

# Update set_b with the symmetric difference of set_a and set_b
set_b.symmetric_difference_update(set_a)
print("After symmetric_difference_update on set_b with set_a:", set_b)

# Difference update on set_b with set_a
set_b.difference_update(set_a)
print("After difference_update on set_b with set_a:", set_b)

# Discard an element from set_a
set_a.discard(4)
print("After discarding 4 from set_a:", set_a)

# Remove an element from set_a
set_a.remove(5)
print("After removing 5 from set_a:", set_a)

# Check if set_a is a subset of set_b
is_subset = set_a.issubset(set_b)
print("Is set_a a subset of set_b?", is_subset)

# Check if set_b is a superset of set_a
is_superset = set_b.issuperset(set_a)
print("Is set_b a superset of set_a?", is_superset)

# Check if set_a and set_b are disjoint sets
is_disjoint = set_a.isdisjoint(set_b)
print("Are set_a and set_b disjoint?", is_disjoint)

# Pop an element from set_a
popped_element = set_a.pop()
print("Popped element from set_a:", popped_element)

# Clear all elements from set_a
set_a.clear()
print("After clearing set_a:", set_a)

# Array Operations

import array as arr

# Create an array of integers
array_int = arr.array('i', [1, 2, 3, 4, 5])

# Append an element to the array
array_int.append(6)
print("Array after appending 6:", array_int)

# Insert an element at a specific position
array_int.insert(2, 10)
print("Array after inserting 10 at index 2:", array_int)

# Remove an element from the array
array_int.remove(3)
print("Array after removing element 3:", array_int)

# Pop an element from the array
popped_value = array_int.pop()
print("Popped value from array:", popped_value)
print("Array after pop:", array_int)

# Extend the array by appending elements from another array
array_int.extend([7, 8, 9])
print("Array after extending:", array_int)

# Reverse the array
array_int.reverse()
print("Array after reversing:", array_int)

# Get the index of an element in the array
index_of_10 = array_int.index(10)
print("Index of element 10:", index_of_10)

# Count the occurrences of an element in the array
count_of_7 = array_int.count(7)
print("Count of element 7:", count_of_7)

# Convert array to a list
array_as_list = array_int.tolist()
print("Array as list:", array_as_list)