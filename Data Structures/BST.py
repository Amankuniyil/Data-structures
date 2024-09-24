class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, curr_node):
        if data < curr_node.data:
            if curr_node.left is None:
                curr_node.left = Node(data)
            else:
                self._insert(data, curr_node.left)
        elif data > curr_node.data:
            if curr_node.right is None:
                curr_node.right = Node(data)
            else:
                self._insert(data, curr_node.right)

    def search(self, data):
        return self._search(data, self.root)

    def _search(self, data, curr_node):
        if curr_node:
            if data == curr_node.data:
                return True
            elif data < curr_node.data:
                return self._search(data, curr_node.left)
            else:
                return self._search(data, curr_node.right)
        return False

    def inorder(self):
        elems = []
        self._inorder(self.root, elems)
        return elems

    def _inorder(self, curr_node, elems):
        if curr_node:
            self._inorder(curr_node.left, elems)
            elems.append(curr_node.data)
            self._inorder(curr_node.right, elems)

    def delete(self, data):
        self.root = self._delete(self.root, data)




    def _delete(self, node, data):
        if not node:
            return node
        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._min_value_node(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current
