'''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def mergeTwoLists(self, l1, l2):
        newl1 = l1.split('->')
        newl2 = l2.split('->')
        newl = sorted(newl1 + newl2)
        afterMerge = '->'.join(newl)
        return afterMerge

if __name__ == "__main__":
    a = Solution()
    l1 = '1->2->4'
    l2 = '1->3->4'
    print(a.mergeTwoLists(l1, l2))
