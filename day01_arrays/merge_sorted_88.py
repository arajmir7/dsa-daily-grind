class Solution(object):
    def merge(self, A, m, B, n):
        i = m-1
        j = n-1
        idx = m+n-1
        while i>=0 and j>=0:
            if A[i] >= B[j]:
                A[idx] = A[i]
                i -= 1
            else:
                A[idx] = B[j]
                j -= 1
            idx -= 1
        while j>=0:
            A[idx] = B[j]
            j -= 1
            idx -= 1

A = [4,5,6,0,0,0]
B = [1,2,3]
sol = Solution()
sol.merge(A,3,B,3)
print("Merge A: ", A)