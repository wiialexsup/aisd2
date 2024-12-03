import random
from collections import deque


# Класс узла дерева
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key


# Класс бинарного дерева
class BinaryTree:
    def __init__(self):
        self.root = None

    # Вставка узла в дерево
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

    # Обход в глубину (pre-order)
    def dfs_pre_order(self):
        result = []
        self._dfs_pre_order(self.root, result)
        return result

    def _dfs_pre_order(self, node, result):
        if node:
            result.append(node.value)
            self._dfs_pre_order(node.left, result)
            self._dfs_pre_order(node.right, result)

    # Обход в глубину (in-order)
    def dfs_in_order(self):
        result = []
        self._dfs_in_order(self.root, result)
        return result

    def _dfs_in_order(self, node, result):
        if node:
            self._dfs_in_order(node.left, result)
            result.append(node.value)
            self._dfs_in_order(node.right, result)

    # Обход в глубину (post-order)
    def dfs_post_order(self):
        result = []
        self._dfs_post_order(self.root, result)
        return result

    def _dfs_post_order(self, node, result):
        if node:
            self._dfs_post_order(node.left, result)
            self._dfs_post_order(node.right, result)
            result.append(node.value)

    # Обход в ширину (BFS)
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


# Пример использования
if __name__ == "__main__":
    # Создание и заполнение дерева случайными числами
    tree = BinaryTree()
    for _ in range(10):
        tree.insert(random.randint(1, 100))

    # Обход в глубину (pre-order)
    print("DFS Pre-order:", tree.dfs_pre_order())

    # Обход в глубину (in-order)
    print("DFS In-order:", tree.dfs_in_order())

    # Обход в глубину (post-order)
    print("DFS Post-order:", tree.dfs_post_order())

    # Обход в ширину (BFS)
    print("BFS:", tree.bfs())