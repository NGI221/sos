
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

employee_salaries = [1500.0, 2500.5, 1200.75,
                     3000.0, 1800.25, 2800.0, 3500.0, 2000.0]

salaries_selection_sorted = selection_sort(list(employee_salaries))
print("Salaries sorted with Selection Sort:", salaries_selection_sorted)

salaries_bubble_sorted = bubble_sort(list(employee_salaries))
print("Salaries sorted with Bubble Sort:", salaries_bubble_sorted)

top_five_salaries = sorted(employee_salaries, reverse=True)[:5]
print("Top five highest salaries:", top_five_salaries)
