class Solution:
    def topKFrequent(self, nums, k):
        # Frequency map
        count = {}

        # Count occurrences
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # Bucket array
        # Index = frequency
        freq = [[] for _ in range(len(nums) + 1)]

        # Place numbers into frequency buckets
        for num, c in count.items():
            freq[c].append(num)

        result = []

        # Traverse buckets backwards
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:

                result.append(num)

                # Stop when k elements collected
                if len(result) == k:
                    return result

if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    sol = Solution()
    result = sol.topKFrequent(nums, k)
    print(f"Top {k} Frequent Elements:", result)