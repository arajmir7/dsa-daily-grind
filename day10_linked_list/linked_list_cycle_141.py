class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class Solution:
    def hasCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next       
            fast = fast.next.next     

            if slow == fast:
                return True

        return False

def create_linked_list(arr):  # Helper function to create linked list
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head

    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def create_cycle(head, pos):  # Helper function to create cycle
    if pos == -1:
        return head

    cycle_node = None
    current = head
    index = 0

    while current.next:
        if index == pos:
            cycle_node = current
        current = current.next
        index += 1

    current.next = cycle_node  # create cycle
    return head
if __name__ == "__main__":
    arr = [3, 2, 0, -4]
    head = create_linked_list(arr)
    head = create_cycle(head, 1)
    sol = Solution()
    result = sol.hasCycle(head)
    print("Cycle exists:", result)