l = []
l = list()
l = [1, 2, 3, 4, 5]
l = [[1, 2, 3], [4, 5, 6]]
print(l)


l = [1, 2, 3, 4, 5]
m = [6, 7, 8, 9, 10]
print(l + m)  # concatenation
print(l * 3)  # repetition
print(3 in l)  # membership
print(len(l))  # length


names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George']
print(names[0])      # First element
print(names[-1])     # Last element
print(names[1:3])    # Slicing
names[1] = 'David'   # Modify element
print(names)

print(names[-1:-4:-1])  # Reverse slicing

names.append('Hannah')  # Add element
print(names)

names.insert(2, 'Zoe')  # Insert element at index 2
print(names)

names.remove('Charlie')  # Remove element by value
print(names)

popped_name = names.pop()  # Remove and return last element
print(popped_name)
print(names)

names.extend(['Ian', 'Jack'])  # Extend list with another list
print(names)

names.clear()  # Clear the list
print(names)

names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona', 'George']
index_of_diana = names.index('Diana')  # Find index of element
print(index_of_diana)

count_of_bob = names.count('Bob')  # Count occurrences of element
print(count_of_bob)

names.sort()
names.reverse()  # Sort and reverse the list
print(names)

print(sorted(names))  # Return a sorted copy of the list

a = [3, 1, 4, 1, 5, 9, 2, 6, 5]
b = a # Both a and b refer to the same list object
print(id(a), id(b))  # Print memory addresses
print(a is b)  # Check if both lists are the same object


c = a.copy()  # Create a shallow copy of the list
print(id(a), id(c))  # Print memory addresses

max_value = max(a)  # Find maximum value
min_value = min(a)  # Find minimum value
sum_value = sum(a)  # Calculate sum of elements
print(max_value, min_value, sum_value)

l = [0, 0.0, '', [], (), {}, False, set()]
print(all(l))  # Check if all elements are truthy
print(any(l))  # Check if any element is truthy