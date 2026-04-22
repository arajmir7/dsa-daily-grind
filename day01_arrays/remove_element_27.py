class Solution(object):
    def removeElement(self, A, val):
        i = 0
        for j in range(len(A)):
            if A[j] != val:
                A[i] = A[j]
                i += 1
        return i
A = [0,1,2,2,3,4,0,2]
val = 2
sol = Solution()
k = sol.removeElement(A, val)
print("k =" , k)
print("Updated elements: ", A[:k])