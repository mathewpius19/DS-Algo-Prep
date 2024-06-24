def maxMatrixSum(mat):
    rows = len(mat)
    cols = len(mat[0])
    sum = 0
    count = 0
    small = float("inf")
    for i in range(rows):
        for j in range(cols):
            current = mat[i][j]
            small = min(small, abs(current))
            if current < 0:
                count += 1
            sum += abs(current)
    return sum if count % 2 == 0 else sum - (2 * small)


print(maxMatrixSum([[1, 2, 3], [-4, -5, -6], [1, 2, 3]]))
