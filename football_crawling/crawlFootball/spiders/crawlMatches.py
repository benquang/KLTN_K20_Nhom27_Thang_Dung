import scrapy
from crawlFootball.items import *
from crawlFootball.spiders.functions import *

class CrawlmatchSpider(scrapy.Spider):
    name = "crawlMatches"
    allowed_domains = ["fbref.com"]
    start_urls = ["https://fbref.com/en/comps/9/",  #Premier Leauge
                    # "https://fbref.com/en/comps/12/", #LaLiga
                    # "https://fbref.com/en/comps/11/",  #Seria A
                    # "https://fbref.com/en/comps/20/", #Bundesliga
                    # "https://fbref.com/en/comps/13/"   #Ligue 1
                  ]
    root_url = "https://fbref.com/";
    season = 2023
    numOfSeason = 6
    custom_settings = {
        # 'FEEDS':{
        #     'matches.csv':{'format':'csv','overwrite':True}
        #     },
        'LOG_STDOUT' : {True},
        "LOG_FILE" :'./crawlMatches_log.txt',
        'DOWNLOADER_MIDDLEWARES':{
            'crawlFootball.middlewares.TooManyRequestsRetryMiddleware': 543,
        },
        'ITEM_PIPELINES':{
            "crawlFootball.pipelines.MultiCSVItemPipeline": 300,
        },
        'DOWNLOAD_DELAY' : 2,
        'CONCURRENT_REQUESTS' : 1,
        'RETRY_HTTP_CODES' : [429],
    }
    def parse(self, response):
        for url in self.start_urls:
            yield response.follow(url = url,
                                  callback = self.parse_on_seasons,
                                  meta = {'current_url':url}
                                )
    def parse_on_seasons(self,response):
        start_url=response.meta.get('current_url')
        for i in range(0,self.numOfSeason):
            response.meta['current_url'] = start_url
            season = self.season - i
            season_url = str(season) + "-" + str(season+1)+'/schedule/' 
            response.meta['season'] = str(season) + "/" + str(season+1) 
            response.meta['current_url'] += season_url 
            current_url = response.meta['current_url']
            yield response.follow(url = current_url,callback = self.parse_on_matches,
                                  meta = response.meta
                                  )
    def parse_on_matches(self,response):
        matches = response.xpath('//td[@class= "center " 
                                  and @data-stat="score"]/a/@href').extract()
        for match in matches:
            current_url = "https://fbref.com" + match
            response.meta['current_url'] = current_url
            yield response.follow(url = current_url,
                                  callback = self.parse_on_match_stats,
                                  meta = response.meta)
    def parse_on_match_stats(self,response):
        function = Functions()
        home_stats = fbref_MatchStats() 
        away_stats = fbref_MatchStats()
        home_squad  = fbref_MatchSquad()
        away_squad = fbref_MatchSquad()
        match_infos = fbref_MatchInfos()

        match_id = function.Fbref_ExtractMatchID(response.meta.get('current_url'))
        home_stats['fbrefMatchId'] = match_id
        away_stats['fbrefMatchId'] = match_id
        match_infos['fbrefMatchId'] = match_id

        match_infos['fbrefURL'] = response.meta.get('current_url')
        match_infos['season'] = response.meta.get('season')

        leauge = response.xpath('//div[@id="content"]//a/text()').get()
        match_infos['leauge'] = leauge

        match_date = response.xpath('//div[@class = "scorebox"]//strong/a/text()').extract()[2]
        match_infos['match_date_str'] = match_date

        match_infos['match_date'] = function.Fbref_ExtractMatchDate(match_date)

        match_week = response.xpath('//div[@id="content"]/div/text()').get()[1:]
        match_week = match_week.replace('(',"").replace(')',"")
        match_infos['match_week'] = match_week

        teams = response.xpath('//div[@class = "scorebox"]//strong/a/text()').extract()[0:2]
        home_stats['team'] = teams[0]
        away_stats['team'] = teams[1]
        match_infos['home_team'] = teams[0]
        match_infos['away_team'] = teams[1]

        home_stats['is_home_team'] = 'Yes'
        away_stats['is_home_team'] = 'No'

        scores = response.xpath('//div[@class = "scores"]/div[@class="score"]/text()').extract()
        home_stats['score'] = scores[0]
        away_stats['score'] = scores[1]

        managers = response.xpath('//div[./strong/text()="Manager"]/text()').extract()
        managers = [manager.replace('\xa0',' ')[2:] for manager in managers ]
        home_stats['manager'] = managers[0]
        away_stats['manager'] = managers[1]

        captains = response.xpath('//div[./strong/text()="Captain"]/a/text()').extract()
        captains = [captain.replace('\xa0',' ') for captain in captains ]
        home_stats['captain'] = captains[0]
        away_stats['captain'] = captains[1]
        
        venue_time = str(match_date)
        venue_time +=', '+response.xpath('//span[@class = "venuetime"]/text()').get()
        match_infos['venue_time'] = venue_time

        attendance = response.xpath('//div[.//small/text()="Attendance"]/small/text()').get()
        match_infos['attendance'] = attendance

        venue = response.xpath('//div[.//small/text()="Venue"]/small/text()').get()
        match_infos['venue'] = venue

        officials = response.xpath('//div[.//small/text()="Officials"]/small/span/text()').extract()
        officials = [official.replace('\xa0',' ') for official in officials ]
        officials = ', '.join(officials)
        match_infos['officials'] = officials

        formations = response.xpath('//div[@class="lineup"]//tr[1]/th/text()').extract()
        formations = [function.Fbref_ExtractFormation(formation) for formation in formations]
        formations = [formation.replace('-','') for formation in formations]
        home_stats['formation'] = formations[0]
        away_stats['formation'] = formations[1]

        possessions = response.xpath('//td[@width="50%"]//strong/text()').extract()
        home_stats['possession'] = possessions[0]
        away_stats['possession'] = possessions[1]

        extra_stats = response.xpath('//div[@id="team_stats_extra"]/div/div/text()').extract()
        extra_stats = [stat for stat in extra_stats if stat.isdigit()]
        home_stats['fouls'] = extra_stats[0]
        away_stats['fouls'] = extra_stats[1]
        home_stats['corners'] = extra_stats[2]
        away_stats['corners'] = extra_stats[3]
        home_stats['crosses'] = extra_stats[4]
        away_stats['crosses'] = extra_stats[5]
        home_stats['touches'] = extra_stats[6]
        away_stats['touches'] = extra_stats[7]
        home_stats['tackles'] = extra_stats[8]
        away_stats['tackles']= extra_stats[9]
        home_stats['interceptions']= extra_stats[10]
        away_stats['interceptions']= extra_stats[11]
        home_stats['aerials_won']= extra_stats[12]
        away_stats['aerials_won']= extra_stats[13]
        home_stats['clearances']= extra_stats[14]
        away_stats['clearances']= extra_stats[15]
        home_stats['offsides']= extra_stats[16]
        away_stats['offsides']= extra_stats[17]
        home_stats['goal_kicks']= extra_stats[18]
        away_stats['goal_kicks']= extra_stats[19]
        home_stats['throw_ins']= extra_stats[20]
        away_stats['throw_ins']= extra_stats[21]
        home_stats['long_balls']= extra_stats[22]
        away_stats['long_balls']= extra_stats[23]
        
        home_summary_stats = response.xpath('(//table[contains(@id, "summary")])[1]/tfoot//text()').extract()
        home_stats['total_players_stats'] = home_summary_stats[0].replace(' Players','')
        home_stats['minutes'] = home_summary_stats[1]
        home_stats['Gls'] = home_summary_stats[2]
        home_stats['Ast'] = home_summary_stats[3]
        home_stats['PK'] = home_summary_stats[4]
        home_stats['PKatt'] = home_summary_stats[5]
        home_stats['Sh'] = home_summary_stats[6]
        home_stats['SoT'] = home_summary_stats[7]
        home_stats['CrdY'] = home_summary_stats[8]
        home_stats['CrdR'] = home_summary_stats[9]
        home_stats['Touches'] = home_summary_stats[10]
        home_stats['Tkl'] = home_summary_stats[11]
        home_stats['Int'] = home_summary_stats[12]
        home_stats['Blocks'] = home_summary_stats[13]
        home_stats['xG'] = home_summary_stats[14]
        home_stats['npxG'] = home_summary_stats[15]
        home_stats['xAG'] = home_summary_stats[16]
        home_stats['SCA'] = home_summary_stats[17]
        home_stats['GCA'] = home_summary_stats[18]
        home_stats['Passes_Cmp'] = home_summary_stats[19]
        home_stats['Passes_Att'] = home_summary_stats[20]
        home_stats['Passes_CmpPercentage']  = home_summary_stats[21]
        home_stats['Passes_PrgP'] = home_summary_stats[22]
        home_stats['Carries'] = home_summary_stats[23]
        home_stats['Carries_PrgC'] = home_summary_stats[24]
        home_stats['Take_Ons_Att'] = home_summary_stats[25]
        home_stats['Take_Ons_Succ'] = home_summary_stats[26]

        away_summary_stats = response.xpath('(//table[contains(@id, "summary")])[2]/tfoot//text()').extract()
        away_stats['total_players_stats'] = away_summary_stats[0].replace(' Players','')
        away_stats['minutes'] = away_summary_stats[1]
        away_stats['Gls'] = away_summary_stats[2]
        away_stats['Ast'] = away_summary_stats[3]
        away_stats['PK'] = away_summary_stats[4]
        away_stats['PKatt'] = away_summary_stats[5]
        away_stats['Sh'] = away_summary_stats[6]
        away_stats['SoT'] = away_summary_stats[7]
        away_stats['CrdY'] = away_summary_stats[8]
        away_stats['CrdR'] = away_summary_stats[9]
        away_stats['Touches'] = away_summary_stats[10]
        away_stats['Tkl'] = away_summary_stats[11]
        away_stats['Int'] = away_summary_stats[12]
        away_stats['Blocks'] = away_summary_stats[13]
        away_stats['xG'] = away_summary_stats[14]
        away_stats['npxG'] = away_summary_stats[15]
        away_stats['xAG'] = away_summary_stats[16]
        away_stats['SCA'] = away_summary_stats[17]
        away_stats['GCA'] = away_summary_stats[18]
        away_stats['Passes_Cmp'] = away_summary_stats[19]
        away_stats['Passes_Att'] = away_summary_stats[20]
        away_stats['Passes_CmpPercentage'] = away_summary_stats[21]
        away_stats['Passes_PrgP'] = away_summary_stats[22]
        away_stats['Carries'] = away_summary_stats[23]
        away_stats['Carries_PrgC'] = away_summary_stats[24]
        away_stats['Take_Ons_Att'] = away_summary_stats[25]
        away_stats['Take_Ons_Succ'] = away_summary_stats[26]

