# NFL-draft-analysis
Web scraper and subsequent analysis about the NFL draft over the past 10 years

Files included:
1) nfl_draft_scrape.py -> creates csv file for every player and their pro statistics in each NFL draft from 2010-2020.  Scrapes the data from https://www.pro-football-reference.com/years/2020/draft.htm and for each page for all other years in the draft. THIS SHOULD BE FIRST FILE TO RUN.

2) basic_draft_summations.py -> makes a new dataframe with pandas, and basic overview of the data using pandas groupby functions.  Also includes matplotlib.pyplot to provide two different barh graphs to illustrate number of NFL pro bowl appearances by each grouping.

First graph: display of top 30 colleges for pro bowl appearances in NFL (code to obtain graph is in basic_draft_summations.py)
![by_univ](https://user-images.githubusercontent.com/70147377/105380576-0c2adb00-5bdc-11eb-8708-77f56df7d210.png)


