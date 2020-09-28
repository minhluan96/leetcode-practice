class Solution:
    def massOfMolecule(self, molecule):
        stack = []

        mapMolecule = { 'C': 12, 'H': 1, 'O': 16 } 

        for c in molecule:
            if c == '(':
                stack.append(c)
            elif c == ')':
                totalStack = 0
                currentStackValue = ')'

                while currentStackValue != '(':
                    currentStackValue = stack.pop()
                    if currentStackValue != '(':
                        totalStack += currentStackValue
                    
                stack.append(totalStack)
            elif c in mapMolecule:
                stack.append(mapMolecule[c])

            elif c.isnumeric():
                value = stack.pop()
                stack.append(value * int(c))
            

        return sum(stack)

s = input()
solution = Solution()
result = solution.massOfMolecule(s)
print(result)

                
                