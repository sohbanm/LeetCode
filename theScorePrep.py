# games = [ 
#   { "teamA" : 123, "teamB": 321, "winner": "teamB"},
#   { "teamA" : 123, "teamB": 31, "winner": "teamA"},
#   { "teamA" : 123, "teamB": 321},
# ]

# # 1. number of matches for each team
# matchesPlayed = {}

# for game in games:
#     for detail in game:
#         if detail != "winner":
#             matchesPlayed[game[detail]] = matchesPlayed.get(game[detail], 0) + 1

# print(matchesPlayed)

# # 2. Win percentage of each team
# winRecord = {}

# for game in games:
#     if "winner" in game:
#         if game["winner"] == "teamA":
#             winRecord[game["teamA"]] = winRecord.get(game["teamA"], 0) + 1
#         elif game["winner"] == "teamB":
#             winRecord[game["teamB"]] = winRecord.get(game["teamB"], 0) + 1

# teamWinRate = {}

# for team in matchesPlayed:
#     teamWinRate[team] = winRecord.get(team, 0) / matchesPlayed[team]

# print(teamWinRate)

data = [
    {"bob": {"timePlayed":21, "scoreMade":150}},
    {"joe": {"timePlayed":15, "scoreMade":120}},
    {"moe": {"timePlayed":2, "scoreMade":90}}
]

sorted_data = sorted(data, key=lambda x: list(x.values())[0]['timePlayed'])


print(data)
print(sorted_data)
# for player in data:
#     for name, stats in player.items():
#         print(name)
#         print(stats)

# for player in sorted_data:
#     for name, stats in player.items():
#         print(name)
#         print(stats)

# # test = [ list(x) for x in data]
# test = data.sort(key=lambda x:x["timePlayed"])

# print(test)

