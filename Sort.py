from collections.abc import Iterable

def is_iterable(obj):
    return isinstance(obj, Iterable)

class sort_aglorithms:
    def __init__(self, iter=None):
        self.iter = iter
        
    def bubble(self):
        iter = self.iter
        
        if is_iterable(iter) == False:
            print("Khong phai la iter")
            return 
        
        n = len(self.iter)
        for truoc in range(n):
            for lien_sau in range(n - 1):
                if iter[lien_sau] > iter[lien_sau + 1]:
                     iter[lien_sau + 1], iter[lien_sau] = iter[lien_sau], iter[lien_sau + 1]
            n -= 1
        return iter
    
    def selection(self):
        iter = self.iter
        
        if is_iterable(iter) == False:
            print("Khong phai la iter")
            return 
        
        n = len(self.iter)
        

a = [5, 3, 8, 4, 2]
agl = sort_aglorithms(a)
a_sorted = agl.bubble()           
print(a_sorted)
