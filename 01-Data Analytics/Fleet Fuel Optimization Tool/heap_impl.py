#--------------------Data Structures And Business Applications------------------------
#------------------------------Semester Project---------------------------------------
#BSBA-5B
#Rayyan Asim(23i-5002),Sohaib Safdar(23i-5030)
#Topic 25: Fleet Fuel Optimization

# heap_impl.py
from typing import List, Callable, Any

def parent(i: int) -> int:
    return (i - 1) // 2

def left(i: int) -> int:
    return 2 * i + 1

def right(i: int) -> int:
    return 2 * i + 2

def heapify_down(heap: List[Any], idx: int, size: int, key: Callable[[Any], float]) -> None:
    while True:
        l = left(idx)
        r = right(idx)
        largest = idx
        if l < size and key(heap[l]) > key(heap[largest]):
            largest = l
        if r < size and key(heap[r]) > key(heap[largest]):
            largest = r
        if largest != idx:
            heap[idx], heap[largest] = heap[largest], heap[idx]
            idx = largest
        else:
            break

def heapify_up(heap: List[Any], idx: int, key: Callable[[Any], float]) -> None:
    while idx > 0:
        p = parent(idx)
        if key(heap[idx]) > key(heap[p]):
            heap[idx], heap[p] = heap[p], heap[idx]
            idx = p
        else:
            break

def build_max_heap(arr: List[Any], key: Callable[[Any], float]) -> List[Any]:
    heap = arr[:]  # copy
    n = len(heap)
    start = (n // 2) - 1
    i = start
    while i >= 0:
        heapify_down(heap, i, n, key)
        i -= 1
    return heap

def heap_push(heap: List[Any], item: Any, key: Callable[[Any], float]) -> None:
    heap.append(item)
    heapify_up(heap, len(heap) - 1, key)

def heap_pop(heap: List[Any], key: Callable[[Any], float]) -> Any:
    n = len(heap)
    if n == 0:
        raise IndexError("pop from empty heap")
    top = heap[0]
    if n == 1:
        heap.pop()
        return top
    heap[0] = heap[-1]
    heap.pop()
    heapify_down(heap, 0, len(heap), key)
    return top
