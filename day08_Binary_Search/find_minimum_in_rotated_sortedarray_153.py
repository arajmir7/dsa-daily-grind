class Solution:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1

        return nums[left]

if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    sol = Solution()
    result = sol.findMin(nums)
    print("Minimum element is", result)