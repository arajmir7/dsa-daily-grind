class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root, p, q):

        while root:

            # Both nodes are on left side
            if p.val < root.val and q.val < root.val:
                root = root.left

            # Both nodes are on right side
            elif p.val > root.val and q.val > root.val:
                root = root.right

            # Split point found
            else:
                return root

if __name__ == "__main__":
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    # Nodes to find LCA
    p = root.left          # Node 2
    q = root.right         # Node 8
    sol = Solution()
    ans = sol.lowestCommonAncestor(root, p, q)
    print("Lowest Common Ancestor:", ans.val)