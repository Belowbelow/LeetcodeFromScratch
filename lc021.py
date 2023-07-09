# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        r = []

        while list1.next != None and list2.next != None:
            if list1.val < list2.val:
                r.append(list1.val)
                list1 = list1.next
            else:
                r.append(list2.val)
                list2 = list2.next

        node = ListNode(r[0])
        ret = node
        for i in r[1:]:
            node.next = ListNode(i)
            node = node.next
        if list1.next == None and list2.next == None:
            return ret
        elif list1.next == None:
            node.next = list2
        elif list2.next == None:
            node.next = list1
        return ret

