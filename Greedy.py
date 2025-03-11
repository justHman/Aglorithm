def greedy(items, capacity):
    total = 0
    items.sort(key=lambda x: x[1], reverse=True)
    print(items)
    
    
    for weight, value in items:
        if capacity >= weight:
            total += value
            capacity -= weight
        else:
            total += value * (capacity / weight)
            break
    return total
    


# Danh sách vật phẩm (weight, value)
items = [(10, 60), (20, 100), (30, 120)]
capacity = 50
print(greedy(items, capacity))

