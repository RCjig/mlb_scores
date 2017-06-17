import requests
from bs4 import BeautifulSoup

# get cbssports page for scores
page = requests.get("http://www.cbssports.com/mlb/scoreboard/")
soup = BeautifulSoup(page.content, 'html.parser')

# hold outer containers for each row
scorecard_rows = soup.findAll(class_="row-fixed-height")

# loop through one row of scoreboards
for scorecard_row in scorecard_rows:

	# set list of scorecards
	single_cards = scorecard_row.findAll(class_="single-score-card ingame mlb")

	# loop through each scorecard for table of data
	for tables in single_cards:

		# set table
		table_section = tables.find(class_="in-progress-table section ")
		table = table_section.find('table')
		body = table.find('tbody')
		rows = body.findAll('tr')

		# loop through and print RHE
		for tr in rows:
			cols = tr.findAll('td')
			for td in cols:
				text = td.find(text=True)
				print text,
			print
