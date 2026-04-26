class Solution:
    def longestConsecutive(self, nums):
       
        if not nums:
            return 0
        st = set(nums)
        longest = 0

        for num in st:
            if num - 1 not in st:
                current = num
                count = 1
                while current + 1 in st:
                    current += 1
                    count += 1
                longest = max(longest, count)
        return longest

if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    sol = Solution()
    result = sol.longestConsecutive(nums)
    print("Longest Consecutive Sequence: ", result)