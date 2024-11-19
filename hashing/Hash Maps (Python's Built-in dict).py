#In Python, Hash Maps are implemented using the built-in dict, which internally uses a hash table.
# Using Python's built-in Hash Map (dictionary)
hash_map = {}

# Insert key-value pairs
hash_map["apple"] = 10
hash_map["banana"] = 20

print("Value for 'apple':", hash_map["apple"])

# Delete a key-value pair
del hash_map["apple"]
print("After deletion, 'apple' exists:", "apple" in hash_map)