#----------------------------------------------------------------Export--------------------------------------------------
        yield home_stats
        yield away_stats
        yield match_infos

#----------------------------------------------------------------Squad--------------------------------------------------
        player_names_in_squad_home = response.xpath('//div[@class = "lineup"][1]//td//a/text()').extract()
        home_kitnums = response.xpath('//div[@class = "lineup"][1]//td/text()').extract()

        player_names_in_squad_away = response.xpath('//div[@class = "lineup"][2]//td//a/text()').extract()
        away_kitnums =  response.xpath('//div[@class = "lineup"][2]//td/text()').extract()

        for index,(name, home_kitnum) in enumerate(zip(player_names_in_squad_home,home_kitnums)):
            home_squad  = fbref_MatchSquad()
            home_squad['fbrefMatchId'] = match_id
            home_squad['player_name'] = name
            home_squad['player_kitnum'] = home_kitnum
            home_squad['team'] = home_stats['team']
            home_squad['is_home_team'] = 'Yes'
            if index > 10:
                home_squad['is_sub'] = 'Yes'
            else:   home_squad['is_sub'] = 'No'
            yield home_squad

        for index,(name, away_kitnum) in enumerate(zip(player_names_in_squad_away,away_kitnums)):
            away_squad  = fbref_MatchSquad()
            away_squad['fbrefMatchId'] = match_id
            away_squad['player_name'] = name
            away_squad['player_kitnum'] = away_kitnum
            away_squad['team'] = away_stats['team']
            away_squad['is_home_team'] = 'No'
            if index > 10:
                away_squad['is_sub'] = 'Yes'
            else:   away_squad['is_sub'] = 'No'
            yield away_squad
