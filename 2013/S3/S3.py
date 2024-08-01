def processMatch(a, b, score_a, score_b, scores):
    if score_a > score_b:
        scores[a] += 3
    elif score_a == score_b:
        scores[a] += 1
        scores[b] += 1
    else:
        scores[b] += 3


def takeInput():
    favorateTeam = int(input())
    nMatchPlayed = int(input())
    games = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    scores = [-1, 0, 0, 0, 0]

    for i in range(nMatchPlayed):
        a, b, score_a, score_b = map(int, input().split())
        processMatch(a, b, score_a, score_b, scores)
        games.remove((a, b))  # a < b so no need to try (b, a)

    return favorateTeam, games, scores


def checkFavIsWinning(score, favorateTeam):
    isWinning = True
    for i in range(len(score)):
        if score[i] >= score[favorateTeam] and i != favorateTeam:
            isWinning = False
            break
    return isWinning


def chancesOfWinning(favorateTeam, games, score):
    if not games:
        if checkFavIsWinning(score, favorateTeam):
            return 1
        else:
            return 0
    win_possibilities = [(0, 3), (3, 0), (1, 1)]  # possible points gained for a game
    totalWins = 0
    a, b = games.pop()
    for a_points, b_points in win_possibilities:
        new_score = score.copy()
        new_score[a] += a_points
        new_score[b] += b_points
        totalWins += chancesOfWinning(favorateTeam, games.copy(), new_score)
    return totalWins


favorateTeam, games, score = takeInput()
print(chancesOfWinning(favorateTeam, games, score))