import pandas
import urllib2
from bs4 import BeautifulSoup


def generate_data_frame():
	# Isolate both players in a data frame to compare results regarding only the two playing each other.
	# Create new data frame
	df = pandas.DataFrame(
		columns=[
			'Winner', 'Looser', 'Tournament_Date',
			'Winner_Games_Won', 'Loser_Games_Won',
			'Winner_Rank', 'Loser_Rank',
			'Winner_Aces', 'Loser_Aces',
			'Winner_FirstServes_Won', 'Loser_FirstServes_Won',
			'Winner_DoubleFaults', 'Loser_DoubleFaults',
			'Winner_ReturnPoints_Won', 'Loser_ReturnPoints_Won',
			'Winner_BreakPoints_Won', 'Winner_BreakPoints'
		])

	# For each row in the ATP matches file if the Winner and Loser is in the match players add the row to the new frame
	for index_match, row_match in df_matches.iterrows():
		match_players = (row_match['Winner'], row_match['Loser'])
		if set(current_match_players).issubset(match_players):
			df.loc[-1] = [
				row_match['Winner'], row_match['Loser'], row_match['Tournament_Date'],
				row_match['Winner_Games_Won'], row_match['Loser_Games_Won'], row_match['Winner_Rank'],
				row_match['Loser_Rank'], row_match['Winner_Aces'], row_match['Loser_Aces'],
				row_match['Winner_FirstServes_Won'], row_match['Loser_FirstServes_Won'],
				row_match['Winner_DoubleFaults'], row_match['Loser_DoubleFaults'],
				row_match['Winner_ReturnPoints_Won'], row_match['Loser_ReturnPoints_Won'],
				row_match['Winner_BreakPoints_Won'], row_match['Winner_BreakPoints'],

			]

			df.index = df.index + 1
	df = df.sort_index()
	# Sort the index? Move inside loop?

	# Set the data types for the columns
	df['Winner_Aces'] = df['Winner_Aces'].replace('.', 0).astype(int)
	df['Loser_Aces'] = df['Loser_Aces'].replace('.', 0).astype(int)
	df['Winner_FirstServes_Won'] = df['Winner_FirstServes_Won'].replace('.', 0).astype(int)
	df['Loser_FirstServes_Won'] = df['Loser_FirstServes_Won'].replace('.', 0).astype(int)
	df['Winner_DoubleFaults'] = df['Winner_DoubleFaults'].replace('.', 0).astype(int)
	df['Loser_DoubleFaults'] = df['Loser_DoubleFaults'].replace('.', 0).astype(int)
	df['Winner_ReturnPoints_Won'] = df['Winner_ReturnPoints_Won'].replace('.', 0).astype(int)
	df['Loser_ReturnPoints_Won'] = df['Loser_ReturnPoints_Won'].replace('.', 0).astype(int)
	df['Winner_BreakPoints_Won'] = df['Winner_BreakPoints_Won'].replace('.', 0).astype(int)
	df['Winner_BreakPoints'] = df['Winner_BreakPoints'].replace('.', 0).astype(int)

	# Return the data frame
	return df


