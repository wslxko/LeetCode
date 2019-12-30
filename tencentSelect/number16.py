'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
说明:

所有输入只包含小写字母 a-z 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-common-prefix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def longestCommonPrefix(self, strs):
        newStrs = sorted(strs, key=lambda i: len(i), reverse=False)
        maxLen = len(newStrs[0])
        numberLen = len(newStrs[1:])
        for i in range(maxLen):
            publicStr = newStrs[0][:i]
            for j in range(numberLen):
                if publicStr not in newStrs[1:][j]:
                    return newStrs[0][:i - 1]
                return None


if __name__ == "__main__":
    a = Solution()
    strs = ["dog", "racecar", "car"]
    print(a.longestCommonPrefix(strs))
