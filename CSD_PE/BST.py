class Finery:
    def __init__(self, code, make, size, price):
        self.code = code
        self.make = make
        self.size = size
        self.price = price

    def __repr__(self):
        return f"{self.code}, {self.make}, {self.size}, {'%.3f' % self.price}"

class Node:
    def __init__(self, data):
        self.data = data
        self.l = None
        self.r = None

class qNode:    
    def __init__(self,data):
        self.data = data
        self.next = None

class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None
    
    def enQueue(self, data):
        node = qNode(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def deQueue(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data

class BSTree:
    def __init__(self):
        self.root = None

    def clear(self):
        self.root = None
    
    def isEmpty(self):
        return self.root == None
    
    def insert(self, data):
        self.root = BSTree.insertNode(self.root, data)  
    
    def insertNode(node, data):
        if node is None:
            return Node(data)
        if data.code < node.data.code:
            node.l = BSTree.insertNode(node.l, data)
        elif data.code > node.data.code:
            node.r = BSTree.insertNode(node.r, data)
        return node
    
    def visit(self, p):
        if p==None:
            return
        print(f"{p.data}")
    
    def preOrder(self, p):
        if p==None:
            return
        self.visit(p)
        self.preOrder(p.l)
        self.preOrder(p.r)
    
    def preVisit(self):
        self.preOrder(self.root)
        print()
    
    def inOrder(self, p):
        if p==None:
            return
        self.inOrder(p.l)
        self.visit(p)
        self.inOrder(p.r)
    
    def inVisit(self):
        self.inOrder(self.root)
        print()      
    
    def postOrder(self,p):
        if p==None:
            return
        self.postOrder(p.l)
        self.postOrder(p.r)
        self.visit(p)
    
    def postVisit(self):
        self.postOrder(self.root)
        print()
        
    def postOrder2(self,p):
        if p==None:
            return
        self.postOrder2(p.l)
        self.postOrder2(p.r)
        if 39<p.data.size<42:
            self.visit(p)
            
    def postVisit2(self):
        self.postOrder2(self.root)
        print()
    
    def breadth_first(self):
        if self.isEmpty():
            return
        mq = MyQueue()
        mq.enQueue(self.root)
        while not mq.isEmpty():
            p = mq.deQueue()
            self.visit(p)
            if p.l!=None:
                mq.enQueue(p.l)
            if p.r!=None:
                mq.enQueue(p.r)
        return mq
    
    def height(self,node):
        if node is None:
            return -1
        return max(self.height(node.l),self.height(node.r))+1
    def deleteLeaf(self,node):
        if node is None:
            return None
        if node.l is None and node.r is None:
            return None
        node.l=self.deleteLeaf(node.l)
        node.r=self.deleteLeaf(node.r)
        return node

    def my_height(self, node):
        def rc(node):
            if node is None:
                return -1
            return 1 + max(rc(node.l), rc(node.r))
        return rc(node)
    # This function is used for Question 1
    def f1(self):
        if self.isEmpty():
            print(0)
            return 
        print(self.my_height(self.root))
        """
            Question 1: Find the Height of given Binary Search Tree (BST). 
            Hint: 
                (1) Implement a function to calculate the height of the tree. 
                    Note: The height of an empty tree is 0 
                    and the height of a tree with single node is 0.
                (2) Recursively calculate the height of the l and the r subtrees 
                    of a node and assign height to the node as max of the heights of two 
                    children plus 1.
            With the data provided, the output after running this function will be:
                OUTPUT:
                2
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------       
        
        print(self.height(self.root))

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    
    # This function is used for Question 2
    def f2(self):
        def rc(node):
            if node is None:
                return 
            rc(node.l)
            rc(node.r)
            if node.data.size > 39 and node.data.size < 42:
                print(node.data)
        return rc(self.root.r) if self.root else None 
        """
            Question 2: Perform the Post-Order traverse on the r branch of the BST, 
            but ONLY visit nodes that has Finery's size lager than 39 and less than 42.
            Hint: 
                (1) You should create 2 new functions 'postVisit2' and 'postOrder2' 
                    with similar content to the two functions "postVisit" and "postOrder" 
                    (available in this file) but only consider the 'size' as in the requirement.
                (2) Call the 'postVisit2' function in the f2() to perform them.
            With the data provided, the output after running these two functions will 
            be:
                OUTPUT:
                SK-SUR263P1, Seiko, 41, 3.555
        """  
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------      
        if self.root and self.root.r:  # Chỉ duyệt nhánh phải
            self.postOrder2(self.root.r)
            print()

        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    def my_insert(self, data):
        def rc(node):
            if node is None:
                node = data
            elif data.data.code < node.data.code:
               node.l = rc(node.l)
            else:
                node.r = rc(node.r)
            return node
        self.root = rc(self.root)
    
    # This function is used for Question 3
    def f3(self):
        k = self.my_height(self.root)
        nNode = Node(Finery(code = 'NEWNODE', make = 'Orient', size = 10*k*k, price = k+3))
        self.my_insert(nNode)
        """
            Question 3: Insert into the current tree a new Finery which code = 'NEWNODE', 
            make = 'Orient', size = 10*k*k, price = k+3, where k is height of the 
            current tree before insertion. 
            Hint:  
                Call the 'insert' function (available in this file) in the f3() to 
                insert the new_Finery with the suitable information. 
       
            With the data provided, the output after running this function will be:
                OUTPUT:
                OR-FUNG8003D0, Orient, 40, 3.762
                CT-BM7466-81H, Citizen, 40, 7.590
                CT-CA7060-88L, Citizen, 42, 8.540
                NEWNODE, Orient, 40, 5.000
                SK-SUR263P1, Seiko, 41, 3.555
                SK-SUR211P1, Seiko, 42, 3.690
      
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        '''k=float(self.height(self.root))
        self.insert(Finery(code = 'NEWNODE', make = 'Orient', size = 10*k*k, price = k+3))'''
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.preVisit()

    # This function is used for Question 4
    def f4(self):
        def rc(node):
            if node is None:
                return
            if node.data.make == "Citizen":
                node.data.price *= 1.2
            rc(node.l)
            rc(node.r)
        rc(self.root)
    
        """
            Question 4: Increase the Citizen Finery's price by 20 percents.
            
            With the data provided, the output after running this function will be:
                OUTPUT:
                OR-FUNG8003D0, Orient, 40, 3.762
                CT-BM7466-81H, Citizen, 40, 9.108
                SK-SUR263P1, Seiko, 41, 3.555
                CT-CA7060-88L, Citizen, 42, 10.248
                SK-SUR211P1, Seiko, 42, 3.690

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        '''def increase_price(node):
            if node is None:
                return
            if node.data.make=='Citizen':
                node.data.price*=1.2
            increase_price(node.l)
            increase_price(node.r)
        increase_price(self.root)'''

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.breadth_first()

    # this function is used for Question 5
    def f5(self):
        def rc(node):
            if node is None:
                return
            if not node.l and not node.r:
                return
            node.l = rc(node.l)
            node.r = rc(node.r)
            return node
        rc(self.root.l)
        """
            Question 5: Remove all leaf nodes for the l branch of the given BST.
            
            With the data provided, the output after running this function will be:
                OUTPUT:
                OR-FUNG8003D0, Orient, 40, 3.762
                CT-BM7466-81H, Citizen, 40, 7.590
                SK-SUR263P1, Seiko, 41, 3.555
                SK-SUR211P1, Seiko, 42, 3.690

        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        '''if self.root and self.root.l:
            self.deleteLeaf(self.root.l)
            print()'''
        


        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.breadth_first()
        
# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    tree = BSTree()
    tree.insert(Finery('OR-FUNG8003D0', 'Orient', 40, 3.762))
    tree.insert(Finery('SK-SUR263P1', 'Seiko', 41, 3.555))
    tree.insert(Finery('CT-BM7466-81H', 'Citizen', 40, 7.590))
    tree.insert(Finery('CT-CA7060-88L', 'Citizen', 42, 8.540))
    tree.insert(Finery('SK-SUR211P1', 'Seiko', 42, 3.690)) 
    
    print("Do you want to run Q2?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    print("5. Run f5()")

    n = int(input("Enter a number : "))

    if n == 1: 
        print("OUTPUT:")      
        tree.f1()

    if n ==2:
        print("OUTPUT:")
        tree.f2()

    if n == 3:
        print("OUTPUT:")
        tree.f3()

    if n == 4:
        print("OUTPUT:")
        tree.f4()

    if n == 5:
        print("OUTPUT:")
        tree.f5()       
# end main
# --------------------------------
if __name__ == "__main__":
    main()
# ============================================================
