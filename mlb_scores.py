import datetime
import requests
from bs4 import BeautifulSoup


# get cbssports page for scores
today = datetime.datetime.now()
page = requests.get("http://www.cbssports.com/mlb/scoreboard/" + today.strftime('%Y%m%d/'))
soup = BeautifulSoup(page.content, 'html.parser')

# hold outer containers for each row
scorecard_rows = soup.findAll(class_="row-fixed-height")

print
print '---------'

# loop through one row of scoreboards
for scorecard_row in scorecard_rows:

	# set list of scorecards for live games
	single_cards_live = scorecard_row.findAll(class_="single-score-card ingame mlb")

	# loop through each scorecard for table of data
	for tables in single_cards_live:

		#status
		print "STATUS: Inning -",

		inning_container = tables.find(class_="top-bar")
		inning = inning_container.find(class_="game-status in-progress")
		print (inning.find(text=True))

		# set table
		table_section = tables.find(class_="in-progress-table section ")
		table = table_section.find('table')
		body = table.find('tbody')
		rows = body.findAll('tr')

		# loop through and print RHE
		for tr in rows:
			cols = tr.findAll('td')

			# print team name
			team_container = tr.find(class_='team')
			team_name = team_container.find(class_='team')
			print (team_name.find(text=True)),

			for td in cols:
				text = td.find(text=True)
				print text,
			print
		print '---------'

	# post game scorecards
	single_cards_post = scorecard_row.findAll(class_="single-score-card postgame mlb")

	# loop through each scorecard for table of data
	for tables in single_cards_post:

		#status
		print "STATUS: FINAL"

		# set table
		table_section = tables.find(class_="in-progress-table section ")
		table = table_section.find('table')
		body = table.find('tbody')
		rows = body.findAll('tr')

		# loop through and print RHE
		for tr in rows:
			cols = tr.findAll('td')

			# print team name
			team_container = tr.find(class_='team')
			team_name = team_container.find(class_='team')
			print (team_name.find(text=True)),

			for td in cols:
				text = td.find(text=True)
				print text,
			print
		print '---------'

	# pre game scorecards
	single_cards_pre = scorecard_row.findAll(class_="single-score-card pregame mlb")

	# loop through each scorecard for table of data
	for tables in single_cards_pre:

		#status
		print "STATUS:",

		time_container = tables.find(class_="game-status pregame")
		time = time_container.find(class_="game-status pregame-date")
		time_print = (unicode((time.find(text=True))).encode('ascii', 'ignore'))[57:64]

		if time_print[6] == 'm':
			print time_print
		else:
			print time_print,

		# set table
		table_section = tables.find(class_="in-progress-table section ")
		table = table_section.find('table')
		body = table.find('tbody')
		rows = body.findAll('tr')

		# loop through and print RHE
		for tr in rows:
			cols = tr.findAll('td')

			# print team name
			team_container = tr.find(class_='team')
			team_name = team_container.find(class_='team')
			print (team_name.find(text=True)),
			print

		print '---------'

print
