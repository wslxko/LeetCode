"""
给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1：

输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
示例 2：

输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
 

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/combination-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import itertools24

class Solution:
    def combinationSum(self, candidates, target):
        cls = []
        for index in range(len(candidates)):
            result = list(itertools.combinations_with_replacement(candidates, index + 1))
            for i in result:
                if sum(i) == target:
                    cls.append(list(i))

        for j in candidates:
            cls_1 = []
            num = j
            index = 1
            if target % j == 0:
                while j*index < target:
                    num += num
                    index += 1
                for k in range(index):
                    cls_1.append(j)
                if cls_1 not in cls:
                    cls.append(cls_1)
        return cls


if __name__ == "__main__":
    a = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    print(a.combinationSum(candidates, target))
