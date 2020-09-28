class Solution:
    def singleNumber(self, nums) -> int:
        '''
        Using dictionary, space complextity: O(n), time complexity O(n)
        '''
        nmap = dict()

        for n in nums:
            if n in nmap:
                nmap[n] += 1
            else:
                nmap[n] = 1

        return list(nmap.keys())[list(nmap.values()).index(1)]


class Solution2:

    '''
        If we take XOR of zero and some bit, it will return that bit
            a ⊕ 0 = a
            If we take XOR of two same bits, it will return 0
            a ⊕ a = 0
            a ⊕ b ⊕ a = (a ⊕ a) ⊕ b = 0 ⊕ b = b
            So we can XOR all bits together to find the unique number.
    '''
    def singleNumber(self, nums) -> int:
        a = 0
        for n in nums:
            a ^= n
        return a


tc = [4,1,2,1,2]
solution = Solution2()
result = solution.singleNumber(tc)
print(result)