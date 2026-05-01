class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next   
            curr.next = prev     
            prev = curr             
            curr = next_node       
        return prev

def create_linked_list(arr):
    head = ListNode(arr[0])
    temp = head
    
    for i in range(1, len(arr)):
        temp.next = ListNode(arr[i])
        temp = temp.next
    
    return head

def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    head = create_linked_list(arr)
    print("Original List:")
    print_linked_list(head)
    sol = Solution()
    new_head = sol.reverseList(head)
    print("Reversed List:")
    print_linked_list(new_head)