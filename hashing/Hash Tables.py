#A Hash Table is a data structure that maps keys to values for efficient lookups, insertions, and deletions.
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        self.table[index] = value

    def get(self, key):
        index = self.hash_function(key)
        return self.table[index]

    def delete(self, key):
        index = self.hash_function(key)
        self.table[index] = None

# Example
ht = HashTable()
ht.insert("apple", 10)
ht.insert("banana", 20)
print("Value for 'apple':", ht.get("apple"))
ht.delete("apple")
print("Value for 'apple' after deletion:", ht.get("apple"))
