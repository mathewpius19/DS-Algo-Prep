# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    # Write your code here.
    node = head
    count = 0
    if k is None:
        return
    while node is not None:
        count += 1
        node = node.next

    headNode = head.next
    if count - k == 0:
        head.value = headNode.value
        head.next = headNode.next
        return

    removeNode = head
    removeValue = 0
    for i in range((count - k)):
        removeNode = removeNode.next
    removeValue = removeNode.value

    prev = head
    currentNode = prev.next
    while currentNode is not None:
        if currentNode.value == removeValue:
            prev.next = currentNode.next
        currentNode = currentNode.next
        prev = prev.next

    return
