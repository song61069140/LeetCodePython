"""

给出 n 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且有效的括号组合。

例如，给出 n = 3，生成结果为：

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/generate-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



"""


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        total_l = []
        total_l.append([None])  # 0组括号时记为None
        total_l.append(["()"])  # 1组括号只有一种情况
        for i in range(2, n + 1):  # 开始计算i组括号时的括号组合
            l = []
            for j in range(i):  # 开始遍历 p q ，其中p+q=i-1 , j 作为索引
                now_list1 = total_l[j]  # p = j 时的括号组合情况
                now_list2 = total_l[i - 1 - j]  # q = (i-1) - j 时的括号组合情况
                for k1 in now_list1:
                    for k2 in now_list2:
                        if k1 is None:
                            k1 = ""
                        if k2 is None:
                            k2 = ""
                        el = "(" + k1 + ")" + k2
                        l.append(el)  # 把所有可能的情况添加到 l 中
            total_l.append(l)  # l这个list就是i组括号的所有情况，添加到total_l中，继续求解i=i+1的情况
        return total_l[n]


if __name__ == '__main__':
    solu = Solution()
    print(solu.generateParenthesis(3))
