# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        arr = []

        while head != None:
            arr.append(head.val)
            head = head.next
        
        del arr[len(arr) - n]

        if not len(arr): return None

        node = ListNode(arr[0])
        head = node

        for i in range(1, len(arr)):
            head.next = ListNode(arr[i])
            head = head.next

        return node


class Solution2:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        arr = []
        node = head

        while head != None:
            arr.append(head)
            head = head.next
        
        pos = len(arr) - n

        if not pos:
            if len(arr) > 1: 
                return arr[pos + 1]
            else:
                return None

        prev_pos = pos - 1 if (pos - 1 >= 0) else 0
        next_pos = pos + 1 if (pos + 1 < len(arr)) else None
        
        if next_pos:
            arr[prev_pos].next = arr[next_pos]
        else:
            arr[prev_pos].next = None

        node = arr[0]
        
        return node

a = ListNode(1)
b = ListNode(2)
# c = ListNode(3)
# d = ListNode(4)
# e = ListNode(5)
a.next = b
# b.next = c
# c.next = d
# d.next = e


solution = Solution2()
result = solution.removeNthFromEnd(a, 2)

while result:
    print(result.val)
    result = result.next