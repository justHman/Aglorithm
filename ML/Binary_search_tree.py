class Node:
    def __init__(self, key):
        self.r = None
        self.l = None
        self.k = key


class BSTree:
    def __init__(self):
        self.root = None
    
    def insert(self, new_number):
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
        pass

    def search(self, k):
        def rc(node):
            if node is None:
                return 
            if node.k == k:
                return node
            elif k < node.k:
                return rc(node.l)
            elif k > node.k:
                return rc(node.r)
            
        node = rc(self.root)
        if node:
            return node
        return Node(None)

    def findFather(self, k):
        pass

    def calHeight(self):
        pass

    def countLeaf(self):
        pass

    def sum(self):
        s = 0
        def rc(node):
            if node is None:
                return
            nonlocal s
            s += node.k
            return  
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
            return 1 + + rc(node.l) + rc(node.r)
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
    t.printTree1()
    print()
    a = t.search(5)
    print(a.k)
    t.printTree1()


if __name__ == '__main__':
    processing()
