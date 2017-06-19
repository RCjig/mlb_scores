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

	# post game scorecards
	single_cards_post = scorecard_row.findAll(class_="single-score-card postgame mlb")

	# loop through each scorecard for table of data
	for tables in single_cards_post:

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

print
