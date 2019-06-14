'''
给定一个没有重复数字的序列，返回其所有可能的全排列。

示例:

输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

from itertools import permutations


class Solution:
    def permute(self, nums):
        all_list = []
        for p in permutations(nums):
            list_p = list(p)
            all_list.append(list_p)
        return all_list


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 5]
    a = Solution()
    print(a.permute(nums))
