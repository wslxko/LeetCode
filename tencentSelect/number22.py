'''
给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: nums = [1,2,3]
输出:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def subsets(self, nums):
        subsetsNums = []
        for indexOuter in range(len(nums)):
            for indexInner in range(len(nums) + 1):
                num1 = list(nums[indexOuter:indexInner])
                num2 = list(nums[indexOuter:indexInner:2])
                if num1 not in subsetsNums:
                    subsetsNums.append(num1)
                if num2 not in subsetsNums:
                    subsetsNums.append(num2)
        return subsetsNums


if __name__ == "__main__":
    a = Solution()
    nums = [1, 2, 3]
    print(a.subsets(nums))