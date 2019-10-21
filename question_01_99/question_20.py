"""

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 运用栈的思想，遍历完后  栈内要清空
        math_case = {
            '{': '}',
            '[': ']',
            '(': ')',
        }

        if not s:
            return True
        if len(s) % 2 == 1:
            return False
        stack = []
        for item in s:
            if item in math_case.keys():
                stack.append(item)
            elif item in math_case.values() and stack:
                if math_case[stack[len(stack) - 1]] == item:
                    stack = stack[:-1]
                else:
                    return False
            else:
                return False
        # 栈内数据未处理完
        if len(stack) != 0:
            return False
        return True


if __name__ == '__main__':
    solu = Solution()
    print(solu.isValid('{[]}'))
