class Watch:
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
        self.left = None
        self.right = None

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
            node.left = BSTree.insertNode(node.left, data)
        elif data.code > node.data.code:
            node.right = BSTree.insertNode(node.right, data)
        return node
    
    def visit(self, p):
        if p==None:
            return
        print(f"{p.data}")
    
    def preOrder(self, p):
        if p==None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)
    
    def preVisit(self):
        self.preOrder(self.root)
        print()
    
    def inOrder(self, p):
        if p==None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)
    
    def inVisit(self):
        self.inOrder(self.root)
        print()      
    
    def postOrder(self,p):
        if p==None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)
    
    def postVisit(self):
        self.postOrder(self.root)
        print()
    
    def breadth_first(self):
        if self.isEmpty():
            return
        mq = MyQueue()
        mq.enQueue(self.root)
        while not mq.isEmpty():
            p = mq.deQueue()
            self.visit(p)
            if p.left!=None:
                mq.enQueue(p.left)
            if p.right!=None:
                mq.enQueue(p.right)

    # Compute the height of given Binary Search Tree 
    def maxDepth(self,node):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------       
        if node is None:
            return 0
        else:
            ldepth=self.maxDepth(node.left)
            rdepth=self.maxDepth(node.right)
            depth=max(ldepth,rdepth)+1
            return depth
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    
    # Perform the Post-Order traverse on the BST, 
    # but only visit nodes that has Watch's price 
    # in the interval [3,8].
    def postOrder2(self,p):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------       
        if p==None:
            return
        self.postOrder2(p.left)
        self.postOrder2(p.right)
        if 3<p.data.price<8:
            self.visit(p)        

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    
    def postVisit2(self):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------       
        self.postOrder2(self.root)
        print()

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        
    # Decrease the Watch's price of all nodes that 
    # have size = 42 by 1       
    def updateWatch(self):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------       
        if self.isEmpty():
            return
        mq = MyQueue()
        mq.enQueue(self.root)
        while not mq.isEmpty():
            p = mq.deQueue()
            if p.data.size==40:
                p.data.size-=1
                
            if p.left!=None:
                mq.enQueue(p.left)
            if p.right!=None:
                mq.enQueue(p.right)
                
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    
    # Remove all nodes that are leaves of given BST
    def deleteLeaf(self,node):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------       
        if node is None:
            return None
        if node.left is None and node.right is None:
            return None
        node.left=self.deleteLeaf(node.left)
        node.right=self.deleteLeaf(node.right)
        return node
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    def my_height(self, node):
        def rc(node):
            if not node:
                return 0
            return max(rc(node.left), rc(node.right)) + 1
        return rc(node)
    
    # This function is used for Question 1
    def f1(self):
        print(self.my_height(self.root))
        """
            Question 1: Compute the height of given Binary Search Tree . 
            Hint: 
                (1) Implement a 'maxDepth' function to calculate the height of the tree. 
                    Note: The height of an empty tree is 0 and the height of a tree with 
                    single node is 1.
                (2) Recursively calculate the height of the left and the right subtrees 
                    of a node and assign height to the node as max of the heights of two 
                    children plus 1.
            With the data provided, the output after running this function will be:
                OUTPUT:
                3
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------       
        #print(self.maxDepth(self.root))
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    
    # This function is used for Question 2
    def f2(self):
        def rc(node):
            if not node:
                return
            rc(node.left)
            rc(node.right)
            if 3 < node.data.price < 8:
                print(node.data)
        rc(self.root)
        """
            Question 2: Perform the Post-Order traverse on the BST, but ONLY visit nodes 
            that has Watch's price lager than 3 and less than 8.
            Hint: 
                (1) You should create 2 new functions 'postVisit2' and 'postOrder2' 
                    with similar content to the two functions "postVisit" and "postOrder" 
                    (available in this file) to perform the Post-Order traverse but only 
                    consider prices in the interval [3,8].
                (2) Call the 'postVisit2' function in the f2() to perform them.
            With the data provided, the output after running these two functions will 
            be:
                OUTPUT:
                CT-BM7466-81H, Citizen, 40, 7.590
                SK-SUR211P1, Seiko, 42, 3.690
                SK-SUR263P1, Seiko, 41, 3.555
                OR-FUNG8003D0, Orient, 40, 3.762
        """  
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------      
        #self.postVisit2()
        
		
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
    def my_in(self, data):
        def rc(node):
            if not node:
                return data
            elif data.data.code < node.data.code:
                node.left = rc(node.left)
            else:
                node.right = rc(node.right)
            return node
        return rc(self.root)
                        
    # This function is used for Question 3
    def f3(self):
        k = self.my_height(self.root)
        nNode = Node(Watch(code = 
            'OR-FGW01006W0', make = 'Orient', size = 38, price = k))
        self.my_in(nNode)
        """
            Question 3: Insert into the current tree a new Watch which code = 
            'OR-FGW01006W0', make = 'Orient', size = 38, price = k, where k is height 
            of the current tree before insertion. 
            Hint:  
                Call the 'insert' function (available in this file) in the f3() to 
                insert the new_watch with price = float(Tree_Height in Question 1) 
                into the tree.
            With the data provided, the output after running this function will be:
                OUTPUT:
                OR-FUNG8003D0, Orient, 40, 3.762
                CT-BM7466-81H, Citizen, 40, 7.590
                CT-CA7060-88L, Citizen, 42, 8.540
                OR-FGW01006W0, Orient, 38, 3.000
                SK-SUR263P1, Seiko, 41, 3.555
                SK-SUR211P1, Seiko, 42, 3.690      
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        #k=float(self.maxDepth(self.root))
        #self.insert(Watch(code = 'OR-FGW01006W0', make = 'Orient', size = 38, price = k))
		
		
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.preVisit()

    # This function is used for Question 4
    def f4(self):
        def rc(node):
            if not node:
                return
            if node.data.size == 40:
                node.data.price -= 1
            rc(node.left)
            rc(node.right)
        rc(self.root)
        """
            Question 4: Decrease the Watch's price of all nodes that have size = 40 by 1. 
            Hint: 
                (1) You should create a new function 'updateWatch' which body is similar 
                    to the function 'breadth_first' (provided in this file already) for 
                    doing BFS but considering only size = 40.
                (2) Call the 'updateWatch' function in the f4() to perform it (decrease 
                    the Watch's price of all nodes that have size = 40' by 1).
            With the data provided, the output after running this function will be:
                OUTPUT:
                OR-FUNG8003D0, Orient, 40, 2.762
                CT-BM7466-81H, Citizen, 40, 6.590
                SK-SUR263P1, Seiko, 41, 3.555
                CT-CA7060-88L, Citizen, 42, 8.540
                SK-SUR211P1, Seiko, 42, 3.690
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        
        #self.updateWatch()
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.breadth_first()

    # this function is used for Question 5
    def f5(self):
        def rc(node):
            if not node:
                return
            if not node.left and not node.right:
                return 
            node.left = rc(node.left)
            node.right = rc(node.right)
            return node
        rc(self.root)
        """
            Question 5: Remove all leaf nodes from the given Binary Search Tree (BST). 
            Hint: 
                (1) Leaf nodes have neither left child nor right child.
                (2) Implement a 'deleteLeaf' function to remove all leaf nodes 
                    from the given BST.
                (3) Call the 'deleteLeaf' function in the f5() to perform it.
            With the data provided, the output after running this function will be:
                OUTPUT:
                OR-FUNG8003D0, Orient, 40, 3.762
                CT-BM7466-81H, Citizen, 40, 7.590
                SK-SUR263P1, Seiko, 41, 3.555
        """
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        #self.deleteLeaf(self.root)
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.breadth_first()
        
# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    tree = BSTree()
    tree.insert(Watch('OR-FUNG8003D0', 'Orient', 40, 3.762))
    tree.insert(Watch('SK-SUR263P1', 'Seiko', 41, 3.555))
    tree.insert(Watch('CT-BM7466-81H', 'Citizen', 40, 7.590))
    tree.insert(Watch('CT-CA7060-88L', 'Citizen', 42, 8.540))
    tree.insert(Watch('SK-SUR211P1', 'Seiko', 42, 3.690)) 
    
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
