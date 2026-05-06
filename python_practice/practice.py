class Solution:
    def search(self, num, min):
        left = 0
        right = len(num)-1

        while left <= right:
            mid = (left + right) // 2

            if num[mid] == target:
                return mid
            
            if num[left] <= num[mid]:
                if num[left] <= target <= num[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if num[mid] <= target <= num[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1
if __name__ == "__main__":
    num = [1,3,4,0,6,7,8,9]
    target = 0
    sol = Solution()
    result = sol.search(num, target)
    print(result)