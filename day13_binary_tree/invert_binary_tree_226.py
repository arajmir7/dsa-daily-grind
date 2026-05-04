class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        
        root.left, root.right = root.right, root.left 
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

def print_level_order(root):
    from collections import deque
    q = deque([root])
    
    while q:
        node = q.popleft()
        if node:
            print(node.val, end=" ")
            q.append(node.left)
            q.append(node.right)
    print()


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()
    new_root = sol.invertTree(root)
    print("Inverted Tree (Level Order):")
    print_level_order(new_root)