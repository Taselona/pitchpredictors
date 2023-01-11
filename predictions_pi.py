# Store the list of users and their points
users = {}

# Get the predictions for each match from each user
for i in range(10):
    match = input("Enter the details of match " + str(i+1) + " (e.g. 'Team1 vs Team2 3-1'): ")
    for user in users:
        prediction = input("Enter your prediction for match " + str(i+1) + " (" + user + "): ")
        score, _, result = prediction.split(" ")
        team1, team2 = score.split("-")
        actual_score, _, actual_result = match.split(" ")
        actual_team1, actual_team2 = actual_score.split("-")
        if (team1 == actual_team1) and (team2 == actual_team2):
            users[user] += 3
        elif result == actual_result:
            users[user] += 1
        else:
            users[user] += 0

# Print the results for each user
for user in users:
    print(user + ": " + str(users[user]) + " points")
