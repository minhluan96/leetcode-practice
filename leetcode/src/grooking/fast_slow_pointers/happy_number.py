class Solution:
    def sumDigits(self, n):
        s = str(n)
        total = 0
        for i in range(len(s)):
            total += pow(int(s[i]), 2)
        return total

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.sumDigits(n)

        while fast != slow and fast != 1:
            slow = self.sumDigits(slow)
            fast = self.sumDigits(self.sumDigits(fast))
        
        return fast == 1 or not fast == slow

n = 12
solution = Solution()
result = solution.isHappy(n)
print(result)