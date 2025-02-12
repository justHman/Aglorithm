class Phone:
    def __init__(self, n, b, p):
        self.name = n
        self.brand = b
        self.price = p

    def show_Phone(self):
        print(self.name, ", ", self.brand, ", ", self.price)


class Node:
    def __init__(self, elem, next_node):
        self.elem = elem  # elem la mot bien co kieu la Phone
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def addFirst(self, n, b, p):
        self.head = Node(Phone(n, b, p), self.head)
        self.size = self.size + 1

    def rc_f1(self, node):
        if node is None:
            return 
        node.elem.show_Phone()
        self.rc_f1(node.next)
            
    def f1(self):
        self.rc_f1(self.head)

    def f2(self):
        def rc_f2(node, arr):
            if node is None:
                return
            arr.append(node)
            rc_f2(node.next, arr)

        a = []
        rc_f2(self.head, a)
        print(a)
        for i in a[::-1]:
            i.elem.show_Phone()
    
    def rc_f3(self, node):
            if node is None:
                return 0
            return node.elem.price + self.rc_f3(node.next)
            
            
    def f3(self):
        rs = self.rc_f3(self.head)
        print(rs)

    


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
        lst.f3()
    