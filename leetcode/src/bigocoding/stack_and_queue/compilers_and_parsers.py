class Solution:
    def compilersAndParsers(self, t, lines):
        results = []

        for i in range(t):
            line = lines[i]

            stack = []
            maxLength = 0

            for i in range(len(line)):
                c = line[i]
                if c == '<':
                    stack.append(c)
                else:
                    if not len(stack):
                        break

                    stack.pop()

                if len(stack) == 0:
                    maxLength = max(maxLength, i + 1)
                    
            
            results.append(maxLength)

        return results


t = int(input())
lines = []

for _ in range(t):
    lines.append(input())

solution = Solution()
result = solution.compilersAndParsers(t, lines)
for i in range(len(result)):
    print(result[i])