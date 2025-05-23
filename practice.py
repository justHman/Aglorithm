def ms(a):
    n = len(a)
    m = n//2
    if n <= 1: return a
    l = ms(a[:m])
    r = ms(a[m:])
    i,j,rs = 0, 0 ,[]
    while i<len(l) and j <len(r):
        if l[i] < r[j]:
            rs.append(l[i])
            i += 1
        else:
            rs.append(r[j])
            j += 1

    rs.extend(l[i:])
    rs.extend(r[j:])
    return rs

a = [9,6,3,2]
rs = ms(a)
print(rs)