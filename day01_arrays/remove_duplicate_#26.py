class Solution:
    def removeDuplicates(self, A):
        if not A:
            return 0
        i = 0
        for j in range(1, len(A)):
            if A[i] != A[j]:
                i += 1
                A[i] = A[j]
        return i + 1
A = [0,0,1,1,1,2,2,3,3,4,4]
sol = Solution()
k = sol.removeDuplicates(A)
print("Unique Count", k)
print("Array after removing duplicates: ", A[:k])