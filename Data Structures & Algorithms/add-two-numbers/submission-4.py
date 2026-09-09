# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        temp = head
        l1Sum = 0 
        l2Sum = 0 
        power = 0
        while l1: 
            l1Sum += l1.val * (10 ** power)
            power += 1 
            l1 = l1.next
        power = 0 
        while l2: 
            l2Sum += l2.val * (10 ** power)
            power += 1 
            l2 = l2.next 

        Tsum = l1Sum+l2Sum
        for i in range(len(str(Tsum))-1,-1,-1): 
            temp.next = ListNode(int(str(Tsum)[i]),None)
            temp = temp.next
        return head.next
        


        # while l1 and l2: 
        #     twosum = l1.val+l2.val
        #     if twosum < 10: 
        #         temp.next = ListNode(twosum,temp.next)
        #     else: 
        #         for i in range(len(str(twosum))-1,-1,-1):
        #             print(str(twosum)[i], end=" ")
        #             temp.next = ListNode(str(twosum)[i],temp.next)
        #             # temp = temp.next
        #     l1 = l1.next 
        #     l2 = l2.next 
        #     temp = temp.next 

        # if l1: 
        #     temp.next = l1 
        # if l2: 
        #     temp.next = l2
        # return head.next  
