"""


编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        prefix = strs[0]
        for item in strs:
            for i in range(len(prefix)):
                if len(item) > i and prefix[i] != item[i]:
                    prefix = prefix[:i]
                    break
                elif len(item) <= i:
                    prefix = prefix[:i]
        return prefix


if __name__ == '__main__':
    pass
    solu = Solution()
    # print(solu.longestCommonPrefix(["flower", "flow", "flight"]))
    # print(solu.longestCommonPrefix(["dog", "racecar", "car"]))
    print(solu.longestCommonPrefix(["aa", "a"]))
