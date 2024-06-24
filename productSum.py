#O(N) Time n is the number of elements in the array
#O(d) Space, where d is the greatest depth of "special arrays" in the array

def productSum(array, depth=1):
    sum = 0
    for ele in array:
        if type(ele)==list:
            sum+= productSum(ele,depth+1)
        else:
            sum+=ele
    return depth*(sum)
print(productSum([5, 2, [7, -1], 3, [6, [-13, 8], 4]]))

