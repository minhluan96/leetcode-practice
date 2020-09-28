class Solution:

    def array(self, s, t):
        return sorted(s) == sorted(t)

    def automaton(self, s, t):
        j = 0
        for i in range(len(s)):
            if j == len(t): 
                break
            if s[i] == t[j]:
                j += 1
        
        return j == len(t)
    
    def both(self, s, t):
        for i in range(len(t)):
            if s.find(t[i]) == -1:
                return False

        return True

    def suffix_structures(self, s, t):
        if self.array(s, t):
            return 'array'
        elif self.automaton(s, t):
            return 'automaton'
        elif self.both(s, t):
            return 'both'
        else:
            return 'need tree'


        


        


s = 'bvoczualgnsktwmfivbztaovhjmdjqkpyuhlyaigrpzhfnemepaqkhijjaybjjzwsxgjmsdohysjbxqzkjgntinitk'
t = 'voczualgsktwmfivbztaovhjmdjqkpyuhlyaigrpzhfnemepaqkhijjaybjjzwsxgjmsdohysjbxqzkjgntinitk'

# s = 'hdastwecjvtvnkzdyjnmxrdrroxbgmipicyvttofnrznzupmxulkjkkwhdpuztccmagvyzzmrfokizoxeyicefezldjzpgx'
# t = 'edteydtfmoljkcrwijmzuytdfzehpvabynnrokoplzidikzknervpjxmvucagcxtzjroxwgsrmupzdtmyznzhxcif'

# s = 'igvexeiswahnrjbbcvovwbhvkiryermvrytrpqhbmcwaypzhgjuxkwqiubjqnvpwslvdxdmyxqomckofzheqijdyngiweedr'
# t = 'igvxeiswahnrjbbvvwbvkiryermvrytrpqhbmcwaypzhgjuxkwqiubjqnvpwslvdxdmyxqomckofzheqijdyngiweedr'

# s = 'automaton'
# t = 'tomat'

s = 'both'
t = 'hot'

# s = input()
# t = input()
solution = Solution()
result = solution.suffix_structures(s, t)
print(result)