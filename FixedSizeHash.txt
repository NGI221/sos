
def hash_func(key, size):
    return key % size


def insert(key, table, size):
    i = hash_func(key, size)
    while table[i] not in (None, "DELETED"):
        i = (i + 1) % size
    table[i] = key


def search(key, table, size):
    i = start = hash_func(key, size)
    while table[i] is not None:
        if table[i] == key:
            return i
        i = (i + 1) % size
        if i == start:
            break
    return -1


def delete(key, table, size):
    i = search(key, table, size)
    if i != -1:
        table[i] = "DELETED"


def display(table):
    for i, v in enumerate(table):
        print(f"Index {i}: {v}")


# Example usage
size = 7
table = [None] * size

for k in [10, 20, 5, 15]:
    insert(k, table, size)

print("Hash Table after insertions:")
display(table)

delete(10, table, size)
print("\nHash Table after deleting 10:")
display(table)

key = 15
res = search(key, table, size)
print(f"\nKey {key} {'found at index ' + str(res) if res != -1 else 'not found'}")
