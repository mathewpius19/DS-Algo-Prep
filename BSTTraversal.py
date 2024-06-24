def inOrder(tree, array):
    if tree is not None:
        inOrder(tree.left, array)
        array.append(tree.value)
        inOrder(tree.right, array)
    return array


def preOrder(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrder(tree.left, array)
        preOrder(tree.right, array)
    return array


def postOrder(tree, array):
    if tree is not None:
        postOrder(array.left, array)
        postOrder(array.right, array)
        array.append(tree.value)
    return array
