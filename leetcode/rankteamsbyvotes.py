from collections import defaultdict

votes = ["ABC", "ACB", "ABC", "ACB", "ACB"]


def teams_win_by_votes(votes):
    if not votes:
        return None
    teams = votes[0]
    votes_count = defaultdict(int)
    for i in range(len(votes)):
        teams = votes[i]
        for j, team in enumerate(teams):
            votes_count[team] += j
    result = ''.join(sorted(votes_count, key=votes_count.get))
    return result


result = teams_win_by_votes(votes)
print(result)