# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(None)
        curr = head
        queue = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(queue, (lists[i].val,i))
                lists[i] = lists[i].next

        while queue:
            val, i = heapq.heappop(queue)
            curr.next = ListNode(val)
            curr = curr.next
            if lists[i]:
                heapq.heappush(queue, (lists[i].val, i))
                lists[i] = lists[i].next

        return head.next                