#----------------------------------------------------------------Goals--------------------------------------------------
        home_goals = response.xpath('//div[@class="event" and @id="a"]/div[./div[@class = "event_icon goal"]]//text()').extract()
        home_goals = [goal\
                            .replace('&rsquor;','')\
                            .replace('\xa0','')\
                            .replace('\n','')\
                            .replace('\t','')\
                            for goal in home_goals]
        home_goals = [goal for goal in home_goals if (goal!='' and goal != ' ')]
        home_goals = [goal.replace(' · ','').replace(' (OG)','(OG)').replace(' (P)','(P)') for goal in home_goals]
        
        for i in range(0,len(home_goals)-1,2):
            match_goals = fbref_MatchGoals()
            match_goals['fbrefMatchId'] = match_id
            match_goals['player_name'] = home_goals[i]
            if '(OG)' in  home_goals[i+1]:
                match_goals['type_of_goal'] = "Own Goal"
                home_goals[i+1] = home_goals[i+1].replace('(OG)','')
            elif '(P)' in home_goals[i+1]:
                match_goals['type_of_goal'] = "Penalty"
                home_goals[i+1] = home_goals[i+1].replace('(P)','')
            else:
                match_goals['type_of_goal'] = "Normal"
            match_goals['team'] = home_stats['team']
            match_goals['minute'] = home_goals[i+1]
            match_goals['is_home_team'] = "Yes"

            yield match_goals

        away_goals = response.xpath('//div[@class="event" and @id="b"]/div//text()').extract()
        away_goals = [goal\
                            .replace('&rsquor;','')\
                            .replace('\xa0','')\
                            .replace('\n','')\
                            .replace('\t','')\
                            for goal in away_goals]
        away_goals = [goal for goal in away_goals if (goal!='' and goal != ' ')]
        away_goals = [goal.replace(' · ','').replace(' (OG)','(OG)').replace(' (P)','(P)') for goal in away_goals]
        
        for i in range(0,len(away_goals)-1,2):
            match_goals = fbref_MatchGoals()
            match_goals['fbrefMatchId'] = match_id
            match_goals['player_name'] = away_goals[i]
            if '(OG)' in  away_goals[i+1]:
                match_goals['type_of_goal'] = "Own Goal"
                away_goals[i+1] = away_goals[i+1].replace('(OG)','')
            elif '(P)' in away_goals[i+1]:
                match_goals['type_of_goal'] = "Penalty"
                away_goals[i+1] = away_goals[i+1].replace('(P)','')
            else:
                match_goals['type_of_goal'] = "Normal"
            match_goals['team'] = away_stats['team']
            match_goals['minute'] = away_goals[i+1]
            match_goals['is_home_team'] = "No"
            
            yield match_goals


