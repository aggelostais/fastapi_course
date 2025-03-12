"""
Sets are similar to lists but are unordered and cannot contain duplications
Use curly brackets
"""

my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set) # Automatically removes duplicates
print(len(my_set))


for x in my_set:
    print(x)


my_set.discard(3)
print(my_set)
my_set.add(6)
print(my_set)
my_set.update([7, 8])
print(my_set)


""""
Tuples are similar to lists but are immutable
Use round brackets
"""

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1]) # Indexing starts at 0
my_tuple[1] = 100 # Tuples are immutable so they don't support item assignment
print(my_tuple[1:3]) # Slicing
print(len(my_tuple))
print(my_tuple.count(1)) # Count the number of times an item appears in a tuple
print(my_tuple.index(3)) # Find the index of an item in a tuple
























