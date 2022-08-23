# SORTING ALGORITHMS

--------------------
## Sorting 
Means rearranging a sequence sequence of objects so as to put them in some logical order


* Buble sort (Sinking sort) - Bubble sort is a sorting algorithm that compares two adjacent elements and swaps them until they are in the intended order.
ar

```python

def sort(arr):
    n = len(arr)-1
    for x in range(n):
        for y in range(n):
            if(arr[y] > arr[y+1]):
                arr[y], arr[y+1] = arr[y+1], arr[y] 
    return arr
```
