class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def update_height(self, node):
        node.height = 1 + max(self.get_height(node.left),
                              self.get_height(node.right))

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        self.update_height(x)
        self.update_height(y)
        return y

    def insert(self, root, value, priority):
        if not root:
            return Node(value, priority)

        if priority < root.priority:
            root.left = self.insert(root.left, value, priority)
        else:
            root.right = self.insert(root.right, value, priority)

        self.update_height(root)
        balance = self.get_balance(root)

        if balance > 1:
            if priority < root.left.priority:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance < -1:
            if priority > root.right.priority:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def get_max(self, root):
        while root.right:
            root = root.right
        return root

    def delete(self, root, priority):
        if not root:
            return root

        if priority < root.priority:
            root.left = self.delete(root.left, priority)
        elif priority > root.priority:
            root.right = self.delete(root.right, priority)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.get_max(root.left)
            root.priority = temp.priority
            root.value = temp.value
            root.left = self.delete(root.left, temp.priority)

        self.update_height(root)
        balance = self.get_balance(root)

        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [(root.value, root.priority)] + self.inorder(root.right)


class PriorityQueueAVL:
    def __init__(self):
        self.tree = AVLTree()
        self.root = None

    def push(self, value, priority):
        self.root = self.tree.insert(self.root, value, priority)

    def pop(self):
        if not self.root:
            return None
        max_node = self.tree.get_max(self.root)
        self.root = self.tree.delete(self.root, max_node.priority)
        return max_node.value

    def peek(self):
        if not self.root:
            return None
        return self.tree.get_max(self.root).value

    def show(self):
        return self.tree.inorder(self.root)
