class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# TODO: HS: 3.5.2024
# To return linked list in ascending order instead of list

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        merged_list = []
        next = list1
        while next:
            merged_list.append(next.val)
            next = next.next
        next_two = list2
        while next_two:
            merged_list.append(next_two.val)
            next_two = next_two.next
        merged_list.sort()
        return merged_list


list1 = ListNode(1, ListNode(2, ListNode(3, None)))
list2 = ListNode(1, ListNode(3, ListNode(4, 0)))

result = Solution().mergeTwoLists(list1, list2)
