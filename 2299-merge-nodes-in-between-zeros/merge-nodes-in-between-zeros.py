# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        result = []
        sum = 0
        while head:
            if head.val == 0:
                if sum != 0: result.append(ListNode(sum))
                sum = 0
            sum += head.val
            head = head.next
        if sum != 0:
            result.append(ListNode(sum))
        for i in range(1,len(result)):
            result[i-1].next = result[i]
        
        return result[0]
        