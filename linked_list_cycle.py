# use two points with one going at twice the speed of the other
# if they eventually coincide, there's a loop

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_point = slow_point = head
        while fast_point is not None and fast_point.next is not None:
            slow_point = slow_point.next
            fast_point = fast_point.next.next

            if fast_point == slow_point:
                return True
        return False    