class Solution:
    def findPeakElement(self, nums):
        left = 0
        right = len(nums) - 1
        
        while left < right:
            mid = (left + right)//2
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        return left
    
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    sol = Solution()
    ans = sol.findPeakElement(nums)
    print("Array:", nums)
    print("Peak Index:", ans)