class Node:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


operators = {'+', '-', '*', '/', '^'}


def build_from_prefix(expr):
    expr = expr[::-1]
    stack = []
    for ch in expr:
        if ch not in operators:
            stack.append(Node(ch))
        else:
            a, b = stack.pop(), stack.pop()
            node = Node(ch)
            node.left, node.right = a, b
            stack.append(node)
    return stack[-1]


def postorder_non_recursive(root):
    if not root:
        return []
    s1, s2 = [root], []
    while s1:
        n = s1.pop()
        s2.append(n)
        if n.left:
            s1.append(n.left)
        if n.right:
            s1.append(n.right)
    return [n.val for n in reversed(s2)]


def delete_tree(root):
    if root:
        root.left = root.right = None
    return None


expr = "+--abc/def"
root = build_from_prefix(expr)
print("Prefix Expression:", expr)
print("Postorder (Non-Recursive):", " ".join(postorder_non_recursive(root)))
root = delete_tree(root)
print("Tree deleted. Root is now:", root)
