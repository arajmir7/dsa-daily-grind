class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_area = 0
        while left < right:
            width = right - left
            h = min(height[left], height[right])
            area = width * h
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

if __name__ == "__main__":
    A = [1,8,6,2,5,4,8,3,7]
    sol = Solution()
    result = sol.maxArea(A)
    print("Area: ", A)
    print("Max area: ", result)