#python TREE

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    # Method to insert a value into the binary tree
    def insert(self, val):
        self.root = self.insertRec(self.root, val)

    def insertRec(self, node, val):
        if node is None:
            return TreeNode(val)

        if val < node.val:
            node.left = self.insertRec(node.left, val)
        elif val > node.val:
            node.right = self.insertRec(node.right, val)

        return node

    # Method to perform inorder traversal of the binary tree
    def inorderTraversal(self):
        self.inorderTraversalRec(self.root)
        print()

    def inorderTraversalRec(self, node):
        if node:
            self.inorderTraversalRec(node.left)
            print(node.val, end=" ")
            self.inorderTraversalRec(node.right)

    # Method to search for a value in the binary tree
    def search(self, val):
        return self.searchRec(self.root, val)

    def searchRec(self, node, val):
        if node is None:
            return False

        if val == node.val:
            return True
        elif val < node.val:
            return self.searchRec(node.left, val)
        else:
            return self.searchRec(node.right, val)

    # Method to find the maximum value in the binary tree
    def findMax(self):
        if self.root is None:
            raise ValueError("Tree is empty")

        return self.findMaxRec(self.root)

    def findMaxRec(self, node):
        if node.right:
            return self.findMaxRec(node.right)

        return node.val

if __name__ == "__main__":
    tree = BinaryTree()

    # Insert values into the binary tree
    tree.insert(50)
    tree.insert(30)
    tree.insert(20)
    tree.insert(40)
    tree.insert(70)
    tree.insert(60)
    tree.insert(80)

    # Perform inorder traversal of the binary tree
    print("Inorder Traversal:")
    tree.inorderTraversal()

    # Search for a value in the binary tree
    search_value = 40
    print(f"Searching for {search_value}: {tree.search(search_value)}")

    # Find the maximum value in the binary tree
    print("Maximum value:", tree.findMax())
