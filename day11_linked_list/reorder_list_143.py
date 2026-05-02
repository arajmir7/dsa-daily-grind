class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        if not head or not head.next:
            return

        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        curr = slow.next
        slow.next = None 
        
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first = head
        second = prev
        
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
        
            first = temp1
            second = temp2

def create_list(arr): # create linked list
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_list(head): # Helper: print list
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    head = create_list(arr)
    sol = Solution()
    sol.reorderList(head)
    print("Reordered List:")
    print_list(head)