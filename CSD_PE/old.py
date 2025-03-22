class Room:
    def __init__(self, code=None, status=0,size=0,price=0):
        self.code = code
        self.status = status
        self.size = size
        self.price = price

    def __repr__(self):
        return f"{self.code}, {self.status}, {self.size}, {self.price}"

class Node:
    def __init__(self, value):
        self.info = value
        self.next = None

class dataList: #Singly
    def __init__(self):
        self.head = None
        self.tail = None

    def search_approve(self, t1):
        cur = self.head
        approve = []
        while cur is not None:
            if cur.info.size >= t1.info.size and cur.info.price <= t1.info.price and cur.info.status == 0:
                approve.append(cur)
            cur = cur.next
        return approve
    
    def sort_room(self):
        sorted_room = []
        cur = self.head
        while cur:
            sorted_room.append(cur)
            cur = cur.next
        sorted_room.sort(key=lambda room: room.info.price)
        for room in sorted_room:
            print(room.info)
        return sorted_room
    
    def search(self, rq):
        sorted_room = self.sort_room()
        for room in sorted_room:
            if room.info.price <= rq.info.price and room.info.status == 0 and room.info.size >= rq.info.size:
                return room
        return None 
        '''def key_func(room):
            return room.info.price

        approve = self.search_approve(t1)
        m = None
        if approve:
            m = min(approve, key=key_func)
        return m'''

    def addLast(self, code, status, size, price):
        if size <= 0 or price <= 0:
            return
        nNode = Node(Room(code, status, size, price))
        if not self.head:
            self.head = self.tail = nNode
        else:
            self.tail.next = nNode
            self.tail = nNode
        # ===== Begin your code =====
        '''if size <= 0 or price <= 0:
            return
        new_node = Node(Room(code, status, size, price))
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node'''
        # ===== End your code =====

    def display(self):
        print("Data List:")
        if (self.head is None):
            print("Empty")
        current = self.head
        while current:
            print(current.info)
            current = current.next
        print("=========")

    def loadData(self, l):
        data = ['001', 0, 10, 200,
                '002', 1, 0, 50,
                '003', 0, 3, 70,
                '004', 0, 4, 100,
                '005', 0, 3, 70,
                '101', 1, 5, 120,
                '102', 0, 4, 100,
                '103', 0, 3, 80,
                '104', 0, 3, 70,
                '105', 1, 6, -10]
        for i in range(l):
            self.addLast(data[4*i], data[4*i+1], data[4*i+2], data[4*i+3])

class requestQueue: # Queue
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return True if not self.front else False
    
    def enQueue(self, size, price):
        nNodde = Node(Room(size = size, price=price))
        if size <= 0 or price <= 0:
            return
        if not self.front:
            self.front = self.rear = nNodde
        else:
            self.rear.next = nNodde
            self.rear = nNodde
        # ===== Begin your code =====
        '''if size <= 0 or price <= 0:
            return
        new_node = Node(Room(size=size, price=price))
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node'''
        # ===== End your code =====

    def deQueue(self):
        tmp = None
        # ===== Begin your code =====
        if self.front is None:
            return tmp
        tmp = self.front
        self.front = self.front.next
        # ===== End your code =====
        return tmp

    def display(self):
        print("Request Queue:")
        if (self.front is None):
            print("Empty")
        current = self.front
        while current:
            print(str(current.info.size) + str(", ") + str(current.info.price))
            current = current.next
        print("=========")

    def loadRequest(self, l):
        data = [1, 100,
                0, 500,
                12, 500,
                4, 50,
                4, 400,
                3, 120,
                2, 300,
                5, 90,
                3, 200,
                4, 15]
        for i in range(l):
            self.enQueue(data[2*i], data[2*i+1])

class Hotel: # product
    def __init__(self):
        self.data = dataList()
        self.request = requestQueue()

    def load(self, m, n):
        self.data.loadData(m)
        self.request.loadRequest(n)

    def display(self):
        self.data.display()
        self.request.display()

    def f1(self,m,n):
        self.load(m,n)
        self.display()

    def rent(self, t1):
        p = self.data.head
        # ===== Begin your code =====


        # ===== End your code =====

    def f2(self):
        rq = self.request.deQueue()
        room = self.data.search(rq)
        print('room', room.info if room else room)
        if room:
            room.info.status = 1
        
        # ===== Begin your code =====
        '''a = []
        t1 = self.request.deQueue()
        result = self.data.search(t1)
        if result is None:
            a.append(t1)
        else:
            result.info.status += 1

        for i in a:
            self.request.enQueue(i.info.size, i.info.price)'''
        # ===== End your code =====

    def f3(self):
        while not self.request.is_empty():
            rq = self.request.deQueue()
            room = self.data.search(rq)
            print('room', room.info if room else room)
            if room:
                room.info.status = 1
        # ===== Begin your code =====
        '''t1 = self.request.deQueue()
        while t1 is not None:
            result = self.data.search(t1)
            if result is not None:
                result.info.status += 1
            t1 = self.request.deQueue()'''
        # ===== End your code =====

    def f4(self):
        c = 0
        # ===== Begin your code =====
        self.f3()
        cur = self.data.head
        while cur:
            if cur.info.status == 0:
                c += 1
            cur = cur.next
        # ===== End your code =====
        return c


# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    ds = Hotel()
    m = int(input("Input the number of Room (from 1 to 10):\nm =   "))
    while (m < 1 or m > 10):
        m = int(input("Please input the number of Room (from 1 to 10):\nm =   "))
    n1 = int(input("Input the number of requests in the request_queue (from 1 to 10):\nn =   "))
    while (n1 < 1 or n1 > 10):
        n1 = int(input("Please input the number of requests in the request_queue (from 1 to 10):\nn =   "))

    print("Do you want to run Q1?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    n = int(input("Input a question (1=>4) : "))
    if n == 1:
        print("OUTPUT:")
        ds.f1(m,n1)

    if n == 2:
        ds.load(m,n1)
        print("OUTPUT:")
        print("Before")
        ds.display()
        ds.f2()
        print("After")
        ds.display()

    if n == 3:
        ds.load(m, n1)
        print("OUTPUT:")
        print("Before")
        ds.display()
        ds.f3()
        print("After")
        ds.display()

    if n == 4:
        ds.load(m, n1)
        print("OUTPUT:")
        print("Before")
        ds.display()
        c = ds.f4()
        print("After")
        ds.display()
        print("Available Room(s): " + str(c))



# End main
# --------------------------------
if __name__ == "__main__":
    main()
# ================================