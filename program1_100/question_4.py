"""

给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。

请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。

你可以假设 nums1 和 nums2 不会同时为空。

示例 1:

nums1 = [1, 3]
nums2 = [2]

则中位数是 2.0
示例 2:

nums1 = [1, 2]
nums2 = [3, 4]

则中位数是 (2 + 3)/2 = 2.5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/median-of-two-sorted-arrays
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""
import sys


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        length = len(nums1) + len(nums2)
        if length % 2 == 0:
            return (self.helper(nums1, 0, nums2, 0, length // 2) + self.helper(nums1, 0, nums2, 0,
                                                                              length // 2 + 1)) / 2.0

        return self.helper(nums1, 0, nums2, 0, (length + 1) // 2)

    def helper(self, nums1, m, nums2, n, k):
        if m >= len(nums1):
            return nums2[n + k - 1]
        if n >= len(nums2):
            return nums1[m + k - 1]
        if k == 1:
            return min(nums1[m], nums2[n])

        p1 = m + k // 2 - 1
        p2 = n + k // 2 - 1
        mid1 = nums1[p1] if p1 < len(nums1) else sys.maxsize
        mid2 = nums2[p2] if p2 < len(nums2) else sys.maxsize
        if mid1 < mid2:
            return self.helper(nums1, m + k // 2, nums2, n, k - k // 2)

        return self.helper(nums1, m, nums2, n + k // 2, k - k // 2)


if __name__ == '__main__':
    solu = Solution()
    a = solu.findMedianSortedArrays(nums1=[1, 3],
                                    nums2=[2])

    print(a)

    b = solu.findMedianSortedArrays(nums1=[1, 2],
                                    nums2=[3, 4])

    print(b)
