class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 创建一个链表
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

current = head
while current:
    print(current.data)
    current = current.next
