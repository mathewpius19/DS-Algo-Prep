def tournamentWinner(competitions, results):
    # Write your code here.
    resultDict = {}
    for team in competitions:
        for value in team:
            if value not in resultDict:
                resultDict[value] = 0
            else:
                continue
    for i in range(len(competitions)):
        if results[i] == 0:
            resultDict[competitions[i][1]] += 3
        else:
            resultDict[competitions[i][0]] += 3

    largest = float("-inf")
    winner = ""
    for key, value in resultDict.items():
        if value > largest:
            largest = value
            winner = key

    return winner


print(
    tournamentWinner([["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]], [0, 0, 1])
)
