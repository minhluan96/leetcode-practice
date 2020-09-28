class Solution:
    def findDuplicate(self, nums) -> int:
        slow = nums[0]
        fast = nums[0]

        '''
        We will find the entrance when two pointer is met, which doesn't mean it has to be a duplicated number
        The entrance could be a position that 2 pointers will eventually meet and pointed out that will begin the cycle loop
        2 * slow = fast (1)
        Called the distance from the duplicated number to the intersection is "a"
        - The distance from the begining to the duplicated number is the "F"
        - The distance from duplicated number to the duplicated number (whole cycle) is "C"
        - The times that the fast pointer ran through the loop is "n"
        
        From (1) => 2 * (F + a) = F + nC + a
        <=> 2F + 2a = F + nC + a
        <=> F + a = nC

        So we will find the entrance from the first loop
        '''
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        
        '''
        So we still want to find the duplicated number, 
        - If the slow start from the begining (0), after F steps, it will be 0 + F = F steps
        - If the fast start from the intersection (F + a), after F steps, it will be [(F + a) or nC] + F steps
        The nC is n times of a whole loop which we could consider it ~ 0 since it will get back to the first position from the loop
        => If we eliminate the nC times, which mean we slow down the fast pointer. 
        So now the fast pointer will have the value as the same pointer.

        Why we need "after F steps"
        - Because the duplicated number is found after F steps.
        '''
        slow = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]

        return slow

nums = [1,3,4,2,2]
solution = Solution()
result = solution.findDuplicate(nums)
print(result)



        