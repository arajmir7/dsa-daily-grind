class Solution:
    def longestConsecutive(self, A):
        if not A:
            return 0
        
        st = set(A)
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
        
