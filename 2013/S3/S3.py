favorite_team = int(input())
g = int(input())
points = {1:0,2:0,3:0,4:0}
games = {1:[],2:[],3:[],4:[]}
for i in range(g):
    teamA,teamB,scoreA,scoreB = list(map(int,input().split()))
    if scoreA > scoreB:
        points[teamA] += 3
    elif scoreA < scoreB:
        points[teamB] += 3
    else:
        points[teamB] += 1
        points[teamA] += 1
    games[teamB].append(teamA)
    games[teamA].append(teamB)
possible_out_come = (6 - g) * 3
all_combinations = [(i, j) for i in range(1, 5) for j in range(i + 1, 5)]
unplayed_games = [game for game in all_combinations if game[0] not in games[game[1]] and game[1] not in games[game[0]]]
print("Unplayed games:", unplayed_games)
new_point = points.copy()
games = [(1, 2), (3, 4)]

def calculate_points(game):
  teamA, teamB = game
  winner = input(f"Result of {teamA} vs {teamB} (A win, B win, Tie): ").upper()
  if winner == 'A':
    return {teamA: 3, teamB: 0}
  elif winner == 'B':
    return {teamA: 0, teamB: 3}
  else:
    return {teamA: 1, teamB: 1}
def simulate_outcomes(games):
  all_outcomes = []
  for game in games:
    points = calculate_points(game)
    all_outcomes.append(points)
  return all_outcomes

simulated_outcomes = simulate_outcomes(unplayed_games)
print("Possible point outcomes:")
for outcome in simulated_outcomes:
  print(outcome)



