# Tags: binary-search, review-priority
# You are given two integer arrays nums1 and nums2 of size m and n respectively, where each is sorted in ascending order. Return the median value among all elements of the two arrays.


# Your solution should run in O(log(m+n)) time.
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        left_count = 0
        expected_partition_size = (m + n) // 2
        l = max(0, expected_partition_size - n - 1)
        if l > 0:
            left_count += l
        r = min(m - 1, expected_partition_size - 1)
        while left_count < expected_partition_size:
            i = (l + r) // 2
            j = expected_partition_size - (i + 1) - 1
            if r == -1:
                left_count += expected_partition_size
                break
            if n > j + 1 >= 0 and nums1[i] > nums2[j + 1]:
                r = i if r > i else i - 1
            elif n > j >= 0 and i + 1 < m and nums2[j] > nums1[i + 1]:
                if l == i:
                    left_count += i - l + 1
                    l = i + 1
                else:
                    left_count += i - l
                    l = i
            else:
                left_count += i - l + 1
                if j + 1 > 0:
                    left_count += j + 1

        i = (l + r) // 2
        j = expected_partition_size - (i + 1) - 1
        left_max = None
        if 0 <=i < m:
            left_max = nums1[i]
        if 0 <= j < n:
            left_max = max(left_max, nums2[j]) if left_max is not None else nums2[j]
        right_min = None
        if 0 <= i + 1 < m:
            right_min = nums1[i + 1]
        if 0 <= j + 1 < n:
            right_min = min(right_min, nums2[j + 1]) if right_min is not None else nums2[j + 1]
        if (m + n) % 2 == 0:
            return (left_max + right_min) / 2
        else:
            return right_min


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMedianSortedArrays(nums1=[], nums2=[1]))
    # print(sol.findMedianSortedArrays(nums1=[2,2,4,4], nums2=[2,2,4,4]))
    # print(sol.findMedianSortedArrays(nums1=[3,4], nums2=[1,2]))
    # print(sol.findMedianSortedArrays(nums1=[1, 2], nums2=[3]))
    # print(sol.findMedianSortedArrays(nums1=[1,3], nums2=[2,4]))
    # print(sol.findMedianSortedArrays(nums1=[1,2], nums2=[3,4]))
    # print(sol.findMedianSortedArrays(nums1=[1], nums2=[2,3,4,5,6,7,8,9,10]))
    # print(sol.findMedianSortedArrays(nums1=[-1000000], nums2=[1000000]))
    # print(sol.findMedianSortedArrays(nums1=[0,0], nums2=[0, 1, 1, 1]))
    # print(sol.findMedianSortedArrays(nums1=[0,1, 1], nums2=[0]))
    # print(sol.findMedianSortedArrays(nums1=[0, 0, 1, 1, 1], nums2=[0]))
    # print(sol.findMedianSortedArrays(nums1=[0,0,0,1,1,1,1], nums2=[0]))