def elo_lookup():

	# Get the data frame
	df = df_matches
	#df = generate_data_frame()
	# Run the functions for comparing the data, may add more here.

	df['Winner_Aces'] = df['Winner_Aces'].replace('.', 0).astype(int)
	df['Loser_Aces'] = df['Loser_Aces'].replace('.', 0).astype(int)
	df['Winner_FirstServes_Won'] = df['Winner_FirstServes_Won'].replace('.', 0).astype(int)
	df['Loser_FirstServes_Won'] = df['Loser_FirstServes_Won'].replace('.', 0).astype(int)
	df['Winner_DoubleFaults'] = df['Winner_DoubleFaults'].replace('.', 0).astype(int)
	df['Loser_DoubleFaults'] = df['Loser_DoubleFaults'].replace('.', 0).astype(int)
	df['Winner_ReturnPoints_Won'] = df['Winner_ReturnPoints_Won'].replace('.', 0).astype(int)
	df['Loser_ReturnPoints_Won'] = df['Loser_ReturnPoints_Won'].replace('.', 0).astype(int)
	df['Winner_BreakPoints_Won'] = df['Winner_BreakPoints_Won'].replace('.', 0).astype(int)
	df['Winner_BreakPoints'] = df['Winner_BreakPoints'].replace('.', 0).astype(int)

	aces = compare_data(.1, 'Winner_Aces', 'Loser_Aces', df)
	winner_first_serve = compare_data(.1, 'Winner_FirstServes_Won', 'Loser_FirstServes_Won', df)
	winner_double_faults = compare_data(.1, 'Winner_DoubleFaults', 'Loser_DoubleFaults', df)
	winner_return_points_won = compare_data(.1, 'Winner_ReturnPoints_Won', 'Loser_ReturnPoints_Won', df)
	# Get both players results and compare
	winner0_break_points_points_won = break_points_won(0, 'Winner_BreakPoints_Won', 'Winner_BreakPoints', df)
	winner1_break_points_points_won = break_points_won(1, 'Winner_BreakPoints_Won', 'Winner_BreakPoints', df)
	# Get the percentage difference
	break_point_diff = percentage(.1, winner0_break_points_points_won, winner1_break_points_points_won)

	# Add all the changes
	changes = aces + winner_first_serve + winner_double_faults + winner_return_points_won + break_point_diff
	print(
		"Aces: {} \nWinner First Serve: {}\nWinner Double Faults: {}"
		"\nWinner Return Points Won: {}\nBreak Point Difference: {}".format(
			aces, winner_first_serve, winner_double_faults, winner_return_points_won, break_point_diff))

	# Set the default margin to .8? work on eliminating this.
	player_1_data = .8
	player_2_data = .8

	# For each player,value in the scraped list, if the split value in the ATP data is in the scraped key values
	# set the player_1_data to the elo value and the player_1_name to the scraped key value

	print (current_match_players[0])
	print (current_match_players[1])

	for key, value in item_list.items():
		if set(current_match_players[0].split(' ')).issubset(key.split(' ')):
			player_1_data = value[0]
			player_1_name = key
		else:
			if set(current_match_players[0].split(' ')[-1]).issubset(key.split(' ')):
				player_1_data = value[0]
				player_1_name = key

		if set(current_match_players[1].split(' ')).issubset(key.split(' ')):
			player_2_data = value[0]
			player_2_name = key
		else:
			if str(current_match_players[1].split(' ')[-1]) == str(key.split(' ')[-1]) or str(current_match_players[1].split(' ')[-2]) == str(key.split(' ')[-1]):
				player_2_data = value[0]
				player_2_name = key

	# Do the math for the odds of winning regarding the elo value.
	# Work out the difference
	difference = float(player_1_data) - float(player_2_data)
	difference = int(round(difference))
	player_b = 1/(1+10**(difference/400.0))
	player_a = (1 - player_b) / 1.1
	print('{} current odds of winning are {}'.format(player_2_name,player_b))
	print('{} current odds of winning are {}'.format(player_1_name, player_a))

	# If the data frame is empty use the ELO odds + the changes.
	if df.empty:
		player_1_change = (
								player_a + changes)

		print (
			'{} and {} have not played before but the ranking suggests that {} should have a chance of {}&'.format(
				current_match_players[0], current_match_players[1],current_match_players[0],round(player_1_change,1)))
		df_completed.loc[index, 'player_1_win_probability'] = round(player_1_change,1)
		return

	get_average_win(df, changes, player_a)


def get_average_win(df, change, player_result):

	# Set a new frame up counting the number of wins for each player
	df_winner = df.groupby('Winner').size()

	# Lookup the value and set to 0 if there is no value due to no games played.
	try:
		player_1_wins = df_winner[current_match_players[0]]
	except KeyError:
		player_1_wins = 0

	try:
		player_2_wins = df_winner[current_match_players[1]]
	except KeyError:
		player_2_wins = 0

	# Create a tuple with the two player wins a,b
	a = (int(player_1_wins), int(player_2_wins))
	# Find the highest number in the tuple
	index_high = int(a.index(max(a)))
	# Calculate the total games
	total_games = int(player_1_wins) + int(player_2_wins)
	# Calculate the percentage of the highest number of games won
	wins_percentage = 100 * float(a[index_high]) / float(total_games)

	print('Player 1 {} won {} times in a total of {} games.'.format(current_match_players[0], player_1_wins, total_games))
	print('Player 2 {} won {} times in a total of {} games.'.format(current_match_players[1], player_2_wins, total_games))
	print('{} won the most games and won an average of {}% of the time'.format(current_match_players[index_high], wins_percentage))
	print(
			'\nA correction due to ranking has given the following result\n{} has a {} chance of winning'.format(
				current_match_players[index_high], round(player_result + change,1)))

	df_completed.loc[index, 'player_1_win_probability'] = round(player_result + change,1)


def break_points_won(player_number, bp_won, pb_total, df):
	try:
		temp_df = df[df.Winner == str(current_match_players[player_number])]
		total_games = (temp_df[bp_won].count())
		total_data = (temp_df[bp_won].sum())
		if total_data == 0:
			return 0
		average_data_player_bp = float(float(total_data) / float(total_games))

		temp_df = df[df.Winner == str(current_match_players[player_number])]

		total_games = (temp_df[pb_total].count())
		total_data = (temp_df[pb_total].sum())
		if total_data == 0:
			return 0
		average_data_player_won = float(float(total_data) / float(total_games))

		print('Average Break Points Won {}: {}'.format(current_match_players[player_number],average_data_player_bp))
		return percentage(1, average_data_player_bp, average_data_player_won)
	except ZeroDivisionError:
		return 0


