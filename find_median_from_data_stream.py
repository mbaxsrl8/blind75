# Tags: design, heap

import heapq

# The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

# For example:

# For arr = [1,2,3], the median is 2.
# For arr = [1,2], the median is (1 + 2) / 2 = 1.5
# Implement the MedianFinder class:

# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num from the data stream to the data structure.
# double findMedian() returns the median of all elements so far.

class MedianFinder:

    def __init__(self):
        self.small_heap = []  # second half
        self.big_heap = []  # first half

    def addNum(self, num: int) -> None:
        if len(self.small_heap) == 0:
            heapq.heappush(self.small_heap, num)
            return
        bigger_median = self.small_heap[0]
        if num < bigger_median:
            heapq.heappush(self.big_heap, 0 - num)
        else:
            heapq.heappush(self.small_heap, num)

        if len(self.big_heap) > len(self.small_heap):
            heapq.heappush(self.small_heap, 0 - heapq.heappop(self.big_heap))
        if len(self.small_heap) == len(self.big_heap) + 2:
            heapq.heappush(self.big_heap, 0 - heapq.heappop(self.small_heap))

    def findMedian(self) -> float:
        if len(self.small_heap) == len(self.big_heap):
            num1 = self.small_heap[0]
            num2 = 0 - self.big_heap[0]
            res = (num1 + num2) / 2
            return res
        else:
            return self.small_heap[0]


if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
