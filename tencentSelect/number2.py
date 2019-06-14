'''
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def reverse(self, x):
        self.new_x = str(x)[::-1]
        if self.new_x[0] == '0':
            list_new_x = list(self.new_x)
            list_new_x.remove('0')
            self.new_x = ''.join(list_new_x)
            return int(self.new_x)

        elif '-' in self.new_x:
            list_new_x = list(self.new_x)
            list_new_x.remove('-')
            self.new_x = '-' + ''.join(list_new_x)
            return int(self.new_x)

        else:
            return int(self.new_x)

a = Solution()
print(a.reverse(123))