def compare_data(weight, winner_column, loser_column, df):
	try:
		temp_df = df[df.Winner == str(current_match_players[0])]

		total_games = (temp_df[winner_column].count())
		total_data = (temp_df[winner_column].sum())
		if total_data == 0:
			temp_df = df[df.Winner == str(current_match_players[1])]
			total_games = (temp_df[loser_column].count())
			total_data = (temp_df[loser_column].sum())
		average_data_player_1 = float(float(total_data) / float(total_games))
		#print ('{} has an average of {} {}'.format(players[0], average_data_player_1, winner_column))

		# Drop player 1
		temp_df = df[df.Winner == str(current_match_players[1])]

		total_games = (temp_df[winner_column].count())
		total_data = (temp_df[winner_column].sum())
		if total_data == 0:
			temp_df = df[df.Winner == str(current_match_players[0])]
			total_games = (temp_df[loser_column].count())
			total_data = (temp_df[loser_column].sum())

		average_data_player_2 = float(float(total_data) / float(total_games))
		#print ('{} has an average of {} {}'.format(players[1], average_data_player_2, winner_column))
		return float(percentage(weight, average_data_player_2, average_data_player_1))
	except ZeroDivisionError:
		return 0


def rankings(matches, winner, loser):

	df = pandas.DataFrame(
		columns=[
			'Winner', 'Looser', 'Tournament_Date', 'Winner_Rank'])
	for index_match, row_match in matches.iterrows():
		match_players = (row_match['Winner'])

		if any(s in match_players for s in current_match_players):

			df.loc[-1] = [
				row_match['Winner'], row_match['Loser'], row_match['Tournament_Date'],
				row_match['Winner_Rank']]
			df.index = df.index + 1
			df = df.sort_index()
	with pandas.option_context('display.max_rows', None, 'display.max_columns', None):

		# Rankings
		player_2_loc = df.Winner.ne(winner).idxmax()
		player_1_loc = df.Winner.ne(loser).idxmax()

		player_1_rank = df.iloc[player_1_loc]['Winner_Rank']
		player_2_rank = df.iloc[player_2_loc]['Winner_Rank']

		# Aces
		print('{} latest rank is {} \n{} latest rank is {}'.format(current_match_players[0], player_1_rank, current_match_players[1], player_2_rank))

		percent_between_rank = percentage(70, player_1_rank, player_2_rank)

		return float(percent_between_rank)


def percentage(weight, player_1_rank, player_2_rank):
	try:
		top = (float(player_1_rank) - float(player_2_rank))
		top = top * -1
		bottom = (float(player_1_rank) + float(player_2_rank))# /2???
		x = top / bottom
		if int(player_1_rank) > int(player_2_rank):
			x = x * -1

		y = x * weight

		return y
	except ZeroDivisionError:
		return 0


df_players = pandas.read_csv('men_dummy_submission_file.csv', low_memory=False)
df_matches = pandas.read_csv('ATP_matches_lower.csv', low_memory=False)
df_completed = pandas.read_csv('submission_men.csv', low_memory=False)

url = 'http://tennisabstract.com/reports/atp_elo_ratings.html'

page = urllib2.urlopen(url).read()
soup = BeautifulSoup(page,features="html.parser")

item_list = {}
for tr in soup.find_all('tr')[5:]:
	player = tr.find('a')
	items = (tr.findAll("td"))
	item_list[player.text.encode('utf-8')
											.strip().replace("\xc2\xa0", " ").lower()] =\
										[items[3].text.encode('utf-8').strip(), items[5].text.encode('utf-8').strip(),
											items[7].text.encode('utf-8').strip()]

item_list['guido andreozzi'] = [1698,0,0]
item_list['christian garin'] = [1618,0,0]
item_list['bradley klahn'] = [1760,0,0]
item_list['ugo humbert'] = [1600,0,0]
item_list['michael mmoh'] = [1731,0,0]
item_list['lorenzo sonego'] = [1762,0,0]
item_list['felix auger aliassime'] = [1747,0,0]
item_list['lloyd harris'] = [1722,0,0]
item_list['jason kubler'] = [1600,0,0]
item_list['hugo dellien'] = [590,0,0]#????
item_list['juan ignacio londero'] = [490,0,0]#????
item_list['marco trungelliti'] = [482,0,0]#????
item_list['adrian menendez maceiras'] = [440,0,0]#????

print(item_list)
for index, row in df_players.iterrows():
	print('\n')
	# Set the first two players names.
	current_match_players = (row['player_1'].lower().replace('-',' '), row['player_2'].lower().replace('-',' '))
	print (df_completed.loc[index, 'player_1_win_probability'])
	#if str(df_completed.loc[index, 'player_1_win_probability']) == str(0.5):
	elo_lookup()
	df_completed.to_csv('submission_men.csv', encoding='utf-8', index=False)
	#else:
	#	print('Already Completed')


