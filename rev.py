class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        while x != 0:
            rem = x%10
            rev = rev*10 + rem
            x = x//10
        return rev
    
s = Solution()
print(s.reverse(-124560))