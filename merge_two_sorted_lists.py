class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        traveller = dummy = ListNode()
        
        while list1 and list2:
            if list1.val >= list2.val:
                traveller.next = list2
                list2 = list2.next
            else :
                traveller.next = list1
                list1 = list1.next
            traveller = traveller.next    

        if list1: 
            traveller.next = list1
        if list2:
            traveller.next = list2

        return dummy.next  