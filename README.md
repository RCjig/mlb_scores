# mlb_scores
Python web scraper for MLB scores.

Uses python scripting and BeautifulSoup4 import to web scrape from
cbssports.com and its html. Including scores, relative data such as
time for game to take place or current inning are also show.

Script uses nested for loops to go through each class container and
separates each scorecard from the website into three categories: pre,
in, and post-game. Based on which category the scorecard is in, a
different type of status is displayed.

Output is displayed to the consoleas the status of the game, followed 
by the team names in the game along with their HRE. Output is update
everytime the script is ran.

Future plans for this python script are conversion into javascript
for a chrome extension, revised output design, and live output changes
in accordance with realtime scores.
