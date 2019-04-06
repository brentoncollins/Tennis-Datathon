df_winner = df.groupby('Winner').size()

try:
	player_1_wins = df_winner[players[0]]
except KeyError:
	player_1_wins = 0

try:
	player_2_wins = df_winner[players[1]]
except KeyError:

	player_2_wins = 0

total_games = int(player_1_wins) + int(player_2_wins)

players_this = [row['player_1'], row['player_2']]
a = (int(player_1_wins), int(player_2_wins))

index_high = int(a.index(max(a)))

wins_percentage = 100 * float(a[index_high]) / float(total_games)
wins_percentage_a = 100 * float(a[0]) / float(total_games) - 20



















found_match = False
matches_played = 0
matches_list = []
df = pandas.DataFrame(columns=['Winner', 'Looser', 'Winner_Games_Won', 'Loser_Games_Won', 'Winner_Rank', 'Loser_Rank'])

for index_match, row_match in df_matches.iterrows():
	# Loop threw all matches to find the same players in match
	match_players = (row_match['Winner'], row_match['Loser'])

	if set(players).issubset(match_players):
		# If a match can be found with the same players
		found_match = True
		matches_played += 1

		# Add the match winner and looser into the new data frame
		df.loc[-1] = [row_match['Winner'], row_match['Loser'], row_match['Winner_Games_Won'],
		              row_match['Loser_Games_Won'], row_match['Winner_Rank'], row_match['Loser_Rank']]
		df.index = df.index + 1
		df = df.sort_index()

		# Count the total number of matches played.
		matches_against = len(df.index)
try:
	print(df.groupby('Winner').size()[0])
except IndexError:
	print(df.groupby('Winner').min())
	continue

# values = df['Winner'].value_counts().keys().tolist()
# Get each value and put in a list

# try:
#	d = values.index(row['player_1'])
# except ValueError:
#	d = values.index(row['player_2'])

# Find the index for player 1 which we are looking for
# counts = df['Winner'].value_counts().tolist()
# Count the number of wins against the particular opponent
winner_1 = (int(df.groupby('Winner').size()[0]))

wins_percentage_overall = 100 * float(winner_1) / float(matches_against)
# Get the percentage of the wins, which is the first part of the odds.


# df.groupby(['Winner', "Winner_Games_Won"]).size().reset_index(name='counts')  )


# print (values)
with pandas.option_context('display.max_rows', None, 'display.max_columns', None):
	# print(df.loc[df['Winner'] == row['player_1']].sum())
	rank_primary = df.loc[df['Winner'] == row['player_1']].min()[-2]
	# print (rank_primary)
	won_primary = df.loc[df['Winner'] == row['player_1']].sum()[2]
	lost_primary = df.loc[df['Winner'] == row['player_1']].sum()[3]
	# print(won_primary,lost_primary)
	wins_percentage = float(won_primary) - float(lost_primary)

	print("{} won by a difference of of {} and has a top rank of {} when playing him".format(row['player_1'],
	                                                                                         wins_percentage,
	                                                                                         rank_primary))

	rank_secondary = df.loc[df['Winner'] == row['player_1']].min()[-1]
	won_secondary = df.loc[df['Winner'] == row['player_2']].sum()[2]
	lost_secondary = df.loc[df['Winner'] == row['player_2']].sum()[3]
	wins_percentage = float(won_secondary) - float(lost_secondary)
	print(won_secondary, lost_secondary)
	print("{} won by a difference of {} and has a top rank of {} when playing him".format(row['player_2'],
	                                                                                      wins_percentage,
	                                                                                      rank_secondary))

	# df = df.loc[df['Winner'] == row['player_2']].sum())

	# print(df.groupby('Winner').size()[0])

	# print(df)

	print("{} has a {}% Chance of winning".format(row['player_1'], wins_percentage_overall))


