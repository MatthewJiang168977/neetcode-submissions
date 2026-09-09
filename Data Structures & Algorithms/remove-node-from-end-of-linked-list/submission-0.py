# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # nodes = [] 
        # curr = head
        # while curr: 
        #     nodes.append(curr )
        #     curr = curr.next

        # remove = len(nodes)-n
        # if remove == 0: 
        #     return head.next

        # nodes[remove-1].next = nodes[remove].next
        # return head

        dum = ListNode(0,head)  
        l = dum  
        r = head 
        while n > 0: 
            r = r.next 
            n -= 1 

        while r: 
            l = l.next 
            r = r.next 

        l.next = l.next.next
        return dum.next
