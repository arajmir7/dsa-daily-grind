import heapq
class Solution:
    def findKthLargest(self, nums, k):

        # Min Heap
        min_heap = []

        # Process all numbers
        for num in nums:

            # Insert into heap
            heapq.heappush(min_heap, num)

            # Keep heap size = k
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        # Root = kth largest
        return min_heap[0]

if __name__ == "__main__":
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    sol = Solution()
    result = sol.findKthLargest(nums, k)
    print(f"{k}th Largest Element:", result)