#------------------------------------------------------------------PlayerInMatchStats-------------------------------------------------------------------------------
        for i in range(0,int(home_stats['total_players_stats'])):
            player_stats = fbref_MatchPlayerStats()
            player_stats['fbrefMatchId'] = match_id
            player_stats['player_name'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]/th/a/text()').get()
            player_stats['nationality'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="nationality"]/a/span/text()').get()
            player_stats['team'] = home_stats['team']
            player_stats['player_kitnum'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="shirtnumber"]/text()').get()
            player_stats['position'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="position"]/text()').get()
            player_stats['age'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="age"]/text()').get()
            player_stats['minutes'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="minutes"]/text()').get()
            player_stats['Gls'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="goals"]/text()').get()
            player_stats['Ast'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="assists"]/text()').get()
            player_stats['PK'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="pens_made"]/text()').get()
            player_stats['PKatt'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="pens_att"]/text()').get()
            player_stats['Sh'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="shots"]/text()').get()
            player_stats['SoT'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="shots_on_target"]/text()').get()
            player_stats['CrdY'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="cards_yellow"]/text()').get()
            player_stats['CrdR'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="cards_red"]/text()').get()
            player_stats['Touches'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="touches"]/text()').get()
            player_stats['Tkl'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="tackles"]/text()').get()
            player_stats['Int'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="interceptions"]/text()').get()
            player_stats['Blocks'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="blocks"]/text()').get()
            player_stats['xG'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="xg"]/text()').get()
            player_stats['npxG'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="npxg"]/text()').get()
            player_stats['xAG'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="xg_assist"]/text()').get()
            player_stats['SCA'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="sca"]/text()').get()
            player_stats['GCA'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="gca"]/text()').get()
            player_stats['Passes_Cmp'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="passes_completed"]/text()').get()
            player_stats['Passes_Att'] =response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="passes"]/text()').get()
            player_stats['Passes_CmpPercentage'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="passes_pct"]/text()').get()
            player_stats['Passes_PrgP'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="progressive_passes"]/text()').get()
            player_stats['Carries'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="carries"]/text()').get()
            player_stats['Carries_PrgC'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="progressive_carries"]/text()').get()
            player_stats['Take_Ons_Att'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="take_ons"]/text()').get()
            player_stats['Take_Ons_Succ'] = response.xpath(f'(//table[contains(@id, "summary")])[1]/tbody/tr[{i+1}]//td[@data-stat="take_ons_won"]/text()').get()
            yield player_stats

        for i in range(0,int(away_stats['total_players_stats'])):
            player_stats = fbref_MatchPlayerStats()
            away_player_row = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td/text()').extract()
            player_stats['fbrefMatchId'] = match_id
            player_stats['player_name'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]/th/a/text()').extract()
            player_stats['team'] = away_stats['team']
            player_stats['nationality'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="nationality"]/a/span/text()').get()
            player_stats['player_kitnum'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="shirtnumber"]/text()').get()
            player_stats['position'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="position"]/text()').get()
            player_stats['age'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="age"]/text()').get()
            player_stats['minutes'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="minutes"]/text()').get()
            player_stats['Gls'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="goals"]/text()').get()
            player_stats['Ast'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="assists"]/text()').get()
            player_stats['PK'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="pens_made"]/text()').get()
            player_stats['PKatt'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="pens_att"]/text()').get()
            player_stats['Sh'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="shots"]/text()').get()
            player_stats['SoT'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="shots_on_target"]/text()').get()
            player_stats['CrdY'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="cards_yellow"]/text()').get()
            player_stats['CrdR'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="cards_red"]/text()').get()
            player_stats['Touches'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="touches"]/text()').get()
            player_stats['Tkl'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="tackles"]/text()').get()
            player_stats['Int'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="interceptions"]/text()').get()
            player_stats['Blocks'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="blocks"]/text()').get()
            player_stats['xG'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="xg"]/text()').get()
            player_stats['npxG'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="npxg"]/text()').get()
            player_stats['xAG'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="xg_assist"]/text()').get()
            player_stats['SCA'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="sca"]/text()').get()
            player_stats['GCA'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="gca"]/text()').get()
            player_stats['Passes_Cmp'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="passes_completed"]/text()').get()
            player_stats['Passes_Att'] =response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="passes"]/text()').get()
            player_stats['Passes_CmpPercentage'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="passes_pct"]/text()').get()
            player_stats['Passes_PrgP'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="progressive_passes"]/text()').get()
            player_stats['Carries'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="carries"]/text()').get()
            player_stats['Carries_PrgC'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="progressive_carries"]/text()').get()
            player_stats['Take_Ons_Att'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="take_ons"]/text()').get()
            player_stats['Take_Ons_Succ'] = response.xpath(f'(//table[contains(@id, "summary")])[2]/tbody/tr[{i+1}]//td[@data-stat="take_ons_won"]/text()').get()
            yield player_stats

        

        
