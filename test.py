def shortestToChar(s: str, c: str):
        cIndex = [i for i, char in enumerate(s) if char == c]
        rs = []
        for i in range(len(s)):
            shortest = min([abs(i - cI) for cI in cIndex])
            rs.append(shortest)
        print(rs)
        return rs

s = "loveleetcode"
c = "e"
shortestToChar(s, c)
