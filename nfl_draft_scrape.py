import requests, re
from bs4 import BeautifulSoup
import pandas as pd
import csv


class NFL_Draft_scrape():
    def __init__(self):
        #empty 2d array to hold data
        self.full_draft = []
        self.draft_timeline = ['https://www.pro-football-reference.com/years/2019/draft.htm', 
        'https://www.pro-football-reference.com/years/2018/draft.htm', 'https://www.pro-football-reference.com/years/2017/draft.htm', 
        'https://www.pro-football-reference.com/years/2016/draft.htm', 'https://www.pro-football-reference.com/years/2015/draft.htm', 
        'https://www.pro-football-reference.com/years/2014/draft.htm', 'https://www.pro-football-reference.com/years/2013/draft.htm',
        'https://www.pro-football-reference.com/years/2012/draft.htm', 'https://www.pro-football-reference.com/years/2011/draft.htm',
        'https://www.pro-football-reference.com/years/2010/draft.htm']
        
        #Finding correct URL for draft year
        URL = 'https://www.pro-football-reference.com/years/2020/draft.htm'
        page = requests.get(URL)

        self.soup = BeautifulSoup(page.content, 'html.parser')
    
    def make_draft_file(self):
        """
            Simple function to make CSV file, 
            called if CSV does not exist
        """
        self.f = open("nfl_drafts.csv", "w+")
        
        

    def draft_to_file(self, draft_season='https://www.pro-football-reference.com/years/2020/draft.htm'):
        """
            Getting every draft selection, putting in csv file
        """
        #set URL equal to current draft season, passed in from function call
        URL = draft_season
        page = requests.get(URL)
        self.soup = BeautifulSoup(page.content, 'html.parser')

        self.full_draft = []
        results = self.soup.find('tbody')
        player_position = results.select('tr td')
        player_row = [element.text for element in player_position]
        
        player_data = []
        string_copy = []
        for row in player_row:
            string_copy.append(row)
            
            if row == 'College Stats':
                player_data = string_copy[:]
                string_to_use = str(string_copy)
                self.full_draft.extend([player_data])
                with open("nfl_drafts.csv", "a") as a_file:
                    a_file.write("\n")

                    #cleaning up the punctuation
                    string_to_use = string_to_use.replace("[", "")
                    string_to_use = string_to_use.replace(']', '')
                    string_to_use = string_to_use.replace("'", "")

                    a_file.write(string_to_use) 
                string_copy.clear()

        a_file.close()

    def import_drafts(self):
        """
            Load all other drafts into the file
        """
        for draft in self.draft_timeline:
            self.draft_to_file(draft)
                  
#driver code
draft1 = NFL_Draft_scrape()
#If file does not exist, make it, then append data; else, append data by itself
if 'nfl_drafts.csv' == False:
    draft1.make_draft_file()

#import the drafts to csv
draft1.draft_to_file()
draft1.import_drafts()
        