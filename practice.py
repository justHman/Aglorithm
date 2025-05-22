def merge_sort(arr):
    print(arr)
    n = len(arr)
    if n <= 1:
        return arr
    mid = n // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    merge = []
    i = j = 0
    while i < len(left) and j < len(right):
        merge.append(left[i]) if left[i] < right[j] else merge.append(right[j])
        if left[i] < right[j]: i += 1
        else: j += 1
    merge.extend(left[i:])
    merge.extend(right[j:])
    return merge 

arr = [9, 8, 7, 6, 5, 4]
rs = merge_sort(arr)
print(rs)