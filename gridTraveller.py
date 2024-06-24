def gridTraveller(m, n, memo={}):
    key = str(m) + "," + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = gridTraveller(m - 1, n, memo) + gridTraveller(m, n - 1, memo)
    return memo[key]


print(gridTraveller(4, 3))


def gridTravellerTab(m, n):
    arr = [[0 for x in range(m + 1)] for x in range(n + 1)]
    arr[1][1] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            current = arr[i][j]
            if j + 1 <= n:
                arr[i][j + 1] += current
            if i + 1 <= m:
                arr[i + 1][j] += current
    return arr[m][n]


print(gridTravellerTab(2, 3))
