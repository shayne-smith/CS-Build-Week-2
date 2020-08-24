# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # extract integers from both singly-linked lists
        # start with empty string
        s1 = s2 = ""
        
        # join each list node value to existing string
        while l1 is not None:    
            s1 = str(l1.val) + s1
            print(l1.val)
            l1 = l1.next
        while l2 is not None:
            s2 = str(l2.val) + s2
            print(l2.val)
            l2 = l2.next
        
        print(f"s1: {s1}")
        print(f"s2: {s2}")
            
        # convert strings to ints
        n1 = int(s1)
        n2 = int(s2)
        
        # add both integers
        sum = n1 + n2
        
        print(f"sum: {sum}")
        
        # store integer as a linked list in reverse order
        # convert int to string to list of chars from string
        digitList = [int(c) for c in str(sum)]
        
        print(f"digitList: {digitList}")
        
        def buildLL(self, digitList):
            # build singly-linked list of sum in reverse order
            head = ListNode(digitList.pop(0))
            
            while len(digitList) > 0:
                prev_node = head # 0
                
                new_node = ListNode(digitList.pop(0)) # 7
                
                new_node.next = prev_node # 7 -> 0 -> 8
                head = new_node # 7
            
            return head
        
        return buildLL(self, digitList)