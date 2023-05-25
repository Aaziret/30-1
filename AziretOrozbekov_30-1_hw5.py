def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[min_idx] > lst[j]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


lst = [3, 7, 1, 9, 4, 2, 6]
sorted_lst = bubble_sort(lst)  # или selection_sort(lst)
print(sorted_lst)


def binary_search(arr, x):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            end = mid - 1
        else:
            start = mid + 1

    return -1


lst = [1, 2, 3, 4, 5, 6, 7, 8]
elem = 4
result = binary_search(lst, elem)
if result != -1:
    print(f"Элемент {elem} найден в списке на позиции {result}")
else:
    print(f"Элемент {elem} не найден в списке")
