class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                print(f"Updated key {key} with new value {value}")
                return
        self.table[idx].append((key, value))
        print(f"Inserted key {key} with value {value} at index {idx}")

    def search(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                print(f"Found value {v} for key {key}")
                return v
        print(f"Key {key} not found")
        return None

    def delete(self, key):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx].pop(i)
                print(f"Deleted key {key}")
                return True
        print(f"Key {key} not found for deletion")
        return False

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"Index {i}: {chain}")


# Example usage
if __name__ == "__main__":
    ht = HashTable()
    ht.insert(10, "A")
    ht.insert(20, "B")
    ht.insert(15, "C")
    ht.insert(25, "D")  # Collision with 15 if size=10

    ht.display()
    ht.search(15)
    ht.search(99)
    ht.delete(20)
    ht.display()
