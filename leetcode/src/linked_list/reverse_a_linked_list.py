# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        Using iteration
        Time complexity O(n)
        Space complexity O(n)
        '''
        if not head: return None

        arr = []
        while head != None:
            arr.append(head.val)
            head = head.next
        
        end = len(arr) - 1
        current = ListNode(arr[end])
        node = current
        
        for i in range(end - 1, -1, -1):
            node.next = ListNode(arr[i])
            node = node.next
        
        return current

class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
        Using recursive
        Time Complexity O(n)
        Space complexity O(n)
        '''
        
        if head == None or head.next == None:
            return head

        '''
            The node here to idicate that it is the last node and it will be the new head
        '''
        reversed_list_head = self.reverseList(head.next)
        
        '''
        After the iteration 3: the node is 3
        After the iteration 2: the node still 3 (because we return the node at the end of the 3rd iteration)
        '''

        '''
        Assign the head to the last node
        Ex:
        1 - 2 - 3 -> None
        after the recursion above, we are in the last node is 3, and the head is 2
        currently
            2 -> next -> next = None
            2 -> next = 3
        the result is:
            the head is 2

            the head.next is equivalent to node
            so head.next = node ~> node.next = head
            
            2 -> next -> next = 2
            2 -> next = None
        which mean
            3 -> 2 -> None
        '''

        head.next.next = head
        head.next = None
        
        '''
            In the example above, the function will return the head node is 3
        '''

        return reversed_list_head

class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        '''
            Not using a list
            Space complexity O(1)
            Time complexity O(n)
        '''

        prev = None
        current = head
        next_node = None

        while current != None:
            ''' Save the next node '''
            next_node = current.next 
            ''' Reverse the pointer '''
            current.next = prev
            ''' Increase the prev and current to the next node '''
            prev = current
            current = next_node

        ''' New head at the end '''
        return prev

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e

solution = Solution3()
result = solution.reverseList(a)

while result:
    print(result.val)
    result = result.next