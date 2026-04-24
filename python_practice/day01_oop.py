class Solution(object):
    def removeDuplicates(self, A, val):
        i = 0
        for j in range(len(A)):
            if A[j] != val:
                A[i] = A[j]
                i += 1
        return i


if __name__ == "__main__":
    A = [1,1,2,3,3,4,4,5,5,6]
    val = 4
    sol = Solution()
    k = sol.removeDuplicates(A, val)
    print("k: ", k)
    print("After removing duplijcates: ", A[:k])

   