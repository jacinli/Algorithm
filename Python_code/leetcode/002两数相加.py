# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


from typing import Optional

from datastruct_leetcode.ListNode_single import ListNode


# 思路：
#

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return None


if __name__ == '__main__':
    list_node1 = [3, 4, 2]
    head1 = ListNode.create_list_node(list_node1)
    list_node2 = [4, 6, 5]
    head2 = ListNode.create_list_node(list_node2)
    solution = Solution()
    #
    print(head1.print_list())
