class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if head == None:
            return None
        ele = set()
        ele_l = []
        while head != None:
            if head.val not in ele:
                ele.add(head.val)
                ele_l.append(head.val)
            head = head.next
        node = ListNode(val = ele_l[0])
        if len(ele_l) == 1:
            return node

        ret = node
        for i in ele_l[1:]:
            node.next = ListNode(val=i)
            node = node.next
        return ret

