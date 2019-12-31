'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba" 也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def longestPalindrome(self, s):
        palindrome = []
        for indexOuter in range(len(s)):
            for indexInner in range(len(s)):
                if indexInner > indexOuter:
                    a = s[indexOuter:indexInner]
                    b = s[indexOuter:indexInner][::-1]
                    if a == b:
                        palindrome.append(s[indexOuter:indexInner])
        palindrome.sort(key=lambda i: len(i), reverse=True)
        return palindrome[0]


if __name__ == "__main__":
    a = Solution()
    s = "babad"
    print(a.longestPalindrome(s))
