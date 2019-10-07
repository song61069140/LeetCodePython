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
        x = str(x)
        x = list(x)
        x.reverse()
        if x[len(x)-1] == '-':
            x = x[:len(x) - 1]
            x.insert(0, '-')
        x = int(''.join(x))

        if -2 ** 31 >= x or x >= 2 ** 31 - 1:
            return 0
        else:
            return x


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
