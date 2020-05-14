'''
字符串的排列
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:

输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").


示例2:

输入: s1= "ab" s2 = "eidboaoo"
输出: False


注意：

输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间
'''

import itertools


class Solution:
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False

        lenS1 = len(s1)
        result = []
        s1permutations = list(itertools.permutations(s1, lenS1))
        for i in s1permutations:
            s1List = "".join(list(i))
            if s1List in s2:
                result.append(s1List)
        return len(result) > 0


if __name__ == "__main__":
    a = Solution()
    s1 = "ab"
    s2 = "eidbaooo"
    print(a.checkInclusion(s1, s2))
