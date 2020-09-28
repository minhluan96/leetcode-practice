# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
        
        return False


a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = b

solution = Solution()
result = solution.hasCycle(a)
print(result)