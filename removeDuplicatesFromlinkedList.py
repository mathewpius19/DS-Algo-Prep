# O(N) Time | O(1) Space
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
	currentNode = linkedList
	while currentNode is not None:
		nextDistinctNode = currentNode.next
		while nextDistinctNode is not None and currentNode.value == nextDistinctNode.value:
			nextDistinctNode = nextDistinctNode.next
		currentNode.next = nextDistinctNode
		currentNode = nextDistinctNode
	return linkedList
