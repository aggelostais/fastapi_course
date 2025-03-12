"""
Dictionaries
"""


user_dictionary = {
    'username': 'codingwithroby',
    'name': 'Eric',
    'age': 32
}


user_dictionary2 = user_dictionary.copy()
user_dictionary2.pop("age") # removes the key value pair from the dictionary, with the key of "age"
user_dictionary2.clear() # removes all key value pairs from the dictionary
del user_dictionary2 # deletes the dictionary
print(user_dictionary2)






















