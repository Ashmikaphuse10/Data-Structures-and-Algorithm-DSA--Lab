def heapify(arr, n, root, heap_type):
    selected = root
    left = 2 * root + 1
    right = 2 * root + 2

    if left < n:
        if heap_type == "max" and arr[left] > arr[selected]:
            selected = left

        if heap_type == "min" and arr[left] < arr[selected]:
            selected = left

    if right < n:
        if heap_type == "max" and arr[right] > arr[selected]:
            selected = right

        if heap_type == "min" and arr[right] < arr[selected]:
            selected = right

    if selected != root:
        arr[root], arr[selected] = arr[selected], arr[root]
        heapify(arr, n, selected, heap_type)


def heap_sort(numbers, heap_type):
    arr = numbers.copy()
    n = len(arr)

    # Build heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, heap_type)

    # Sorting
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0, heap_type)

    return arr


n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    x = int(input("Enter element: "))
    numbers.append(x)

print("\n1. Min Heap - Descending Order")
print("2. Max Heap - Ascending Order")

choice = int(input("Enter your choice: "))

print("\nOriginal list:", numbers)

if choice == 1:
    result = heap_sort(numbers, "min")
    print("Sorted list (Descending using Min Heap):", result)

elif choice == 2:
    result = heap_sort(numbers, "max")
    print("Sorted list (Ascending using Max Heap):", result)

else:
    print("Invalid choice")