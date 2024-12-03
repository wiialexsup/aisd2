import random
from collections import deque



class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key



class BinaryTree:
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

    
    def dfs_pre_order(self):
        result = []
        self._dfs_pre_order(self.root, result)
        return result

    def _dfs_pre_order(self, node, result):
        if node:
            result.append(node.value)
            self._dfs_pre_order(node.left, result)
            self._dfs_pre_order(node.right, result)


    def dfs_in_order(self):
        result = []
        self._dfs_in_order(self.root, result)
        return result

    def _dfs_in_order(self, node, result):
        if node:
            self._dfs_in_order(node.left, result)
            result.append(node.value)
            self._dfs_in_order(node.right, result)

   
    def dfs_post_order(self):
        result = []
        self._dfs_post_order(self.root, result)
        return result

    def _dfs_post_order(self, node, result):
        if node:
            self._dfs_post_order(node.left, result)
            self._dfs_post_order(node.right, result)
            result.append(node.value)


    def bfs(self):
        if not self.root:
            return []

        result = []
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node.value)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result



if __name__ == "__main__":
   
    tree = BinaryTree()
    for _ in range(10):
        tree.insert(random.randint(1, 100))

    print("DFS Pre-order:", tree.dfs_pre_order())

    
    print("DFS In-order:", tree.dfs_in_order())

    
    print("DFS Post-order:", tree.dfs_post_order())

    print("BFS:", tree.bfs())
