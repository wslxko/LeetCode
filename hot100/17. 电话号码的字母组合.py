"""
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

示例:

输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
说明:
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

import time


class Solution:
    def letterCombinations(self, digits):
        dict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        cls = []
        result = []
        if len(digits) == 0:
            return result
        if len(digits) == 1:
            for i in dict[digits]:
                result.append(i)
        else:
            for i in digits:
                cls.append(dict[i])
            for i in range(len(cls)):
                for j in range(i, len(cls)):
                    if i != j:
                        for i_num in cls[i]:
                            for j_num in cls[j]:
                                result.append(i_num + j_num)
        return result


if __name__ == "__main__":
    a = Solution()
    digits = "2345"
    print(a.letterCombinations(digits))
    print(time.strftime("%Y-%m-%d %H:%M:%S"))
