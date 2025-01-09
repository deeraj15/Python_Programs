class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or(x%10==0 and x!=0):
            return False
        original=x
        reversednum=0
        while x>0:
            lastdigit=x%10
            reversednum=reversednum*10+lastdigit
            x=x//10
        return reversednum==original
