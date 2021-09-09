#Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside 
#the signed 32-bit integer range [-231, 231 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        output = 0
        
        if x < 0:
            negative = -1
            x = x * -1
        else:
            negative = 1
        while x:
            output = output * 10 + x % 10
            x = x // 10
        
        if negative == -1:
            output *= -1
        
        if output > 2 ** 31 -1 or output < - 2 **31:
            output = 0
        
        return output

