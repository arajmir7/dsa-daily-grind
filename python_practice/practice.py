class Solution:
    def rotate(self, matrix):
        n = len(matrix)
        for i in range(n): # Transpose(swapping across diagonal)
            for j in range(i, n): # To avoid double swapping
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        for i in range(n): # reverse each row
            matrix[i].reverse()

if __name__ == "__main__":
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    sol = Solution()
    ans = sol.rotate(matrix)
    print("After rotatation of matrix: ")
    for row in matrix:
        print(row)
