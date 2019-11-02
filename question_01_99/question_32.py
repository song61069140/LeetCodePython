"""

32. 最长有效括号


给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。

示例 1:

输入: "(()"
输出: 2
解释: 最长有效括号子串为 "()"
示例 2:

输入: ")()())"
输出: 4
解释: 最长有效括号子串为 "()()"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        res = [0] * (len(s) + 1)
        for i, v in enumerate(s):
            if v == '(':
                stack.append(i)
            elif v == ')' and stack:
                j = stack.pop()
                res[j] = 1
                res[i] = 1
        tmp, output = 0, 0
        # print(res)
        for i in res:
            if i == 0:
                output = max(tmp, output)
                tmp = 0
            elif i == 1:
                tmp += 1
        return output


if __name__ == '__main__':
    solu = Solution()
    print(solu.longestValidParentheses("(()"))
    print(solu.longestValidParentheses(")()())"))
