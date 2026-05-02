class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):  
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy

        for _ in range(n):
            fast = fast.next
      
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next

def create_linked_list(arr):
    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next

    return head

def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

if __name__ == "__main__":
    arr = [2,3,4,4,6,7,8]
    n = 5
    head = create_linked_list(arr)
    sol = Solution()
    new_head = sol.removeNthFromEnd(head, n)
    print("After removing nth node from end:")
    print_list(new_head)