"""
30 串联所有单词的子串


给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

 

示例 1：

输入：
  s = "barfoothefoobarman",
  words = ["foo","bar"]
输出：[0,9]
解释：
从索引 0 和 9 开始的子串分别是 "barfoo" 和 "foobar" 。
输出的顺序不重要, [9,0] 也是有效答案。
示例 2：

输入：
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
输出：[]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/substring-with-concatenation-of-all-words
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""


class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        res = []
        write = []
        if len(words) == 0:
            return []
        if len(s) < len(words) * len(words[0]):
            return []
        dic = {}
        flag = 0
        for i in words:
            try:
                dic[i] += 1
            except KeyError:
                dic[i] = 1
                flag += 1
                write.append(i)
        # 是否存在用字典查看
        left, right = 0, len(words) * len(words[0])
        # 滑动窗口
        while right <= len(s):
            n, start = 0, left
            per = len(words[0])
            tag = dict(zip(write, [0] * flag))
            while n < len(words):
                # 若存在于字典中
                if dic.get(s[start:start + per]):
                    if tag[s[start:start + per]] < dic[s[start:start + per]]:
                        tag[s[start:start + per]] += 1
                        n += 1
                        start += per
                    else:
                        break
                else:
                    break
            if n == len(words):
                res.append(left)
            left += 1
            right += 1
        return res


if __name__ == '__main__':
    solu = Solution()
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    print(solu.findSubstring(s, words))

    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    print(solu.findSubstring(s, words))
