'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。
'''


class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) > 0:
            sortStrs = sorted(strs, reverse=False, key=len)
            minLen = len(sortStrs[0])
            commonStr = sortStrs[0]
            sortStrs.remove(sortStrs[0])
            commonList = []
            for index in range(minLen):
                common = commonStr[:index + 1]
                for index1 in range(len(sortStrs)):
                    if sortStrs[index1].startswith(common):
                        commonList.append(common)
                if commonList.count(common) > 1:
                    commonList = list(set(commonList))
                else:
                    if common in commonList:
                        commonList.remove(common)
            commonList.sort(reverse=True, key=len)

            if len(commonList) > 0:
                return commonList[0]
            else:
                return " "
        else:
            return " "


if __name__ == "__main__":
    a = Solution()
    l = ["flower", "flow", "flight"]
    print(a.longestCommonPrefix(l))
