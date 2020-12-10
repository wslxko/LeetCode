'''
求 1+2+...+n ，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）。

示例 1：

输入: n = 3
输出: 6
示例 2：

输入: n = 9
输出: 45
 

限制：

1 <= n <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/qiu-12n-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def num(self, n):
        # return (1 + n) * n / 2
        a = 1
        b = 0
        while a <= n:
            b += a
            a += 1
        return b


if __name__ == "__main__":
    a = Solution()
    print(int(a.num(3)))
