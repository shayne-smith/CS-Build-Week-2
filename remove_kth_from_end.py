# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def remove_kth_from_end(head, k):
    
    # special cases
    if k == 0:
        return head
    
    current = head
    nodeArray = []
    
    # iterate through linked list starting at head node
    while current.next != None:

        # add each node to array until self.next is null
        nodeArray.append(current)
        
        # increment current
        current = current.next
    
    # add last node to array
    nodeArray.append(current)
    
    # if length of array is shorter than k
    if len(nodeArray) < k:
        
        # return input head value
        return head
    else:
        
        # store kth node
        kthNode = nodeArray[-k]

        # special case
        if kthNode.value == head.value:
            return kthNode.next
        
        # update current node back to head
        current = head
        print(kthNode.value)
        print(current.value)
        
        # loop through linked list again starting at head until k-1th node is reached
        while current.next != kthNode:
            
            # increment current node
            current = current.next
        
        # change k-1th node next value to k+1th node
        current.next = kthNode.next
        
        # return kth node
        return head

head = ListNode(100)
head.next = ListNode(200)

print(remove_kth_from_end(head, 2))