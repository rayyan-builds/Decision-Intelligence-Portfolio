#--------------------Data Structures And Business Applications------------------------
#------------------------------Semester Project---------------------------------------
#BSBA-5B
#Rayyan Asim(23i-5002),Sohaib Safdar(23i-5030)
#Topic 25: Fleet Fuel Optimization

# sorting.py
from typing import List, Callable, Any

def insertion_sort(arr: List[Any], key: Callable[[Any], float]) -> List[Any]:
    a = arr[:]  # copy so caller list not modified
    n = len(a)
    for i in range(1, n):
        current = a[i]
        current_key = key(current)
        j = i - 1
        while j >= 0 and key(a[j]) > current_key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = current
    return a

def merge(left: List[Any], right: List[Any], key: Callable[[Any], float]) -> List[Any]:
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if key(left[i]) <= key(right[j]):
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i]); i += 1
    while j < len(right):
        res.append(right[j]); j += 1
    return res

def merge_sort(arr: List[Any], key: Callable[[Any], float]) -> List[Any]:
    n = len(arr)
    if n <= 1:
        return arr[:]
    if n <= 16:  # small threshold use insertion sort (practical)
        return insertion_sort(arr, key)
    mid = n // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)
    return merge(left, right, key)

def sort_by_key(arr: List[Any], key: Callable[[Any], float], descending: bool = False) -> List[Any]:
    sorted_list = merge_sort(arr, key)
    if not descending:
        return sorted_list
    # manual reverse (avoid built-in reverse)
    out = []
    idx = len(sorted_list) - 1
    while idx >= 0:
        out.append(sorted_list[idx])
        idx -= 1
    return out
