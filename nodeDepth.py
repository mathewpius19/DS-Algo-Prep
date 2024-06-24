# O(n) Time where n is number of nodes | O(h) Space where h is the height of tree 

def nodeDepths(root):
    # Write your code here.
	depthList = []
	result = calculateNodeDepth(root,1,depthList)
	return result
def calculateNodeDepth(node,count,depthList):
	if node.right is None and node.left is None: # if no child nodes depth is zero
		return 0
	if(node.left is not None):
		depthList.append(count)
		calculateNodeDepth(node.left, count+1, depthList) # count represents each level of the tree and as we go down the tree count is incremented
	if node.right is not None:
		depthList.append(count)
		calculateNodeDepth(node.right,count+1,depthList)
	return sum(depthList) # the sum of depths is returned as result