class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root, val):
        while root:

            # Target found
            if root.val == val:
                return root

            # Search left subtree
            elif val < root.val:
                root = root.left

            # Search right subtree
            else:
                root = root.right

        return None

if __name__ == "__main__":
    root = TreeNode(8)
    root.left = TreeNode(3)
    root.right = TreeNode(10)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(6)
    root.left.right.left = TreeNode(4)
    root.left.right.right = TreeNode(7)
    root.right.right = TreeNode(14)
    root.right.right.left = TreeNode(13)
    target = 6
    sol = Solution()
    result = sol.searchBST(root, target)
    if result:
        print("Target Found:", result.val)
    else:
        print("Target Not Found")