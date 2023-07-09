class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def l2n(node: ListNode):
    sum = ""
    while node.next != None:
        sum += str(node.val)
        node = node.next
    sum += str(node.val)
    return sum[::-1]

def n2l(s: str):
    s = s[::-1]
    node = ListNode(int(s[0]))
    res = node
    for i in range(1, len(s)):
        node.next = ListNode(int(s[i]))
        node = node.next
    return res

def twoAdd(l1: ListNode, l2: ListNode) -> ListNode:
    s1 = l2n(l1)
    s2 = l2n(l2)
    sum = str(int(s1) + int(s2))
    return n2l(sum)


l1_1 = ListNode(8)
l1_2 = ListNode(9)
l1_3 = ListNode(7)
l1_4 = ListNode(5)

l2_1 = ListNode(3)
l2_2 = ListNode(8)
l2_3 = ListNode(9)
l2_4 = ListNode(9)
l2_5 = ListNode(9)

l1_1.next = l1_2
l1_2.next = l1_3
l1_3.next = l1_4

l2_1.next = l2_2
l2_2.next = l2_3
l2_3.next = l2_4
l2_4.next = l2_5

print(twoAdd(l1_1, l2_1))
print(l2n(twoAdd(l1_1, l2_1)))
