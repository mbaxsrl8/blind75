# Tags: heap, review-priority
import heapq

# You are given an 2-D array points where points[i] = [xi, yi] represents the coordinates of a point on an X-Y axis plane. You are also given an integer k.

# Return the k closest points to the origin (0, 0).

# The distance between two points is defined as the Euclidean distance (sqrt((x1 - x2)^2 + (y1 - y2)^2)).

# You may return the answer in any order. The answer is guaranteed to be unique(except for the order in which the points are returned.)
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for point in points:
            x, y = point[0], point[1]
            distanse = x*x + y*y
            if len(heap) < k:
                heapq.heappush(heap, (-distanse, x, y))
            elif distanse < -heap[0][0]:
                heapq.heapreplace(heap, (-distanse, x, y))
            
        result = [[item[1], item[2]] for item in heap]
        return result
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.kClosest(points =[[0,2],[2,2]], k = 1))
