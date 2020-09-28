class Solution:
    def vitaly_and_strings(self, s, t):
        length = len(s)
        pos = -1
        replace_char = ''

        for i in range(0, length):
            if s[i] != t[i]:
                pos = i
                break

        if pos == -1:
            return 'No such string'

        copied = s
        step = 1

        if s[-1] == 'z':
            copied = t
            step = -1

        replace_char = chr(ord(copied[-1]) + step)
        
        new_str = copied[:-1] + replace_char
        
        if new_str == t:
            return 'No such string'

        return new_str
        

s = input()
t = input()
solution = Solution()
result = solution.vitaly_and_strings(s, t)
print(result)                


'''
Bài sửa Psuedo code
'''
def fixSolution(s, t):
    for i in range(len(s), -1, -1):
        if s[i] != 'z':
            s[i] = chr(ord(s[i]) + 1)
            break 
        else:
            s[i] = 'a'
    
    if s == t:
        return 'No such string'
    
    return s

