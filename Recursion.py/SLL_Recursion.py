class Phone:
    def __init__(self, n, b, p):
        self.name = n
        self.brand = b
        self.price = p

    def show_Phone(self):
        print(self.name, ", ", self.brand, ", ", self.price)

class Node:
    def __init__(self, elem, next_node = None):
        self.elem = elem  # elem la mot bien co kieu la Phone
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addFirst(self, n, b, p):
        self.head = Node(Phone(n, b, p), self.head)
        self.size = self.size + 1
            
    def f1(self):
        def rc_f1(node):
            if node is None:
                return 
            node.elem.show_Phone()
            rc_f1(node.next)
        return rc_f1(self.head)

    def f2(self):
        def rc_f2(node):
            if node is None:
                return 
            rc_f2(node.next)
            node.elem.show_Phone()
        return rc_f2(self.head)
             
    def f3(self):
        def rc_f3(node):
            if node is None:
                return 0
            return node.elem.price + rc_f3(node.next)
        rs = rc_f3(self.head)
        return rs

    # find max price by recursion
    def find_max_price(self):
        def rc(node):
            if node is None:
                return 0
            
        return rc(self.head)
    
    def add_last(self, new_node):
        def rc(node):
            if node.next is None:
                node.next = new_node
                return
            rc(node.next)
        rc(self.head)
    
    # find min price by recursion
    def find_min_price(self):
        def rc(node):
            if node is None:
                return node.elem
            return min(node.elem, rc(node.next), key=lambda x: x.price if x.brand == "IPhone" else float('inf')) 
        return rc(self.head)
    
if __name__ == '__main__':
    lst = LinkedList()

    lst.addFirst("Galaxy J10", "Samsung", 7)
    lst.addFirst("Galaxy s23", "Samsung", 20)
    lst.addFirst("13 Pro Max", "IPhone", 27)
    lst.addFirst("A32", "Oppo", 10)
    lst.addFirst("Bphone", "Bom_Phone", 5)
    lst.addFirst("Prime J7", "Samsung", 4)
    lst.addFirst("13 Pro", "IPhone", 7)
    lst.addFirst("A2", "Oppo", 7)
    lst.addFirst("A20", "Oppo", 15)
    print("List da khoi tao xong\n")
    print("Ban muon lam gi?\n")
    print("1. show list tu dau toi cuoi\n")
    print("2. show list tu cuoi ve dau\n")
    print("3. tinh tong cua Price trong list\n")
    print(".... \n")

    print("Default: thoat chuong trinh\n")
    choice = input()
    choice = int(choice)
    r = "khong lam gi ca"
    if (choice == 1):
        lst.f1()
    if (choice == 2):
        lst.f2()
    if (choice == 3):
        rs = lst.f3()
        print(rs)
    if (choice == 4):
        rs = lst.find_max_price()
        print(rs)
    if (choice == 5):
        new_node = Node(Phone("Xiaomi s23", "Samsung", 20))
        lst.add_last(new_node)
        lst.f1()
    if (choice == 6):
        rs = lst.find_min_price()
        rs.show_Phone()
    
    