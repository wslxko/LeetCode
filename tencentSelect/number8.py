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


class Solution:
    def subsetsWithDup(self, nums):
        output = [[]]
        set_output = []
        for i in range(len(nums)):
            for j in range(len(output)):
                output.append(output[j] + [nums[i]])

        for i in output:
            if i not in set_output:
                set_output.append(i)
        return set_output


if __name__ == '__main__':
    nums = [1, 2, 2]
    a = Solution()
    print(a.subsetsWithDup(nums))
