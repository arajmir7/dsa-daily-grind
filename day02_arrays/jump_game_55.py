class Solution:
    def canJump(self, A):
        max_index = 0
        for i in range(len(A)):
            if i > max_index:
                return False
            max_index = max(max_index, i+A[i])
        return True

if __name__ == "__main__":    
    A = [2,3,4,5,1,5,1]
    sol = Solution()
    ans = sol.canJump(A)
    print("Array: ", A)
    print("Can reach: ", ans)