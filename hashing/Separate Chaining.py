#Separate Chaining is another collision resolution technique, where each slot in the hash table is a linked list (or a bucket) that stores all the elements that hash to the same index.
class SeparateChainingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if the key already exists and update its value
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        # If key doesn't exist, append a new pair
        self.table[index].append((key, value))

    def get(self, key):
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                return v
        return None

    def delete(self, key):
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
        print("Key not found")

# Example
hash_table = SeparateChainingHashTable()
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
print("Value for 'apple':", hash_table.get("apple"))
hash_table.delete("apple")
print("Value for 'apple' after deletion:", hash_table.get("apple"))
