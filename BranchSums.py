def branchSums(root):
    sums=[]
    calculateBranchSums(root, 0, sums)
    return sums

def calculateBranchSums(node, runningSum, sums):
    if(node is None):
        return
    
    runningSum+=runningSum+node.value
    
    if(node.left is  None and node.right is None): # if end of branch then add to sums array
        sums.append(runningSum)
        return
    
    calculateBranchSums(node.left,runningSum,sums)# keep calling recursively on both left and right child nodes
    calculateBranchSums(node.right,runningSum,sums)