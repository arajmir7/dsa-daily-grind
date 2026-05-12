import heapq
class MedianFinder:
    def __init__(self):
        # Max Heap (store negatives)
        self.small = []

        # Min Heap
        self.large = []

    def addNum(self, num):
        # Insert into max heap
        heapq.heappush(self.small, -num)

        # Maintain order property
        if (
            self.small and
            self.large and
            (-self.small[0] > self.large[0])
        ):
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        # Balance heaps
        if len(self.small) > len(self.large) + 1:
            value = -heapq.heappop(self.small)
            heapq.heappush(self.large, value)

        if len(self.large) > len(self.small) + 1:
            value = heapq.heappop(self.large)
            heapq.heappush(self.small, -value)

    def findMedian(self):
        # Left heap bigger
        if len(self.small) > len(self.large):
            return -self.small[0]

        # Right heap bigger
        if len(self.large) > len(self.small):
            return self.large[0]

        # Equal size
        return (
            -self.small[0] + self.large[0]
        ) / 2.0

if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    print("Median:", mf.findMedian())
    mf.addNum(2)
    print("Median:", mf.findMedian())
    mf.addNum(3)
    print("Median:", mf.findMedian())
    mf.addNum(4)
    print("Median:", mf.findMedian())