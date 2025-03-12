from collections.abc import Iterable

def is_iterable(obj):
    return isinstance(obj, Iterable)

class sort_aglorithms:
    def __init__(self, iter=None):
        self.iter = iter
    
    def check_sorted(self):
        n = len(self.iter)
        mid = int(n/2)
        start = 0
        for i in range(mid):
            print(self.iter)
            if self.iter[start + i] > self.iter[start + i + 1]:
                return False
            if self.iter[mid + i] > self.iter[mid + i + 1]:
                return False
        return True
    
    def bubble(self):
        iter = self.iter
        
        if is_iterable(iter) == False:
            print("Khong phai la iter")
            return iter
        
        n = len(iter)
        for truoc in range(n):
            finish = True
            for lien_sau in range(n - 1 - truoc):  
                if iter[lien_sau] > iter[lien_sau + 1]:
                    iter[lien_sau + 1], iter[lien_sau] = iter[lien_sau], iter[lien_sau + 1]          
                    finish = False
                    
            if finish:
                return iter
        return iter
    
    def selection(self):
        iter = self.iter
        
        if is_iterable(iter) == False:
            print("Khong phai la iter")
            return iter
        
        n = len(self.iter)
        for i in range(n):
            min = float('inf')
            for j in range(i, n - 1):
                if iter[i] < iter[i + 1]:
                    min = iter[i]
            iter[i], min = min, iter[i]
        return iter
            
            

a = [5, 3, 8, 4, 2]
b = [1, 11, 3, 4, 5, 6, 7, 8, 9]
agl = sort_aglorithms(a)
a_sorted = agl.selection()         
print(a_sorted)
