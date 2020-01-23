#from: https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):

        tempHead = ListNode(0)
        node = tempHead #create a false list head to keep track of head of results list

        carry = False #init carry to false

        while l1 != None or l2 != None: #traverse while we have none Null values

            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0 #get vals from l1 and l2
            val3 = 0

            if carry == True:
                val3 = 1 #val3 will be 0 unless we need to carry

            sum = val1 + val2 + val3
            node.next = ListNode(sum % 10) #assign next node to current sum

            #if the sum just found was > 9
            #then we will need to set val3 to 1 on the next iteration
            if sum > 9:
                carry = True
            else:
                carry = False

            l1 = l1.next if l1 != None else None
            l2 = l2.next if l2 != None else None
            node = node.next #move along all linked lists

        #outside the while loop check for one more carry at the very end
        if carry == True:
            node.next = ListNode(1)

        return tempHead.next #return the node next to the dummy head

'''some edge cases to consider:
[5]
[5]   -> [0,1]

[1,8]
[0]   -> [1,8]
'''
