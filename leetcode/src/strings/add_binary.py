class Solution:
    def addBinary(self, a: str, b: str) -> str:
        remember = 0
        result = []
        len_a, len_b = len(a), len(b)

        while True:
            i = len_a - 1
            j = len_b - 1
            
            value_a = int(a[i]) if i >= 0 else 0
            value_b = int(b[j]) if j >= 0 else 0

            total = value_a + value_b + remember
            
            if total == 2: 
                total = 0
                remember = 1
            elif total > 2:
                remember = 1
                total = 1
            else:
                remember = 0

            len_a -= 1
            len_b -= 1

            if i < 0 and j < 0: 
                if total > 0:
                    result.append(total)
                break
            else:
                result.append(total)

        result.reverse()
        return ''.join(str(x) for x in result)


a = '1111'
b = '1111'
# solution = Solution()
# result = solution.addBinary(a, b)
# print(result)


            
# OPTIMIZE SOLUTIONS

class Solution2:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        s = []

        while i >= 0 or j >= 0:
            total = carry
            
            if j >= 0: total += int(b[j])
            if i >= 0: total += int(a[i])
            s.append(int(total % 2))
            carry = int(total / 2)

            i -= 1
            j -= 1

        if carry: s.append(carry)
        s.reverse()

        return ''.join(''.join(str(x) for x in s))

a = '1111'
b = '1111'
solution = Solution2()
result = solution.addBinary(a, b)
print(result)

# RECURSIVE SOLUTION

class Solution3:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0: return b
        if len(b) == 0: return a

        if a[-1] == '1' and b[-1] == '1':
            return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
        if a[-1] == '0' and b[-1] == '0':
            return self.addBinary(a[0:-1], b[0:-1]) + '0'
        else:
            return self.addBinary(a[0:-1], b[0:-1]) + '1'

a = '1111'
b = '1111'
solution = Solution3()
result = solution.addBinary(a, b)
print(result)