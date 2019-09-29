"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""


class Solution(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            newx = -x
        else:
            newx = x
        x_str = str(newx)
        half = len(x_str) // 2
        mid = None
        if len(x_str) % 2 == 1:
            mid = [x_str[half]]
            left = x_str[:half]
            right = x_str[half + 1:]
        else:
            left = x_str[:half]
            right = x_str[half:]
        left = list(left)
        right = list(right)
        left.reverse()
        right.reverse()
        if mid:
            result = right + mid + left
        else:
            result = right + left

        if x < 0:
            value = -int(''.join(result))
        else:
            value = int(''.join(result))

        if -2 ** 31 >= value or value >= 2 ** 31 - 1:
            return 0
        else:
            return value


class Solution2(object):

    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        str_x = str(x)
        x = ''
        if str_x[0] == '-':
            x += '-'
        x += str_x[len(str_x) - 1::-1].lstrip("0").rstrip("-")
        x = int(x)
        if -2 ** 31 < x < 2 ** 31 - 1:
            return x
        return 0


if __name__ == '__main__':
    import math

    solu = Solution()

    a = solu.reverse(-1563847412)
    print(a)

    b = math.pow(2, 31) - 1

    print(b)
