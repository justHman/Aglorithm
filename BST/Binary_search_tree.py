class Node:
    def __init__(self, key):
        self.r = None
        self.l = None
        self.k = key


class BSTree:
    def __init__(self):
        self.root = None
    
    def insert_rc(self, new_number):
        new_node = Node(new_number)
        def rc(node):
            if node is None:
                node = new_node
            elif new_number < node.k:
                node.l = rc(node.l)
            elif new_number > node.k:
                node.r = rc(node.r)
            return node
        self.root = rc(self.root)
        
    def insert(self, k):
        new_node = Node(k)
        # Nếu cây rỗng, new_node trở thành gốc
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if k < current.k:
                # Nếu bên trái trống, chèn new_node vào bên trái
                if current.l is None:
                    current.l = new_node
                    break
                else:
                    current = current.l
            else:
                # Nếu bên phải trống, chèn new_node vào bên phải
                if current.r is None:
                    current.r = new_node
                    break
                else:
                    current = current.r
        

    def printTree1(self):
        # preorder
        def rc(node):
            if node is None:
                return
            print(node.k, end=', ')
            rc(node.l)
            rc(node.r)
        rc(self.root)

    def printTree2(self):
        # inorder
        def rc(node):
            if node is None:
                return
            rc(node.l)
            print(node.k, end=' ')
            rc(node.r)
        rc(self.root)

    def printTree3(self):
        # postorder
        def rc(node):
            if node is None:
                return
            rc(node.l)
            rc(node.r)
            print(node.k, end=' ')
        rc(self.root)

    def printTree4(self):
        # breadth first traversal
        stack = [self.root]
        while stack:
            node = stack.pop(0)
            print(node.k, end=' ')
            if node.l is not None:
                stack.append(node.l)
            if node.r is not None:
                stack.append(node.r)

    def search(self, k):
        def rc(node):
            if node is None:
                return 
            if node.k == k:
                return node
            if k < node.k:
                return rc(node.l)
            if k > node.k:
                return rc(node.r)
        return rc(self.root)

    def findFather(self, k):
        def rc(node):
            if node is None:
                return 
            if node.k == k:
                return 
            if node.l is not None and node.l.k == k:
                return node
            if node.r is not None and node.r.k == k:
                return node
            if k < node.k:
                return rc(node.l)
            if k > node.k:
                return rc(node.r)
        return rc(self.root)
    
    def calHeight(self, node):
        def rc(node):
            if node is None:
                return -1
            return 1 + max(rc(node.l), rc(node.r))
        return rc(node)
    
    def calHeight1(self):
        def rc(node):
            if node is None:
                return -1
            l = rc(node.l)
            r = rc(node.r)
            return 1 + max(l, r)
        return rc(self.root)

    def countLeaf(self):
        def rc(node):
            if node is None:
                return 0
            if node.l is None and node.r is None:
                return 1
            return rc(node.l) + rc(node.r)
        return rc(self.root)

    def sum(self):
        s = 0
        def rc(node):
            if node is None:
                return
            nonlocal s
            s += node.k
            rc(node.l)
            rc(node.r)
            
        def rc2(node):
            if node is None:
                return 0
            return node.k + rc2(node.l) + rc2(node.r)
        return rc2(self.root)

    def countNode(self):
        def rc(node):
            if node is None:
                return 0
            return 1 + rc(node.l) + rc(node.r)
        return rc(self.root)

    def delete(self, k):
        def find_min_right_and_parent(node):
            parent = node
            min_right = node.r
            while min_right.l:
                parent = min_right
                min_right = min_right.l
            return min_right, parent

        def rc(node):
            if node is None:
                return 
            if k < node.k:
                node.l = rc(node.l)
            elif k > node.k:
                node.r = rc(node.r)
            else:
                if node.l is None or node.r is None:
                    return node.l if node.r is None else node.r
                if node.l is not None and node.r is not None:
                    min_right, parent = find_min_right_and_parent(node)
                    node.k = min_right.k
                    if parent.k == node.k:
                        parent.r = parent.r.r
                    else:
                        parent.l = parent.l.r
            return node 
        self.root = rc(self.root)

    # ======================================================
    # Some extensions for AVL Trees
    def calBalanceFactor(self, node):
        def rc(node):
            if node is None:
                return 0
            lHeight = self.calHeight(node.l) 
            rHeight = self.calHeight(node.r) 
            return lHeight - rHeight
        return rc(node)

    def sleftRotate(self, node):
        # single left rotation
        if node is None or node.r is None:
            return node 
        
        root = node
        right = node.r

        root.r = right.l
        right.l = root
        return right

    def srightRotate(self, n):
        # single right rotation
        if n is None or n.l is None:
            return n
        
        root = n
        left = n.l

        root.l = left.r
        left.r = root
        return left

    def dleftRotate(self, n):
        # double left rotation
        if n is None or n.l is None:
            return n 
        
        n.l = self.sleftRotate(n.l)
        return self.rightRotate(n)

    def drightRotate(self, n):
        # double right rotation
        if n is None or n.r is None:
            return n 
        
        n.r = self.srightRotate(n.r)
        return self.sleftRotate(n)

    def doBalancing(self, n):
        balance_factor = self.calBalanceFactor(n)
        if balance_factor in [-1, 0 , 1]:
            return n
        if balance_factor > 1: # Lệch trái
            if self.calBalanceFactor(n.l) < 0:
                return self.drightRotate(n)
            return self.srightRotate(n)
        if balance_factor < -1:
            if self.calBalanceFactor(n.r) > 0:
                return self.dleftRotate(n)
            return self.sleftRotate(n)
        
    # def AVLDeleteNode(self, n):
    #     def find_min_right(node):
    #         cur = node.r
    #         while cur:
    #             cur = cur.l
    #         return cur
            
    #     def rc(node, n=n):
    #         if node is None:
    #             return
    #         if n < node.k:
    #             node.l = rc(node.l)
    #         elif n > node.k:  
    #             node.r = rc(node.r)
    #         else:
    #             if node.l is None or node.r is None:
    #                 return node.l if node.r is None else node.r
    #             min_right = find_min_right(node)
    #             node.k = min_right.k
    #         return self.doBalancing(node)
    #     self.root = rc(self.root)

    def AVLDeleteNode(self, key):
        def find_min(node):
            while node.l:
                node = node.l
            return node

        def rc(node, key):
            if node is None:
                return None
            if key < node.k:
                node.l = rc(node.l, key)
            elif key > node.k:
                node.r = rc(node.r, key)
            else:
                if node.l is None:
                    return node.r
                elif node.r is None:
                    return node.l
                min_right = find_min(node.r)
                node.k = min_right.k
                node.r = rc(node.r, min_right.k)
            return self.doBalancing(node)
        self.root = rc(self.root, key)

    def AVLInsertNode(self, k):
        new_node = Node(k)
        def rc(node):
            if node is None:
                return new_node
            if k < node.k:
                node.l = rc(node.l)
            elif k > node.k:
                node.r = rc(node.r)
            return self.doBalancing(node)
        self.root = rc(self.root)
           

def insert():
    tree = BSTree()
    
    nodes = [30, 20, 10, 5, 15, 25, 40, 35, 50]
    for n in nodes:
        tree.AVLInsertNode(n)

    print("Cây trước khi xóa:")
    tree.printTree1()
    
    # Xoá một node có hai con (ví dụ: 20)
    print("\nXóa node 25:")
    tree.AVLDeleteNode(30) 
    
    print("Cây sau khi xóa:")
    tree.printTree1()
    
    


if __name__ == '__main__':
    insert()
