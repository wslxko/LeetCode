"""
实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列。

如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。

必须 原地 修改，只允许使用额外常数空间。

示例 1：

输入：nums = [1,2,3]
输出：[1,3,2]
示例 2：

输入：nums = [3,2,1]
输出：[1,2,3]
示例 3：

输入：nums = [1,1,5]
输出：[1,5,1]
示例 4：

输入：nums = [1]
输出：[1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-permutation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import itertools


class Solution:
    def nextPermutation(self, nums):
        set_nums = tuple(nums)
        all_permu = list(itertools.permutations(nums))
        all_permu.sort()
        for index in range(len(all_permu)):
            if all_permu[index] == set_nums and index == len(all_permu) - 1:
                nums.sort()
                return nums
            elif all_permu[index] == set_nums:
                return list(all_permu[index + 1])


if __name__ == "__main__":
    a = Solution()
    nums = [1, 2, 3]
    print(a.nextPermutation(nums))
