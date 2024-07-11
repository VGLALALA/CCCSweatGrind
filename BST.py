class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def deleteNode(root, key):
    if not root:
        return root

    # If the key to be deleted is smaller than the root's key
    # then it lies in the left subtree
    if key < root.val:
        root.left = deleteNode(root.left, key)

    # If the key to be deleted is greater than the root's key
    # then it lies in the right subtree
    elif key > root.val:
        root.right = deleteNode(root.right, key)

    # If key is the same as root's key, then this is the node to be deleted
    else:
        # Node with only one child or no child
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        # Node with two children:
        # Get the inorder successor (smallest in the right subtree)
        temp = findMin(root.right)

        # Copy the inorder successor's content to this node
        root.val = temp.val

        # Delete the inorder successor
        root.right = deleteNode(root.right, temp.val)

    return root

def findMin(node):
    current = node
    while current.left:
        current = current.left
    return current

# Helper function to insert a new node with the given key
def insert(root, key):
    if not root:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# Helper function to do inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

# Driver program to test the functions
if __name__ == '__main__':
    root = None
    keys = [50, 30, 20, 40, 70, 60, 80]

    for key in keys:
        root = insert(root, key)

    print("Inorder traversal of the given tree")
    inorder(root)
    print()

    print("\nDelete 20")
    root = deleteNode(root, 20)
    print("Inorder traversal of the modified tree")
    inorder(root)
    print()

    print("\nDelete 30")
    root = deleteNode(root, 30)
    print("Inorder traversal of the modified tree")
    inorder(root)
    print()

    print("\nDelete 50")
    root = deleteNode(root, 50)
    print("Inorder traversal of the modified tree")
    inorder(root)
    print()
