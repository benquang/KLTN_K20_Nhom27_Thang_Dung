import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from items import *
from functions import Functions
import os,shutil
import undetected_chromedriver as uc
class CrawlMatches:
    leagues_urls = [
        "https://fbref.com/en/comps/9/", #Premier league
        "https://fbref.com/en/comps/12/", #LaLiga
        "https://fbref.com/en/comps/11/", #Seria A
        "https://fbref.com/en/comps/20/", #Bundesliga
        "https://fbref.com/en/comps/13/" #Ligue 1
    ]
    leagues = [
        'Premier League',
        'LaLiga',
        'Serie A',
        'Bundesliga',
        'Ligue 1'
    ]
    root_url = "https://fbref.com/"
    season = 2023
    numOfSeason = 6
    driver = None
    wait = None
    def initialize_driver(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_extension('./extensions/ublock.crx')
        # options.add_argument(r"--user-data-dir=C:\Users\super\AppData\Local\Google\Chrome\User Data")
        # options.add_argument(r"--profile-directory=Profile 4")
        ublock_extension_path = "./extensions/ublock.crx"
        options.add_argument("load-extension=" + ublock_extension_path)
        self.driver = uc.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)
    def close_driver(self):
        if self.driver:
            self.driver.quit()
    def start_crawling(self):
        self.initialize_driver()
        try:
            for index,url in enumerate(self.leagues_urls):
                self.parse_on_seasons(url = url, league = self.leagues[index])
        finally:
            # self.close_driver()
            pass
        
    
    def parse_on_seasons(self, **kwargs):
        start_url = kwargs.get('url')
        match_urls = []
        for i in range(0, self.numOfSeason):
            season = self.season - i
            season_url = str(season) + "-" + str(season + 1) + '/schedule/'
            current_url = start_url + season_url

            self.driver.get(current_url)

            match_urls_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, '//td[@class= "center " and @data-stat="score"]/a')
            ))
            match_urls = [element.get_attribute('href') for element in match_urls_element]
            for url in match_urls:
                for i in range(0, 10):
                    try:
                          self.parse_on_matches(current_url = url, season = str(self.season-i)+'/'+str(self.season-i+1), 
                                      league = kwargs.get('league'))
                    except Exception as e:
                        continue
                    break
            # for url in match_urls:
            #     self.parse_on_matches(current_url = url, season = str(self.season-i)+'/'+str(self.season-i+1)
                            #   , league = kwargs.get('league'))

    def parse_on_matches(self, **kwargs):
        current_url = kwargs.get('current_url')
        print(current_url)
        self.driver.get(current_url)

        # self.scroll_down_to_bottom()

        # wait until elements are loaded
        wait = WebDriverWait(self.driver, 60)
        # wait.until(
        #         EC.presence_of_element_located(
        #             (By.XPATH, '//div[@class = "scorebox"]')
        #     ))
        # wait.until(
        #         EC.presence_of_element_located(
        #             (By.XPATH, '//th[@scope="row"]')
        #         )
        # )

        home_stats = Fbref_MatchStats() 
        away_stats = Fbref_MatchStats()
        home_squad  = Fbref_MatchSquad()
        away_squad = Fbref_MatchSquad()
        match_infos = Fbref_MatchInfos()

        match_id = Functions.Fbref_ExtractMatchID(current_url)
        home_stats.fbrefMatchId = str(match_id)
        away_stats.fbrefMatchId = str(match_id)
        match_infos.fbrefMatchId = str(match_id)

        match_infos.fbrefURL = str(current_url)
        match_infos.season = kwargs.get('season')
        try:
            league = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="content"]//a'))).text
            match_infos.league = league
        except TimeoutException:
            match_infos.league = ''

        try:
            match_date_element = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="scorebox"]//strong/a')))
            match_date = match_date_element[2].text
            match_date = Functions.Fbref_ExtractMatchDate(match_date)
            match_infos.match_date = match_date
        except TimeoutException:
            match_infos.match_date = ''

        try:
            match_week_element = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@id="content"]/div')))
            match_week = match_week_element.text
            match_week = match_week[match_week.index('Matchweek'):].replace(')','')
            match_infos.match_week = match_week
        except TimeoutException:
            match_infos.match_week = ''

        try:
            teams_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="scorebox"]//strong/a')))
            teams = [team.text for team in teams_elements[0:2]]
            home_stats.team = teams[0]
            away_stats.team = teams[1]
            match_infos.home_team = teams[0]
            match_infos.away_team = teams[1]
        except TimeoutException:
            home_stats.team = ''
            away_stats.team = ''
            match_infos.home_team = ''
            match_infos.away_team = ''

        home_stats.is_home_team = 'Yes'
        away_stats.is_home_team = 'No'

        try:
            scores_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="scores"]/div[@class="score"]')))
            scores = [score.text for score in scores_elements]
            home_stats.score = scores[0]
            away_stats.score = scores[1]
        except:
            home_stats.score = ''
            away_stats.score = ''

        try:
            managers_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[./strong="Manager"]')))
            managers = [manager.text.replace('Manager','').replace('\xa0', ' ')[2:] for manager in managers_elements]
            home_stats.manager = managers[0]
            away_stats.manager = managers[1]
        except:
            home_stats.manager = ''
            away_stats.manager = ''

        try:
            captains_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[./strong="Captain"]/a')))
            captains = [captain.text.replace('\xa0', ' ') for captain in captains_elements]
            home_stats.captain = captains[0]
            away_stats.captain = captains[1]
        except:
            home_stats.captain = ''
            away_stats.captain = ''

        try:
            venue_time = str(match_date)
            venue_time += ', ' + wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="venuetime"]'))).text
            match_infos.venue_time = venue_time
        except TimeoutException:
            match_infos.venue_time = ''

        try:
            attendance = wait.until(EC.presence_of_element_located((By.XPATH, '//div[.//small="Attendance"]/small'))).text
            match_infos.attendance = attendance
        except TimeoutException:
            match_infos.attendance = ''
        
        try:
            venue = wait.until(EC.presence_of_element_located((By.XPATH, '//div[.//small="Venue"]/small'))).text
            match_infos.venue = venue
        except:
            match_infos.venue = ''
        
        try:
            officials_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[.//small="Officials"]/small/span')))
            officials = [official.text.replace('\xa0', ' ') for official in officials_elements]
            officials = ', '.join(officials)
            match_infos.officials = officials
        except:
            match_infos.officials = ''

        formations_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="lineup"]//tr[1]/th')))
        formations = [Functions.Fbref_ExtractFormation(formation.text) for formation in formations_elements]
        formations = [formation.replace('-', '') for formation in formations]
        home_stats.formation = formations[0]
        away_stats.formation = formations[1]

        possessions_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//td[@width="50%"]//strong')))
        possessions = [possession.text for possession in possessions_elements]
        home_stats.possession = possessions[0]
        away_stats.possession = possessions[1]

        extra_stats_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@id="team_stats_extra"]/div/div')))
        extra_stats = [stat.text for stat in extra_stats_elements if stat.text.isdigit()]
        home_stats.fouls = extra_stats[0]
        away_stats.fouls = extra_stats[1]
        home_stats.corners = extra_stats[2]
        away_stats.corners = extra_stats[3]
        home_stats.crosses = extra_stats[4]
        away_stats.crosses = extra_stats[5]
        home_stats.touches = extra_stats[6]
        away_stats.touches = extra_stats[7]
        home_stats.tackles = extra_stats[8]
        away_stats.tackles = extra_stats[9]
        home_stats.interceptions = extra_stats[10]
        away_stats.interceptions = extra_stats[11]
        home_stats.aerials_won = extra_stats[12]
        away_stats.aerials_won = extra_stats[13]
        home_stats.clearances = extra_stats[14]
        away_stats.clearances = extra_stats[15]
        home_stats.offsides = extra_stats[16]
        away_stats.offsides = extra_stats[17]
        home_stats.goal_kicks = extra_stats[18]
        away_stats.goal_kicks = extra_stats[19]
        home_stats.throw_ins = extra_stats[20]
        away_stats.throw_ins = extra_stats[21]
        home_stats.long_balls = extra_stats[22]
        away_stats.long_balls = extra_stats[23]

        home_summary_stats_element = wait.until(EC.presence_of_element_located((By.XPATH, '(//table[contains(@id, "summary")])[1]/tfoot')))
        home_summary_stats = home_summary_stats_element.text.split(' ')
        home_summary_stats = [stat for stat in home_summary_stats if 'Players' not in stat]
        home_stats.total_players_stats = home_summary_stats[0]
        home_stats.minutes = home_summary_stats[1]
        home_stats.Gls = home_summary_stats[2]
        home_stats.Ast = home_summary_stats[3]
        home_stats.PK = home_summary_stats[4]
        home_stats.PKatt = home_summary_stats[5]
        home_stats.Sh = home_summary_stats[6]
        home_stats.SoT = home_summary_stats[7]
        home_stats.CrdY = home_summary_stats[8]
        home_stats.CrdR = home_summary_stats[9]
        home_stats.Touches = home_summary_stats[10]
        home_stats.Tkl = home_summary_stats[11]
        home_stats.Int = home_summary_stats[12]
        home_stats.Blocks = home_summary_stats[13]
        home_stats.xG = home_summary_stats[14]
        home_stats.npxG = home_summary_stats[15]
        home_stats.xAG = home_summary_stats[16]
        home_stats.SCA = home_summary_stats[17]
        home_stats.GCA = home_summary_stats[18]
        home_stats.Passes_Cmp = home_summary_stats[19]
        home_stats.Passes_Att = home_summary_stats[20]
        home_stats.Passes_CmpPercentage = home_summary_stats[21]
        home_stats.Passes_PrgP = home_summary_stats[22]
        home_stats.Carries = home_summary_stats[23]
        home_stats.Carries_PrgC = home_summary_stats[24]
        home_stats.Take_Ons_Att = home_summary_stats[25]
        home_stats.Take_Ons_Succ = home_summary_stats[26]

        away_summary_stats_elements = wait.until(EC.presence_of_element_located((By.XPATH, '(//table[contains(@id, "summary")])[2]/tfoot')))
        away_summary_stats = away_summary_stats_elements.text.split(' ')
        away_summary_stats = [stat for stat in home_summary_stats if 'Players' not in stat]
        away_stats.total_players_stats = away_summary_stats[0]
        away_stats.minutes = away_summary_stats[1]
        away_stats.Gls = away_summary_stats[2]
        away_stats.Ast = away_summary_stats[3]
        away_stats.PK = away_summary_stats[4]
        away_stats.PKatt = away_summary_stats[5]
        away_stats.Sh = away_summary_stats[6]
        away_stats.SoT = away_summary_stats[7]
        away_stats.CrdY = away_summary_stats[8]
        away_stats.CrdR = away_summary_stats[9]
        away_stats.Touches = away_summary_stats[10]
        away_stats.Tkl = away_summary_stats[11]
        away_stats.Int = away_summary_stats[12]
        away_stats.Blocks = away_summary_stats[13]
        away_stats.xG = away_summary_stats[14]
        away_stats.npxG = away_summary_stats[15]
        away_stats.xAG = away_summary_stats[16]
        away_stats.SCA = away_summary_stats[17]
        away_stats.GCA = away_summary_stats[18]
        away_stats.Passes_Cmp = away_summary_stats[19]
        away_stats.Passes_Att = away_summary_stats[20]
        away_stats.Passes_CmpPercentage = away_summary_stats[21]
        away_stats.Passes_PrgP = away_summary_stats[22]
        away_stats.Carries = away_summary_stats[23]
        away_stats.Carries_PrgC = away_summary_stats[24]
        away_stats.Take_Ons_Att = away_summary_stats[25]
        away_stats.Take_Ons_Succ = away_summary_stats[26]
        
        # -------------------------- Export -----------------------------
        home_stats.export_to_csv()
        away_stats.export_to_csv()
        match_infos.export_to_csv()
        # -------------------------- Squad -----------------------------
        player_names_in_squad_home = [element.text for element in wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="lineup"][1]//td//a')))]
        home_kitnums = [element.text for element in wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="lineup"][1]//td')))]
        home_kitnums = home_kitnums[0::2]
        player_names_in_squad_away = [element.text for element in wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="lineup"][2]//td//a')))]
        away_kitnums = [element.text for element in wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="lineup"][2]//td')))]
        away_kitnums = away_kitnums[0::2]
        for index,(name, home_kitnum) in enumerate(zip(player_names_in_squad_home,home_kitnums)):
            home_squad  = Fbref_MatchSquad()
            home_squad.fbrefMatchId = match_id
            home_squad.player_name = name
            home_squad.player_kitnum = home_kitnum
            home_squad.team = home_stats.team
            home_squad.is_home_team = 'Yes'
            if index > 10:
                home_squad.is_sub = 'Yes'
            else:   home_squad.is_sub = 'No'
            home_squad.export_to_csv()

        for index,(name, away_kitnum) in enumerate(zip(player_names_in_squad_away,away_kitnums)):
            away_squad  = Fbref_MatchSquad()
            away_squad.fbrefMatchId = match_id
            away_squad.player_name = name
            away_squad.player_kitnum = away_kitnum
            away_squad.team = away_stats.team
            away_squad.is_home_team = 'No'
            if index > 10:
                away_squad.is_sub = 'Yes'
            else:   away_squad.is_sub = 'No'
            away_squad.export_to_csv()

    
        #------------------------ Goals -----------------------------
        self.parse_on_goals('//div[@class="event" and @id="a"]/div[./div[@class="event_icon goal"]]',
                            match_id=match_id,
                            type_of_goal='Normal',
                            team = match_infos.home_team,
                            is_home_team = 'Yes'
                            )
        self.parse_on_goals('//div[@class="event" and @id="a"]/div[./div[@class="event_icon own_goal"]]',
                            match_id=match_id,
                            type_of_goal='Own Goal',
                            team = match_infos.home_team,
                            is_home_team = 'Yes')
        self.parse_on_goals('//div[@class="event" and @id="a"]/div[./div[@class="event_icon penalty"]]',
                            match_id=match_id,
                            type_of_goal='Penalty',
                            team = match_infos.home_team,
                            is_home_team = 'Yes')
        
        self.parse_on_goals('//div[@class="event" and @id="b"]/div[./div[@class="event_icon goal"]]',
                            match_id=match_id,
                            type_of_goal='Normal',
                            team = match_infos.away_team,
                            is_home_team = 'No'
                            )
        self.parse_on_goals('//div[@class="event" and @id="b"]/div[./div[@class="event_icon own_goal"]]',
                            match_id=match_id,
                            type_of_goal='Own Goal',
                            team = match_infos.away_team,
                            is_home_team = 'No')
        self.parse_on_goals('//div[@class="event" and @id="b"]/div[./div[@class="event_icon penalty"]]',
                            match_id=match_id,
                            type_of_goal='Penalty',
                            team = match_infos.away_team,
                            is_home_team = 'No')

        for i in range(0, int(home_stats.total_players_stats)):
            player_stats = Fbref_MatchPlayerStats()
            player_stats.fbrefMatchId = match_id
            player_stats.player_name = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]/th/a'))).text
            player_stats.nationality = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="nationality"]/a/span'))).text
            player_stats.team = home_stats.team
            player_stats.player_kitnum = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="shirtnumber"]'))).text
            player_stats.position = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="position"]'))).text
            player_stats.age = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="age"]'))).text
            player_stats.minutes = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="minutes"]'))).text
            player_stats.Gls = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="goals"]'))).text
            player_stats.Ast = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="assists"]'))).text
            player_stats.PK = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="pens_made"]'))).text
            player_stats.PKatt = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="pens_att"]'))).text
            player_stats.Sh = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="shots"]'))).text
            player_stats.SoT = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="shots_on_target"]'))).text
            player_stats.CrdY = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="cards_yellow"]'))).text
            player_stats.CrdR = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="cards_red"]'))).text
            player_stats.Touches = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="touches"]'))).text
            player_stats.Tkl = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="tackles"]'))).text
            player_stats.Int = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="interceptions"]'))).text
            player_stats.Blocks = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="blocks"]'))).text
            player_stats.xG = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="xg"]'))).text
            player_stats.npxG = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="npxg"]'))).text
            player_stats.xAG = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="xg_assist"]'))).text
            player_stats.SCA = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="sca"]'))).text
            player_stats.GCA = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="gca"]'))).text
            player_stats.Passes_Cmp = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="passes_completed"]'))).text
            player_stats.Passes_Att = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="passes"]'))).text
            player_stats.Passes_CmpPercentage = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="passes_pct"]'))).text
            player_stats.Passes_PrgP = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="progressive_passes"]'))).text
            player_stats.Carries = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="carries"]'))).text
            player_stats.Carries_PrgC = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="progressive_carries"]'))).text
            player_stats.Take_Ons_Att = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="take_ons"]'))).text
            player_stats.Take_Ons_Succ = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="take_ons_won"]'))).text
            player_stats.export_to_csv()
        for i in range(0, int(away_stats.total_players_stats)):
            with open('./html.html', 'w') as f:
                f.write(self.driver.page_source)
            player_stats = Fbref_MatchPlayerStats()
            player_stats.fbrefMatchId = match_id
            player_stats.player_name = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]/th/a'))).text
            player_stats.team = away_stats.team
            player_stats.nationality = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="nationality"]/a/span'))).text
            player_stats.player_kitnum = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="shirtnumber"]'))).text
            player_stats.position = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="position"]'))).text
            player_stats.age = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="age"]'))).text
            player_stats.minutes = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="minutes"]'))).text
            player_stats.Gls = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="goals"]'))).text
            player_stats.Ast = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="assists"]'))).text
            player_stats.PK = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="pens_made"]'))).text
            player_stats.PKatt = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="pens_att"]'))).text
            player_stats.Sh = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="shots"]'))).text
            player_stats.SoT = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="shots_on_target"]'))).text
            player_stats.CrdY = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="cards_yellow"]'))).text
            player_stats.CrdR = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="cards_red"]'))).text
            player_stats.Touches = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="touches"]'))) .text
            player_stats.Tkl = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="tackles"]'))).text
            player_stats.Int = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="interceptions"]'))).text
            player_stats.Blocks = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="blocks"]'))).text
            player_stats.xG = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="xg"]'))).text
            player_stats.npxG = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="npxg"]'))).text
            player_stats.xAG = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="xg_assist"]'))).text
            player_stats.SCA = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="sca"]'))).text
            player_stats.GCA = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="gca"]'))).text
            player_stats.Passes_Cmp = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="passes_completed"]'))).text
            player_stats.Passes_Att = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="passes"]'))).text
            player_stats.Passes_CmpPercentage = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="passes_pct"]'))).text
            player_stats.Passes_PrgP = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="progressive_passes"]'))).text
            player_stats.Carries = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="carries"]'))).text
            player_stats.Carries_PrgC = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="progressive_carries"]'))).text
            player_stats.Take_Ons_Att = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="take_ons"]'))).text
            player_stats.Take_Ons_Succ = wait.until(EC.presence_of_element_located((By.XPATH, f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="take_ons_won"]'))).text
            player_stats.export_to_csv()
    def parse_on_goals(self,xpath: str, match_id: str,type_of_goal:str,team: str, is_home_team: str):
        wait = WebDriverWait(self.driver, 0.5)
        try:
            goals = [element.text for element in wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))]
            goal_string = [goal.replace('’', '').replace(' ·','') for goal in goals]
            for index, goal_string in enumerate(goal_string):
                goal_string_list = goal_string.split(' ')
                player_name = ''.join(goal_string_list[:-1])
                minute = goal_string_list[-1]
                fbref_MatchGoals = Fbref_MatchGoals()
                fbref_MatchGoals.fbrefMatchId = match_id
                fbref_MatchGoals.player_name = player_name
                fbref_MatchGoals.minute = minute
                fbref_MatchGoals.type_of_goal = type_of_goal
                fbref_MatchGoals.team = team
                fbref_MatchGoals.is_home_team = is_home_team
                fbref_MatchGoals.export_to_csv()
        except TimeoutException as e:
            pass
    def scroll_down_to_bottom(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        except Exception as e:
            print(e)
            pass
def clean_all_fbref_folder_content():
    path = './fbref/'
    if os.path.exists(path=path):
        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))

def main():
    clean_all_fbref_folder_content()
    crawler = CrawlMatches()
    crawler.start_crawling()

if __name__ == '__main__':
    # This code won't run if this file is imported.
    main()