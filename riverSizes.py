def riverSizes(matrix):
    visited = [[False for value in row] for row in (matrix)]
    sizes = []
    rows = len(matrix)
    for i in range(rows):
        for j in range(len(matrix[i])):
            if visited[i][j]:
                continue
            traverseNode(visited, matrix, i, j, sizes)

    return sizes


def traverseNode(visited, matrix, i, j, sizes):
    currentRiverSize = 0
    nodesToExplore = [[i, j]]
    while len(nodesToExplore):
        currentNode = nodesToExplore.pop()
        i = currentNode[0]
        j = currentNode[1]
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        currentRiverSize += 1
        unvisitedNeighbours = getUnvisitedNeighbours(matrix, visited, i, j)
        for node in unvisitedNeighbours:
            nodesToExplore.append(node)
    if currentRiverSize > 0:
        sizes.append(currentRiverSize)


def getUnvisitedNeighbours(matrix, visited, i, j):
    unvisited_nodes = []
    if i > 0 and not visited[i - 1][j]:
        unvisited_nodes.append([i - 1, j])
    if i < len(matrix) - 1 and not visited[i + 1][j]:
        unvisited_nodes.append([i + 1, j])

    if j > 0 and not visited[i][j - 1]:
        unvisited_nodes.append([i, j - 1])
    if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
        unvisited_nodes.append([i, j + 1])

    return unvisited_nodes


print(
    riverSizes(
        [
            [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
            [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
        ]
    )
)
