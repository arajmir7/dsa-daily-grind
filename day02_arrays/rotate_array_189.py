class Solution:
    def reverse(self, A, start, end):
        while start < end:
            A[start], A[end] = A[end], A[start]
            start += 1
            end -= 1
    
    def rotateArray(self, A, k, direction):
        n = len(A)
        if n == 0:
            return A
        
        k = k % n
        if k == 0:
            return A

        if direction == "right":
            self.reverse(A, 0, n-1)
            self.reverse(A, 0, k-1)
            self.reverse(A, k, n-1)

        elif direction == "left":
            self.reverse(A, 0, k-1)
            self.reverse(A, k, n-1)
            self.reverse(A, 0, n-1)

        else:
            raise ValueError("direction must be left or right")
        
        return A

if __name__ == "__main__":        
    A = [1,2,3,4,5,6,7,8]
    k = 5
    direction ="right"
    sol = Solution()
    result = sol.rotateArray(A, k, direction)
    print("After rotation: ", result)