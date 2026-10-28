# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        dummy = ListNode(0,head)

        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev,k) # (d,3)=3  (1,3)=6
            if not kth:
                break
            groupNext = kth.next

            # reverse 
            prev, curr = kth.next, groupPrev.next # 4,1  none,4
            while curr != groupNext: # 1  2  3  4:F  4  5 6 none
                temp = curr.next  # 2  3  4 |  5  6 none
                curr.next= prev  # 1->4  2->1  3->2 | 4-> none 5->4 6->5
                prev = curr  # 1  2  3 | 4 5 6
                curr = temp  # 2  3  4 | 5 6 none
             
            temp = groupPrev.next  # 1
            groupPrev.next = kth  # d->3
            groupPrev = temp  # 1

        return dummy.next

    def getKth(self,groupPrev,k):
        curr = groupPrev # d  1
        while curr and k > 0:  # 1 4 5 
            curr = curr.next  # 4 5 6
            k -= 1  # 2 1 0
        return curr  # 3 6

        