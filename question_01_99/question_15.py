"""

给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]


        整个思路比较简单。

        满足要求的组合中，要么至多1个0，要么3个0。

        至多一个0，就意味着，最大值为正，最小值为负。
        只要将正数负数两两配对，那么，判断下和的相反数即可。利用 Counter 统计次数，实现很简单。

        3个0的情况，判断下加上即可。

        """
        import collections
        if len(nums) < 3:
            return []
        nums_dict, res = collections.Counter(nums), []
        for left, right in ((i, j) for i in nums_dict if i < 0 for j in nums_dict if j > 0):
            mid = -left - right
            if left <= mid <= right and mid in nums_dict:
                if mid in (left, right) and nums_dict[mid] == 1:
                    continue
                res.append([left, mid, right])
        if nums_dict.get(0, 0) >= 3:
            res.append([0] * 3)
        return res


if __name__ == '__main__':
    solu = Solution()
    print(solu.threeSum([-1, 0, 1, 2, -1, -4]))
