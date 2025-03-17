class Drink:
    def __init__(self, code, producer, unit, volume, price):
        self.code = code
        self.producer = producer
        self.unit = unit
        self.volume = volume
        self.price = price
    
    def __repr__(self):
        return f"{self.code}, {self.producer}, {self.unit}, {self.volume}, {'%.3f' % self.price}"

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addLast(self, code, producer, unit, volume, price):
        new_node = Node(Drink(code, producer, unit, volume, price))
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    

    def display(self):
        current = self.head
        while current:
            print(current.data, end = ' ')
            current = current.next
            print()

    def loadData(self):
        self.addLast('PS021', 'Pepsi', 'Carton of 24 bottles', '390ml', 175.0)
        self.addLast('MD033', 'Mirinda', 'Carton of 24 cans', '320ml', 168.0)
        self.addLast('SP005', 'Schweppes', 'Carton of 24 cans', '320ml', 220.0)
        self.addLast('2C017', 'Coca-Cola', 'Carton of 24 bottles', '600ml', 218.0)
        self.addLast('MD020', 'Mirinda', 'Carton of 24 bottles', '390ml', 175.0)
    
    # This function is used for Question 1
    def f1(self):
        new_node = Node(Drink(code = 'NEWNODE', producer = '7-Up', unit = 'Carton of 24 cans', 
            volume = '320ml', price = 169.0))
        new_node.next = self.head
        self.head = new_node
                        
        """
            Question 1: Insert at the beginning of the current list a new Drink 
            which code = NEWNODE, producer = '7-Up', unit = 'Carton of 24 cans', 
            volume = '320ml', price = 169.0 
            
            With the data provided, the output after running this function will be:
                OUTPUT:
                NEWNODE, 7-Up, Carton of 24 cans, 320ml, 169.000   
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000 
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        #new_node=Node(Drink(code = 'NEWNODE', producer = '7-Up', unit = 'Carton of 24 cans', volume = '320ml', price = 169.0))
        #new_node.next=self.head
        #self.head=new_node
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 2
    def f2(self):
        # Initialize a new node that will be used in Question 2
        new_node = Node(Drink('NEWNODE', 'Sprite', 'Carton of 24 bottles', '390ml', 112.0))
        index = 3
        cur = self.head
        for i in range(3):
            if cur:
                cur = cur.next
        if cur:
            new_node.next = cur.next
            cur.next = new_node
        """
            Question 2: Using the new_node initialized above, write your code to insert 
            the new_node after the fourth node (which index is 3) of the current list.
            
            With the data provided, the output after running this function will be:
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                NEWNODE, Sprite, Carton of 24 bottles, 390ml, 112.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        '''current=self.head
        count=0
        while current and count<3:
            current=current.next
            count+=1
        if current is not None:
            new_node.next=current.next
            current.next=new_node'''

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    def find_last(self):
        cur = self.head
        node = Node(None)
        while cur:
            if cur.data.price > 200:
                node = cur
            cur = cur.next
        return  node
    
    # This function is used for Question 3
    def f3(self):
        node = self.find_last()
        node.data.price = 999
        """
            Question 3: Find the last node in the linked list that has Drink's price 
            higher than 200.0, if such a node is found, then set the price of Drink 
            in this node to 999.0. 
            Example: if the linked list before change is  
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
            then the the linked list after change is:  
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 999.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------        
        '''last_node=None
        current=self.head
        while current:
            if current.data.price>200:
                last_node=current
            current=current.next
        if last_node:
            last_node.data.price=999.0'''


        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 4
    def f4(self):
        lst = []
        cur = self.head
        stt = 1
        while cur:
            if stt != 2:
                lst.append(cur)
            stt += 1
            cur = cur.next
        lst.sort(key=lambda x: x.data.price, reverse=True)
        self.head = self.tail = None
        for node in lst:
            data = node.data
            self.addLast(data.code, data.producer, data.unit, data.volume, data.price)
        """
            Question 4: Remove the second node, then sort the linked list in an descending 
            order according to Drink's price. 
            Example: if the linked list before change is  
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
            then the the linked list after change is:  
                OUTPUT:
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
                
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------        
        '''if self.head and self.head.next:
            self.head.next=self.head.next.next
        nodes=[]
        current=self.head
        while current:
            nodes.append(current.data)
            current=current.next
        nodes.sort(key=lambda drink:drink.price, reverse=True)
        self.head=None
        self.tail=None
        for drink in nodes:
            self.addLast(drink.code,drink.producer,drink.unit,drink.volume,drink.price)'''
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

    # This function is used for Question 5
    def f5(self):
        if self.head.data.unit == 'Carton of 24 cans':
            self.head = self.head.next
        else:
            cur = self.head
            while cur and cur.next:
                if cur.next.data.unit == 'Carton of 24 cans':
                    cur.next = cur.next.next
                    break
                cur = cur.next
        """
            Question 5: Delete the first node in the linked list with 
            Drink's unit = 'Carton of 24 cans'.
            Example: if the linked list before change is  
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                MD033, Mirinda, Carton of 24 cans, 320ml, 168.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
            then the the linked list after change is:  
                OUTPUT:
                PS021, Pepsi, Carton of 24 bottles, 390ml, 175.000
                SP005, Schweppes, Carton of 24 cans, 320ml, 220.000
                2C017, Coca-Cola, Carton of 24 bottles, 600ml, 218.000
                MD020, Mirinda, Carton of 24 bottles, 390ml, 175.000
                        
        """
        # ------------------------------------------------------------------------------
        # ------------------------- Start your code here ------------------------------        
        '''if self.head and self.head.data.unit=='Carton of 24 cans':
            self.head=self.head.next
        else:
            current=self.head
            while current and current.next:
                if current.next.data.unit=='Carton of 24 cans':
                    current.next=current.next.next
                    break
                current=current.next'''

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.display()

# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    lst = LinkedList()
    lst.loadData()
    print("Do you want to run Q1?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    print("5. Run f5()")

    n = int(input("Enter a number : "))

    if n == 1:
        print("OUTPUT:")
        lst.f1()

    if n ==2:
        print("OUTPUT:")
        lst.f2()

    if n == 3:
        print("OUTPUT:")
        lst.f3()

    if n == 4:
        print("OUTPUT:")
        lst.f4()

    if n == 5:
        print("OUTPUT:")
        lst.f5()
# End main
# --------------------------------
if __name__ == "__main__":
    main()
# ============================================================
