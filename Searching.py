def linear_search(ids, target):
    for i in range(len(ids)):
        if ids[i] == target:
            return i
    return -1


def binary_search(ids, target):
    low, high = 0, len(ids) - 1
    while low <= high:
        mid = (low + high) // 2
        if ids[mid] == target:
            return mid
        elif ids[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


ids = [101, 105, 110, 115, 120, 125]
print("Customer Account IDs:", ids)

target = 115
r1 = linear_search(ids, target)
r2 = binary_search(ids, target)

print(
    f"\nLinear Search: ID {target} {'found at index ' + str(r1) if r1 != -1 else 'not found'}")
print(
    f"Binary Search: ID {target} {'found at index ' + str(r2) if r2 != -1 else 'not found'}")