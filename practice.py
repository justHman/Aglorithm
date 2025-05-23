def s(a, t):
    l,r=0, len(a) - 1
    while l <= r:
        m = (r+l)//2
        if t == a[m]:
            return m
        elif t<a[m]:
            r = m - 1
        else:
            l = m +1
    return -1

a = [1,3,5,7,9]
rs = s(a, 1)
print(rs)