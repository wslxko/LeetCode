'''
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import itertools


class Solution:
    def subsetWithDup(self, nums):
        result = []
        for index in range(len(nums) + 1):
            newNums = itertools.combinations(nums, index)
            for num in newNums:
                if list(num) not in result:
                    result.append(list(num))
        return result


if __name__ == "__main__":
    a = Solution()
    nums = [1, 2, 2]
    print(a.subsetWithDup(nums))
