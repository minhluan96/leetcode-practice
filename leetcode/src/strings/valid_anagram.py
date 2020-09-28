class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''Using sort'''
        sorted_s = ''.join(sorted(s))
        sorted_t = ''.join(sorted(t))

        return sorted_s == sorted_t


    def isAnagramUsingCounter(self, s: str, t: str) -> bool:
        '''Using hashmap or array'''
        hmap = {}

        for c in s:
            if c in hmap:
                hmap[c] += 1
            else:
                hmap[c] = 1

        for c in t:
            if c in hmap:
                hmap[c] -= 1
            else:
                return False   
        
        for k, v in hmap.items():
            if v != 0:
                return False
        
        return True