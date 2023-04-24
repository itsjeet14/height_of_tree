class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

def createBalancedTree(data):
    if not data:
        return None
    mid = len(data)//2
    root = Node(data[mid])
    root.left = createBalancedTree(data[:mid])
    root.right = createBalancedTree(data[mid+1:])
    return root

def maxDepth(root):
    if root is None:
        return 0
    else:
        rDepth = maxDepth(root.right)
        lDepth = maxDepth(root.left)
        if rDepth > lDepth:
            return rDepth + 1
        else:
            return lDepth + 1

if __name__ == "__main__":
    data = list(map(int, input("Enter element separated by space: ").split()))
    data.sort()
    root = createBalancedTree(data)
    print("Height of tree: ",maxDepth(root))