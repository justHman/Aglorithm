def s(a, t):
    l,r = 0, len(a) - 1
    while l <= r:
        m = (l+r) // 2
        if t == a[m]:
            return m
        elif t < a[m]:
            r = m - 1
        else:
            l = m + 1
    return -1

a = [1, 2, 6, 9]
for t in [0, 1, 2, 5, 8, 9, 10]:
    print(s(a,t))