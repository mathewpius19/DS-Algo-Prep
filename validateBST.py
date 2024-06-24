# O(N) Time | O(d) space where d is depth of the tree
def validateBST(tree):
    return validateBSTHelper(tree, float("-inf"), float("inf"))


def validateBSTHelper(tree, minValue, maxValue):
    if tree is None:
        return True
    if tree.value < minValue or tree.value >= maxValue:
        return False

    leftValid = validateBSTHelper(tree.left, minValue, tree.value)
    return leftValid and validateBSTHelper(tree.right, tree.value, maxValue)
