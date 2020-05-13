'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
请注意，你的答案必须是 子串 的长度，"wke" 是一个子序列，不是子串。
'''

# 因为使用的循环，所以导致时间方面消耗非常大，暂时只会这一招
class Solution:
    def lengthOfLongestSubstring(self, s):
        lists = list(s)
        listsSet = list(set(lists))
        if len(lists) > 0:
            if lists == listsSet:
                return len(lists)
        elif len(lists) == 0:
            return 0

        a = []
        for i in range(len(lists)):
            for j in range(i, len(lists) + 1):
                list2 = lists[i:j]
                list2set = list(set(list2))
                list2set.sort(key=list2.index)
                if list2 == list2set:
                    a.append(list2)

        a.sort(reverse=True, key=len)
        return len(a[0])


if __name__ == "__main__":
    a = Solution()
    print(a.lengthOfLongestSubstring("sdofksokp"))
