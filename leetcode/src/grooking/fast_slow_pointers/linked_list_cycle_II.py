class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        current = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                while slow is not current:
                    current = current.next
                    slow = slow.next

                return slow
        
        return None

a = ListNode(3)
b = ListNode(2)
c = ListNode(0)
d = ListNode(4)
a.next = b
b.next = c
c.next = d
d.next = b

solution = Solution()
result = solution.detectCycle(a)
print(result.val)
