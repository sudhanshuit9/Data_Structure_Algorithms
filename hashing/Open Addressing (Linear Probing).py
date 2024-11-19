#Open Addressing is a collision resolution technique where, upon a collision, we probe (search) for the next available slot. 
class OpenAddressingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * self.size

    def hash_function(self, key):
        return hash(key) % self.size

    def linear_probe(self, key):
        index = self.hash_function(key)
        original_index = index

        # Probe until we find an empty slot or the key
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return index  # Key found
            index = (index + 1) % self.size
            if index == original_index:
                return None  # Table is full
        return index  # Found an empty slot

    def insert(self, key, value):
        index = self.linear_probe(key)
        if index is not None:
            self.table[index] = (key, value)
        else:
            print("Table is full")

    def get(self, key):
        index = self.linear_probe(key)
        if index is not None:
            return self.table[index][1]
        return None

    def delete(self, key):
        index = self.linear_probe(key)
        if index is not None:
            self.table[index] = None

# Example
hash_table = OpenAddressingHashTable()
hash_table.insert("apple", 10)
hash_table.insert("banana", 20)
print("Value for 'apple':", hash_table.get("apple"))
hash_table.delete("apple")
print("Value for 'apple' after deletion:", hash_table.get("apple"))
