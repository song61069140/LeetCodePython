"""


给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

例如，给定数组 nums = [-1，2，1，-4], 和 target = 1.

与 target 最接近的三个数的和为 2. (-1 + 2 + 1 = 2).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum-closest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        # res_lst = []
        res = nums[0] + nums[1] + nums[2] - target
        for x in range(len(nums)):
            a = nums[x]
            y = x + 1
            z = len(nums) - 1
            while y < z:
                b = nums[y]
                c = nums[z]
                sum = a + b + c
                if abs(sum - target) < abs(res - target):
                    res = sum
                if sum > target:
                    z -= 1
                elif sum < target:
                    y += 1
                else:
                    res = target
                    return res
        return res


if __name__ == '__main__':
    solu = Solution()

    # print(solu.threeSumClosest([-1, 2, 1, -4], 1))
    print(solu.threeSumClosest([0, 2, 1, -3], 1))
