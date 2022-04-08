# inputs :
# competitions = [
#   ["HTML", "C#"],
#   ["C#", "Python"],
#   ["Python", "HTML"]
# ]
# result = [0,0,1]

TEAM_WINNING_SCORE = 1


def tournament_winner(competitions, results):
    current_best_team = ""
    scores = {current_best_team: 0}

    for idx, competition in enumerate(competitions):
        result = results[idx]
        home_team, away_team = competition
        winning_team = home_team if result == TEAM_WINNING_SCORE else away_team
        update_score(winning_team, 3, scores)
        if scores[winning_team] > scores[current_best_team]:
            current_best_team = winning_team
    return current_best_team


def update_score(team, points, scores):
    if team not in scores:
        scores[team] = 0
    scores[team] += points


if __name__ == '__main__':
    competitions = [
        ["HTML", "C#"],
        ["C#", "Python"],
        ["Python", "HTML"]
    ]
    results = [0, 0, 1]

    winning_team = tournament_winner(competitions, results)
    print(f"winning team is: {winning_team}")
