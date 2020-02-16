#from: https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):

        if l1 != None and l2 == None:
            return l1 #only l2 is 'None'
        elif l1 == None and l2 != None:
            return l2 #only l1 is 'None'
        elif l1 == None and l2 == None:
            return l1 #they're both 'None'

        resultHead = l1

        nxt = l1
        comp = l2 #the compare node
        prev = None

        while comp != None:
            if nxt.val <= comp.val and nxt.next == None:
                nxt.next = comp
                break

            if nxt.val > comp.val:
                l2_next = comp.next
                comp.next = nxt #reassign comp.next

                if prev == None:
                    resultHead = comp #reassign the head
                    prev = comp
                    nxt = comp.next #reassign pointers
                    comp = l2_next

                else: # if prev != None:
                    prev.next = comp
                    prev = comp
                    nxt = comp.next
                    comp = l2_next

            else:
                prev = nxt
                nxt = nxt.next

        return resultHead
