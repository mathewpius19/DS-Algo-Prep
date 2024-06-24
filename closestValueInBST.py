#Avg:O(log(N)) Time | O(log(N)) space
#Worst:O(N) Time | O(N) space
#Recursive approach
def findClosestValueInBST(tree, target):
    return findClosestValueInBSTHelper(tree,target, float("inf"))


def findClosestValueInBSTHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target-closest)> abs(target-tree.value):
        closest = tree.value
    
    if tree.value>target:
        return findClosestValueInBSTHelper(tree.left, target, closest)
    elif tree.value<target:
        return findClosestValueInBSTHelper(tree.right, target, closest)
    else:
        return closest

#Avg:O(log(N)) Time | O(1) space
#Worst:O(N) Time | O(1) space
#Iterative
def findClosestValueInBSTHelper1(tree, target,closest):
    return findClosestValueInBSTIterative(tree,target,float("inf"))

def findClosestValueInBSTIterative(tree,target,closest):
    currentNode = tree
    while currentNode is not None:
        if abs(target-closest) > abs(target-currentNode):
            closest = currentNode.value
        if currentNode.value<target:
            currentNode = currentNode.right
        elif currentNode.value>target:
            currentNode = currentNode.left
        else:
            break
    return closest

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
