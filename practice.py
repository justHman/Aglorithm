import random

# def merge_sort(arr):
#     print(arr)
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr)//2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#     rs = []
#     i, j = 0, 0
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             rs.append(left[i])
#             i += 1
#         else:
#             rs.append(right[j])
#             j += 1
#     rs.extend(left[i:])
#     rs.extend(right[j:])
#     return rs

def insertion_check(arr):
    swapped = False
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            swapped = True
            break
    return swapped

def merge_sort(arr):
    print(arr)
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        result.append(left[i] if left[i] <= right[j] else right[j])
        if left[i] <= right[j]: i += 1
        else: j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def smart_sort(arr):
    if not insertion_check(arr):  # Đã sắp xếp
        return arr
    return merge_sort(arr)        # Cần sắp xếp

arr = [random.randint(1, 1000000) for _ in range(10000)]
rs = merge_sort(arr)
print(rs)