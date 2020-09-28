class Solution:
    """
        Using Stack O(n)
    """
    open_p = ['(', '[', '{']
    close_p = [')', ']', '}']
    
    def isValid(self, s: str) -> bool:
        if not len(s): return True
        
        if len(s) % 2 != 0: return False

        i = 0
        stack = []
        while i < len(s):
            if s[i] in self.open_p:
                stack.append(s[i])
                i += 1
            elif not len(stack): 
                return False 
            else:
                last_item_in_stack = stack[-1]
                pairs = list(zip(self.open_p, self.close_p))
                if (last_item_in_stack, s[i]) not in pairs:
                    return False
                stack.pop()
                i += 1

        if not len(stack): return True 
                
        return False

#tc = "(([]){})"
tc = "(]"
# solution = Solution()
# result = solution.isValid(tc)
# print(result)


'''Better format but still using the same approach is Stack'''
class Solution2:
    def isValid(self, s: str) -> bool:
        stack = []

        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            ''' # is a dummy element '''
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack

#tc = "(([]){})"
tc = "(((((("
solution = Solution2()
result = solution.isValid(tc)
print(result)