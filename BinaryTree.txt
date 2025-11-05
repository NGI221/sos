class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def find_min(self, root):
        while root.left is not None:
            root = root.left
        return root

    def delete(self, root, key):
        if root is None:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            # Node with two children: Get inorder successor
            temp = self.find_min(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)
        return root

    def inorder(self, root):
        return [] if root is None else self.inorder(root.left) + [root.key] + self.inorder(root.right)

# Interactive CLI
bst = BST()
while True:
    print("\nChoose operation: 1) Insert 2) Search 3) Delete 4) Display 5) Exit")
    choice = input("Enter choice number: ").strip()
    if choice == '1':
        try:
            key = int(input("Enter integer key to insert: "))
            bst.root = bst.insert(bst.root, key)
            print(f"Inserted {key}.")
        except ValueError:
            print("Key must be an integer.")
    elif choice == '2':
        try:
            key = int(input("Enter integer key to search: "))
            node = bst.search(bst.root, key)
            if node:
                print(f"Key {key} found in the BST.")
            else:
                print(f"Key {key} not found.")
        except ValueError:
            print("Key must be an integer.")
    elif choice == '3':
        try:
            key = int(input("Enter integer key to delete: "))
            bst.root = bst.delete(bst.root, key)
            print(f"Deleted {key} if it existed.")
        except ValueError:
            print("Key must be an integer.")
    elif choice == '4':
        sorted_keys = bst.inorder(bst.root)
        print("BST Inorder traversal: ", sorted_keys if sorted_keys else "Empty tree")
    elif choice == '5':
        print("Exiting BST program.")
        break
    else:
        print("Invalid choice. Try again.")