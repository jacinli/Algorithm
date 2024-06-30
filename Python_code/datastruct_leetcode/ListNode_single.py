# 单向链表的创建

class ListNode:
    def __init__(self, val=0, node=None):
        self.val = val
        self.node = node

    def print_list(self):
        current = self
        list_node = []
        while current:
            list_node.append(current.val)
            current = current.node
        return list_node

    @staticmethod
    def create_list_node(val_list):
        """
        通过列表创建链表
        :param val_list: 列表
        :return: 链表
        """
        head = ListNode(val_list[0])
        current = head
        for i in range(1, len(val_list)):
            current.node = ListNode(val_list[i])
            current = current.node
        return head


if __name__ == '__main__':
    list_node1 = [1, 4, 5, 6, 98]
    head1 = ListNode.create_list_node(list_node1)
    print(head1.print_list())
