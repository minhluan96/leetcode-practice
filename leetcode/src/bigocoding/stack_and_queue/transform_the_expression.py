class Solution:
    def transformTheExpression(self, t, expressions):
        stack = []
        results = []

        for i in range(t):
            newString = '' 
            expression = expressions[i]

            for c in expression:
                if c.isalpha():
                    newString += c
                elif c == ')':
                    value = stack.pop()
                    newString += value
                elif c != '(':
                    stack.append(c)

            results.append(newString)


        return results

t = int(input())
expressions = []
for i in range(t):
    string = input()
    expressions.append(string) 

# expressions = [
# '(a+(b*c))',
# '((a+b)*(z+x))',
# '((a+t)*((b+(a+c))^(c+d)))',
# ]

solution = Solution()
result = solution.transformTheExpression(t, expressions)
for ans in result:
    print(ans)
                