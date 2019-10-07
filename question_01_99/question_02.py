"""

给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


"""

# Definition for singly-linked list.
import math


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        该方法有可能转int的时候，长度溢出
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        str1 = str(l1.val)
        str2 = str(l2.val)
        while l1.next:
            l1 = l1.next
            str1 = str(l1.val) + str1
        while l2.next:
            l2 = l2.next
            str2 = str(l2.val) + str2

        v = int(str1) + int(str2)

        v_lst = list(str(v))
        first_node = ListNode(v_lst[0])
        for item in v_lst[1:]:
            node = ListNode(int(item))
            node.next = first_node
            first_node = node
        return first_node

    def addTwoNumbers_2(self, l1, l2):
        """
        用链表的思想来反向相加
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        r = re
        carry = 0
        while (l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = carry + x + y
            carry = s // 10
            r.next = ListNode(s % 10)
            r = r.next
            if (l1 != None): l1 = l1.next
            if (l2 != None): l2 = l2.next
        if (carry > 0):
            r.next = ListNode(1)
        return re.next


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    sol = Solution()
    aa = sol.addTwoNumbers(l1, l2)
    print(aa)

    bb = sol.addTwoNumbers_2(l1, l2)

    print(bb)
