def to_hop(arr, C = []):
    if len(C) == len(arr):
        print("".join(C))
        return 
    
    for i in arr:
        C.append(i)
        to_hop(arr, C)
        C.pop()

arr = [i for i in input().split(" ")]
to_hop(arr)