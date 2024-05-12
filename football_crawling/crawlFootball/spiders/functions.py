from datetime import datetime
import re
import pandas as pd
class Functions:
    def ExtractWorkRates(self, str):
        result = str.split('/')
        result = [s.strip() for s in result]
        return result
    def ConvertUpdateDate(self, str):
        date_object = datetime.strptime(str, '%b %d, %Y')
        formatted_date = date_object.strftime('%Y-%m-%d')
        return formatted_date
    def ExtractInfosString(self, str):
        age = re.findall(r'\d+', str)[0]
        birth_date = re.findall(r'[A-Za-z]+\s\d+,\s\d+', str)[0]
        birth_date = self.ConvertUpdateDate(birth_date)
        height = re.findall(r'\d+cm', str)[0][:-2]
        weight = re.findall(r'\d+kg', str)[0][:-2]
        
        result_list = [age, birth_date, height, weight]

        return result_list
    def ExtractTeamIdsFromURL(self, url):
        team_id = re.search(r"/team/(\d+)/", url).group(1)
        return team_id
    def ExtractMatchIdFromTransfermarkt(self, url):
        split_string = url.split("/")
        index_spieler = split_string.index("spielbericht")
        player_id = split_string[index_spieler + 1]
        return player_id
        
    def RemoveAllExtraSpaceAndEnter(self, input_string):
        final_str = re.sub(r'\s+', ' ', input_string.strip())
        final_str = final_str.replace('\n','')
        return final_str
    def ConvertTransfermarktMatchDay(self, match_day):
        date_obj = datetime.strptime(match_day, "%a, %m/%d/%y")
        formatted_date = date_obj.strftime("%Y-%m-%d")
        return formatted_date
    def ExtractPlayerIdTransfermarkt(self, url):
        split_string = url.split("/")
        index_spieler = split_string.index("spieler")
        player_id = split_string[index_spieler + 1]
        return player_id
    def ExtractTeamIdFromTransfermarkt(self, url):
        split_string = url.split("/")
        index_team = split_string.index("verein")
        team_id = split_string[index_team + 1]
        return team_id
    def RemoveNotUsedCharInFormation(self,formation):
        formation = formation.replace('Starting Line-up: ','')
        formation = formation.replace('Attacking','')
        formation = formation.replace('Defending','')
        formation = formation.replace('double 6','')
        formation = formation.replace('flat','')
        formation = formation.replace('Diamond','')
        formation = self.RemoveAllExtraSpaceAndEnter(formation)
        return formation
    def ExtractPlayerIdFromUrl_fbref(self, url):
        split_string = url.split('/')
        index_players = split_string.index('players')
        player_id = split_string[index_players+1]
        return player_id
    def Fbref_ExtractTotalStats(self,string):
        split_string = string.split(' ')
        return split_string[2]
    def Fbref_ExtractMatchID(self,url):
        split_string = url.split('/')
        index_matches = split_string.index('matches')
        match_id = split_string[index_matches+1]
        return match_id
    def Fbref_ExtractMatchDate(self,date_string):
        date_format = "%A %B %d, %Y"
        datetime_object = datetime.strptime(date_string, date_format)
        return datetime_object.date()
    def Fbref_ExtractTeamIDs(self,url):
        split_string = url.split('/')
        index_squads = split_string.index('squads')
        team_id = split_string[index_squads+1]
        return team_id
    
    # def GetFirstDaysOfEachMonth(self,input_df):
    #     """
    #     This function will get the first update of each month only
    #     input_df contains column "date" and "url"
    #     """
    #     dates = input_df['date'].tolist()
    #     first_days_of_each_month = []
    #     # Loop through the list of dates
    #     for i in range (0,len(dates)):
    #         if (i+1<len(dates)): # Check if the next date exists
    #             next_date = dates[i+1] # Get the next date
    #         else: break
    #         current_month = dates[i].split(' ')[0] # Get the current month
    #         next_month = next_date.split(' ')[0] # Get the next month
    #         if (current_month != next_month): # Check if the current month is different from the next month
    #             first_days_of_each_month.append(dates[i])
    #     result = input_df[input_df['date'].isin(first_days_of_each_month)]
    #     return result
    def GetFirstDaysOfEachMonth(self,df):
        # Format "date" column
        df['date'] = pd.to_datetime(df['date'], format="%b %d, %Y", errors='coerce')
        df = df.dropna(subset=['date'])
        df['year'] = df['date'].dt.year
        df['month'] = df['date'].dt.month
        df['day'] = df['date'].dt.day

        # Find the minimum day for each month and year
        min_day_df = df.groupby(['year', 'month'])['day'].min().reset_index()
        # Merge with the original dataframe to get the corresponding URL
        result = pd.merge(df, min_day_df, on=['year', 'month', 'day'])
        return result[['url', 'date']]
    
    def Fbref_ExtractFormation(self,str):
        opening_paren_index = str.index("(")
        closing_paren_index = str.index(")")
        formation = str[opening_paren_index + 1:closing_paren_index]
        return formation



