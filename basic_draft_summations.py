import requests
import pandas as pd
import csv
import numpy as np
import matplotlib.pyplot as plt


class NFL_draft_analysis():
    def __init__(self):
        pass

    def separate_file(self):
        """
            Read csv file into pandas dataframe (df)
            Then, add 'names' row as column titles
        """
        df = pd.read_csv("nfl_drafts.csv", names = ['Pick', 'Team', 'Player_name', 'POS', 
        'Age', 'Last_played', 'AP1', 'PB', 'ST', 'CarAV', 'DrAV', 'G_perS', 'PaCmp', 'PaAtt', 
        'PaYds', 'PaTD', 'Int', 'Att', 'Yds', 'RuTD', 'Rec', 'ReYds', 'ReTD', 'Solo', 'DeInt', 
        'Sk', 'Coll/Univ', 'Stat'], error_bad_lines = False)
        return df
        
    def PB_by_position(self, df):
        """
             Calculate number of NFL pro bowl appearances by player position on draft day
        """
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            df_pos = df.groupby(['POS']).sum()
            print(df_pos['PB'])
 
    def sum_by_university(self,df):
        """
            Calculate number of All Pro teams by Coll/University
            Then, presents a visual on number of NFL pro-bowl appearances each college produces (top 30 universities)
        """
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            df_univ = df.groupby(['Coll/Univ']).sum()
        
        df_univ = df_univ.sort_values('PB')
        df_top_univ = df_univ[-30:]
        
        #Visual bargraph for top 30 Colleges and number of pro-bowl appearances they produce
        df_univ_PB = df_top_univ['PB']
        univ_plot = df_univ_PB.plot(kind="barh", fontsize=4)
        univ_plot.set_xlabel("Pro bowl appearances")
        univ_plot.set_title("PRO BOWL APPEARANCES, BY COLLEGE/UNIVERSITY, 2010-2020")
        plt.show()
        
        return
    
    def sum_by_team(self,df):
        """
            Calculate sums by each team for pro-bowls, all pro teams, and total games started 
            Then, present a visual of pro-bowl appearances of picks sorted by team drafting 
        """
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
            df_team = df.groupby(['Team']).sum()
            #print(df_team[['PB', 'AP1', 'ST']])
            

        #for a visual, barh of pro-bowls by drafting team
        df_team1 = df_team['PB']
        team_plot = df_team1.plot(kind="barh", fontsize=4)
        team_plot.set_xlabel("Pro bowl appearances")
        team_plot.set_title("PRO BOWL APPEARANCES, BY NFL DRAFTING TEAM, 2010-2020")
        plt.show()
        
        #return the new df(by team)
        return df_team

                  
#driver code
P = NFL_draft_analysis()
dF = P.separate_file()
P.sum_by_university(dF) 
P.PB_by_position(dF)
df_avgs = P.sum_by_team(dF)
