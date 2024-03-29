"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s in ('', None):
            return 0
        s_length = len(s)
        s_lst = list(s)
        s_set = set(s_lst)
        max_length = len(s_set)
        if max_length == s_length:
            return max_length
        if max_length <= 1:
            return max_length

        for i in range(max_length):
            left_max = max_length - i
            for j in range(s_length - left_max + 1):
                set_count = len(set(s_lst[j:left_max + j]))
                if set_count == left_max:
                    return left_max
        return 0

    def lengthOfLongestSubstring_2(self, s):
        if s == '':
            return 0
        start, end = 0, 0  # 以当前字符结束的最大子串起止下标
        subl = 1  # 以当前字符结束的最大子串长度
        maxl = 1
        l = s.__len__()
        for i in range(1, l):
            ss = s[start:end + 1]  # 以上一字符结束的最大子串
            index = ss.find(s[i])
            if index == -1:  # 当前字符未在子串出现，可以加入子串
                end += 1
            else:  # 当前字符重复, 子串位置后移（因为子串是不重复的，所以移动后得到的一定是不重复子串）
                start = start + index + 1
                end += 1
            subl = end - start + 1
            maxl = max(maxl, subl)
        return maxl


if __name__ == '__main__':
    sol = Solution()

    result = sol.lengthOfLongestSubstring("dvdf")

    print(result)
