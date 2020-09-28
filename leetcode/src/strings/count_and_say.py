class Solution:
    def countAndSay(self, n: int) -> str:
        if not n: return ''
        if n == 1: return '1'
        return self.execute('1', n - 1)
        

    def execute(self, string, n):
        if not n:
            return string

        queue_node = []

        matched = []
        
        for s in string:
            if s not in matched:
                if len(matched):
                    matched.pop()
                matched.append(s)
                node = Node(s)
                queue_node.append(node)
            else:
                last_node = queue_node.pop()
                last_node.increase_frequency()
                queue_node.append(node)

        result = ''
        for node in queue_node:
           result += str(node)
        
        return self.execute(result, n - 1)

class Node:
    frequency = 1
    
    def __init__(self, value):
        self.value = value

    def increase_frequency(self):
        self.frequency += 1

    def __str__(self):
        return '{}{}'.format(self.frequency, self.value)


# 1121
# ~> 211211

solution = Solution()
result = solution.countAndSay(4)
print(result)