import random
import time
import matplotlib.pyplot as plt



class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1



class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, root, key):
        if not root:
            return AVLNode(key)

        if key < root.key:
            root.left = self._insert(root.left, key)
        else:
            root.right = self._insert(root.right, key)

        root.height = 1 + max(self._get_height(root.left), self._get_height(root.right))

        balance = self._get_balance(root)

        
        if balance > 1 and key < root.left.key:
            return self._right_rotate(root)

    
        if balance < -1 and key > root.right.key:
            return self._left_rotate(root)


        if balance > 1 and key > root.left.key:
            root.left = self._left_rotate(root.left)
            return self._right_rotate(root)


        if balance < -1 and key < root.right.key:
            root.right = self._right_rotate(root.right)
            return self._left_rotate(root)

        return root

    def _left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self._get_height(z.left), self._get_height(z.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    def _get_height(self, root):
        if not root:
            return 0
        return root.height

    def _get_balance(self, root):
        if not root:
            return 0
        return self._get_height(root.left) - self._get_height(root.right)

    def height(self):
        return self._get_height(self.root)



class RedBlackNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'red'  


class RedBlackTree:
    def __init__(self):
        self.TNULL = RedBlackNode(0)
        self.TNULL.color = 'black'
        self.root = self.TNULL

    def insert(self, key):
        node = RedBlackNode(key)
        node.parent = None
        node.key = key
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 'red'

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if node.key < x.key:
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif node.key < y.key:
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 'black'
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def fix_insert(self, k):
        while k.parent.color == 'red':
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right
                if u.color == 'red':
                    u.color = 'black'
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 'black'
                    k.parent.parent.color = 'red'
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 'black'

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node == self.TNULL:
            return 0
        left_height = self._height(node.left)
        right_height = self._height(node.right)
        return max(left_height, right_height) + 1



def test_tree(tree_class, n, runs=10):
    total_height = 0
    total_time = 0

    for _ in range(runs):
        tree = tree_class()
        start_time = time.time()
        for i in range(n):
            tree.insert(random.randint(1, 10000))
        height = tree.height()
        total_height += height
        total_time += (time.time() - start_time)

    avg_height = total_height / runs
    avg_time = total_time / runs
    return avg_height, avg_time



sizes = [1,10,20,30, 40, 50, 90,100,150, 200,250, 300,350, 400,450, 500,550,600,650,700,750, 800,850,900,950,1000, 1024]
bst_heights = []
avl_heights = []
rbt_heights = []

with open("tree_heights.txt", "w") as f:
    f.write("Size,BST Height, AVL Height, Red-Black Tree Height\n")

    for size in sizes:
        bst_height, _ = test_tree(BinarySearchTree, size)
        avl_height, _ = test_tree(AVLTree, size)
        rbt_height, _ = test_tree(RedBlackTree, size)

        avl_heights.append(avl_height)
        rbt_heights.append(rbt_height)
        bst_heights.append(bst_height)
        f.write(f"{size},{bst_height} {avl_height}, {rbt_height}\n")


plt.figure(figsize=(10, 6))

plt.plot(sizes, bst_heights, label='Binary Search Tree (BST)', marker='o')
plt.plot(sizes, avl_heights, label='AVL Tree', marker='x', color='blue')
plt.plot(sizes, rbt_heights, label='Red-Black Tree', marker='o', color='green')

plt.title('Высота деревьев поиска в зависимости от числа узлов')
plt.xlabel('Количество узлов')
plt.ylabel('Высота дерева')
plt.legend()
plt.grid(True)
plt.show()
