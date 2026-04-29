class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right)//2

            if nums[mid] == target:
                return mid

            elif nums[mid] < target:
                left = mid + 1

            else:
                right = mid - 1

        return -1

if __name__ == "__main__":
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    sol = Solution()
    ans = sol.search(nums, target)
    print("Array:", nums)
    print("Target:", target)
    print("Index:", ans)