class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root):

        # DFS function
        def dfs(node, low, high):

            # Base Case
            # Empty node is always valid
            if not node:
                return True

            # Current node must stay inside valid range
            if node.val <= low or node.val >= high:
                return False

            # Check left subtree
            left = dfs(node.left, low, node.val)

            # Check right subtree
            right = dfs(node.right, node.val, high)

            # Both subtrees must be valid
            return left and right
            
        return dfs(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(12)
    root.right.right = TreeNode(20)
    sol = Solution()
    result = sol.isValidBST(root)
    print("Is Valid BST:", result)