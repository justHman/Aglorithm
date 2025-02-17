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
            print(node.k, end=' ')
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
                return  rc(node.l)
            if k > node.k:
                return  rc(node.r)
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
                return  rc(node.l)
            if k > node.k:
                return rc(node.r)
        return rc(self.root)
    
    def calHeight(self):
        def rc(node):
            if node is None:
                return -1
            return 1 + max(rc(node.l), rc(node.r))
        return rc(self.root)
    
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
        pass

    # ======================================================
    # Some extensions for AVL Trees
    def calBalanceFactor(self, n):
        pass

    def sleftRotate(self, n):
        # single left rotation
        pass

    def srightRotate(self, n):
        # single right rotation
        pass

    def dleftRotate(self, n):
        # double left rotation
        pass

    def drightRotate(self, n):
        # double right rotation
        pass

    def doBalancing(self, n):
        pass
    
    def vd(self):
        s = 0
        print(id(s))
        def vd1():
            nonlocal s
            s += 10
            print(id(s))
        vd1()
        print(s)
            

def processing():
    t = BSTree()
    t.insert(3)
    t.insert(1)
    t.insert(2)
    t.insert(4)
    t.printTree4()
    print()
    a = t.countLeaf()
    print(a)


if __name__ == '__main__':
    processing()
