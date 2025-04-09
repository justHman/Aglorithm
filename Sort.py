from collections.abc import Iterable
import time
import random

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
                print(iter) 
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
            finish = True 
            min = i
            for j in range(i + 1 , n):
                print(iter)
                if iter[j] < iter[min]:
                    min = j
                    finish = False 
            iter[i], iter[min] = iter[min], iter[i]

            if finish:
                return iter
        return iter
            
    def insertion(self):
        iter = self.iter
        
        if is_iterable(iter) == False:
            print("Khong phai la iter")
            return iter
        
        n = len(iter)
        for i in range(1, n):
            for j in range(i, 0, -1):
                print(iter)
                if iter[j] < iter[j - 1]:
                    iter[j], iter[j - 1] = iter[j - 1], iter[j]
                else: 
                    break
        return iter


    def quick(self):
        iter = self.iter
        
        if is_iterable(iter) == False:
            print("Khong phai la iter")
            return iter
        
        def partion(arr=None):
            pivot = arr[-1]
            i = -1
            for j in range(len(arr) - 1):
                if arr[j] < pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1], arr[j + 1] = arr[j + 1], arr[i + 1]
            return i + 1

        def rc(arr=None):
            if not arr:
                return []
            if len(arr) <= 1:
                return arr
            p = partion(arr)
            left = rc(arr[:p])
            right = rc(arr[p:])
            return left + [arr[p]] + right
        return rc(self.iter)
    
    def merge(self):
        def sort(left, right):
            arr = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr.append(left[i])
                    i += 1
                else:
                    arr.append(right[j])
                    j += 1
            arr.extend(left[i:])
            arr.extend(right[j:])
            return arr
        
        def rc(arr):
            if not arr:
                return []
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = rc(arr[:mid])
            right = rc(arr[mid:])
            return sort(left, right)
        return rc(self.iter)

    def heap(self):
        pass

a = [5, 5, 8, 4, 2]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = random.sample(range(1000001), 1000000)
d = 11
sort = sort_aglorithms(c)
start = time.time()
arr_sorted = sort.selection()
end = time.time()
print(arr_sorted)
print('Speed:', end - start)
