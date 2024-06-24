def minimumWaitingTime(queries):
    # Write your code here.
    if len(queries) == 0 or len(queries)==1:
        return 0
    querySort = sorted(queries)
    waitTime = 0
    totalTime = 0
    for i in range(len(querySort)-1):
        waitTime = waitTime + querySort[i]
        totalTime += waitTime
    return totalTime

print(minimumWaitingTime([3, 2, 1, 2, 6]))