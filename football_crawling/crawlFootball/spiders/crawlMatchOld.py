import scrapy
from crawlFootball.items import *
from crawlFootball.spiders.functions import *
class CrawlmatchSpider(scrapy.Spider):
    name = "crawlMatchOld"
    allowed_domains = ["www.transfermarkt.com"]
    start_urls = ["https://www.transfermarkt.com/premier-league/spieltagtabelle/wettbewerb/GB1",
                # "https://www.transfermarkt.com/laliga/spieltagtabelle/wettbewerb/ES1", 
                # "https://www.transfermarkt.com/bundesliga/spieltagtabelle/wettbewerb/L1",
                # "https://www.transfermarkt.com/serie-a/spieltagtabelle/wettbewerb/IT1",
                # "https://www.transfermarkt.com/ligue-1/spieltagtabelle/wettbewerb/FR1", 
                ]
    custom_settings = {
        'FEEDS':{
            'matches.csv':{'format':'csv','overwrite':True}
            },
        'LOG_STDOUT' : {True},
        "LOG_FILE" :'./scrapy_output.txt'
    }
    root_url = "https://www.transfermarkt.com"
    season = 2022
    numOfSeasons = 1
    #+'&spieltag=6'
    def parse(self, response):
        for url in self.start_urls:
            yield response.follow(url=url, callback=self.parse_on_seasons,
                                  meta = {'current_url':url}
                                  )
    def parse_on_seasons(self, response):
        for i in range(0,self.numOfSeasons):
            season = self.season - i
            current_url = response.meta.get('current_url')
            current_url += '?saison_id='+str(season)
            response.meta['current_url'] = current_url
            response.meta['season'] = season
            yield response.follow(url=current_url, callback=self.parse_on_matchdays,meta = response.meta)
    def parse_on_matchdays(self, response):
        numOfMatchDay = len(response.css('select[data-placeholder = "Einen Spieltag auswählen"] option').extract())
        current_url = response.meta.get('current_url')
        for i in range(1,numOfMatchDay):
            next_url = str(current_url)
            next_url += '&spieltag='+str(i)
            response.meta['current_url'] = next_url
            response.meta['match_day'] = i
            yield response.follow(url=next_url, callback=self.parse_on_matches, meta = response.meta)
    def parse_on_matches(self,response):
        match_urls = response.xpath('//a[span[@class = "matchresult finished"]]/@href').extract()
        for match_url in match_urls:
            current_url =  self.root_url + match_url
            response.meta['current_url'] = current_url
            yield response.follow(url=current_url, callback=self.parse_on_lineups, meta = response.meta)
        pass
    def parse_on_lineups(self,response):
        lineup_url = response.xpath('//a[text() = "Line-ups"]/@href').get()
        current_url = self.root_url + lineup_url
        formations = response.css("div[class ='large-7 aufstellung-vereinsseite columns small-12 unterueberschrift aufstellung-unterueberschrift']::text").extract()
        response.meta['current_url'] = current_url
        response.meta['formations'] = formations
        yield response.follow(url=current_url, callback=self.parse_on_matchsquad,meta = response.meta)
    def parse_on_matchsquad(self,response):        
        functions = Functions()
        matchSquad1 = MatchSquad()
        matchSquad2 = MatchSquad()
        current_url = response.meta.get('current_url')
        formations = response.meta.get('formations')

        player_start_urls = response.css('a.wichtig::attr(href)').extract()[0:22]
        player_start_ids = []
        for player_start_url in player_start_urls:
            id = functions.ExtractPlayerIdTransfermarkt(player_start_url)
            player_start_ids.append(id)
        player_start_names = response.css('a.wichtig::text').extract()[0:22]
        player_sub_team1_names = response.xpath('//div[@class="large-6 columns" and ./div/h2/text() = "Substitutes"][1]/div/div/table/tr/td/table/tr/td/a[@class = "wichtig"]/text()').extract()
        player_sub_team2_names = response.xpath('//div[@class="large-6 columns" and ./div/h2/text() = "Substitutes"][2]/div/div/table/tr/td/table/tr/td/a[@class = "wichtig"]/text()').extract()
        player_sub_team1_urls = response.xpath('//div[@class="large-6 columns" and ./div/h2/text() = "Substitutes"][1]/div/div/table/tr/td/table/tr/td/a[@class = "wichtig"]/@href').extract()
        player_sub_team2_urls = response.xpath('//div[@class="large-6 columns" and ./div/h2/text() = "Substitutes"][2]/div/div/table/tr/td/table/tr/td/a[@class = "wichtig"]/@href').extract()
        

        player_sub_team1_ids = []
        player_sub_team2_ids = []
        for player_sub_team1_url in player_sub_team1_urls:
            id = functions.ExtractPlayerIdTransfermarkt(player_sub_team1_url)
            player_sub_team1_ids.append(id)
        for player_sub_team2_url in player_sub_team2_urls:
            id = functions.ExtractPlayerIdTransfermarkt(player_sub_team2_url)
            player_sub_team2_ids.append(id)
        
        for i in range(len(player_sub_team1_names),20):
            player_sub_team1_names.append('')
            player_sub_team1_ids.append('')

        for i in range(len(player_sub_team2_names),20):
            player_sub_team2_names.append('')
            player_sub_team2_ids.append('')



        matchSquad1_url = response.css('a[class = "sb-vereinslink"]::attr(href)').extract()[0]
        matchSquad2_url = response.css('a[class = "sb-vereinslink"]::attr(href)').extract()[1]
        matchSquad1['transfermarktMatchId'] = functions.ExtractMatchIdFromTransfermarkt(current_url)
        matchSquad1['match_day'] = response.meta.get('match_day')
        matchSquad1['date'] = response.css('p[class = "sb-datum hide-for-small"] a::text').extract()[1]
        matchSquad1['date'] = functions.RemoveAllExtraSpaceAndEnter(matchSquad1['date'])
        matchSquad1['date'] = functions.ConvertTransfermarktMatchDay(matchSquad1['date'])
        matchSquad1['season'] = response.meta.get('season')
        matchSquad1['team_id'] = functions.ExtractTeamIdFromTransfermarkt(matchSquad1_url)
        matchSquad1['team_name'] = response.css('a[class = "sb-vereinslink"]::text').extract()[0]
        matchSquad1['leauge'] = response.css('a[class = direct-headline__link]::text').extract()[0]
        matchSquad1['formation'] = formations[0]
        matchSquad1['formation'] = str(functions.RemoveNotUsedCharInFormation(matchSquad1['formation']))
        matchSquad1['player1'] = player_start_names[0]
        matchSquad1['player2'] = player_start_names[1]
        matchSquad1['player3'] = player_start_names[2]
        matchSquad1['player4'] = player_start_names[3]
        matchSquad1['player5'] = player_start_names[4]
        matchSquad1['player6'] = player_start_names[5]
        matchSquad1['player7'] = player_start_names[6]
        matchSquad1['player8'] = player_start_names[7]
        matchSquad1['player9'] = player_start_names[8]
        matchSquad1['player10'] = player_start_names[9]
        matchSquad1['player11'] = player_start_names[10]
        matchSquad1['sub1'] = player_sub_team1_names[0]
        matchSquad1['sub2'] = player_sub_team1_names[1]
        matchSquad1['sub3'] = player_sub_team1_names[2]
        matchSquad1['sub4'] = player_sub_team1_names[3]
        matchSquad1['sub5'] = player_sub_team1_names[4]
        matchSquad1['sub6'] = player_sub_team1_names[5]
        matchSquad1['sub7'] = player_sub_team1_names[6]
        matchSquad1['sub8'] = player_sub_team1_names[7]
        matchSquad1['sub9'] = player_sub_team1_names[8]
        matchSquad1['sub10'] = player_sub_team1_names[9]
        matchSquad1['sub11'] = player_sub_team1_names[10]
        matchSquad1['sub12'] = player_sub_team1_names[11]
        matchSquad1['sub13'] = player_sub_team1_names[12]
        matchSquad1['sub14'] = player_sub_team1_names[13]
        matchSquad1['sub15'] = player_sub_team1_names[14]
        matchSquad1['sub16'] = player_sub_team1_names[15]
        matchSquad1['sub17'] = player_sub_team1_names[16]
        matchSquad1['sub18'] = player_sub_team1_names[17]
        matchSquad1['sub19'] = player_sub_team1_names[18]
        matchSquad1['sub20'] = player_sub_team1_names[19]
        

        matchSquad1['transfermarktId_player1'] = player_start_ids[0]
        matchSquad1['transfermarktId_player2'] = player_start_ids[1]
        matchSquad1['transfermarktId_player3'] = player_start_ids[2]
        matchSquad1['transfermarktId_player4'] = player_start_ids[3]
        matchSquad1['transfermarktId_player5'] = player_start_ids[4]
        matchSquad1['transfermarktId_player6'] = player_start_ids[5]
        matchSquad1['transfermarktId_player7'] = player_start_ids[6]
        matchSquad1['transfermarktId_player8'] = player_start_ids[7]
        matchSquad1['transfermarktId_player9'] = player_start_ids[8]
        matchSquad1['transfermarktId_player10'] = player_start_ids[9]
        matchSquad1['transfermarktId_player11'] = player_start_ids[10]
        matchSquad1['transfermarktId_sub1'] = player_sub_team1_ids[0]
        matchSquad1['transfermarktId_sub2'] = player_sub_team1_ids[1]
        matchSquad1['transfermarktId_sub3'] = player_sub_team1_ids[2]
        matchSquad1['transfermarktId_sub4'] = player_sub_team1_ids[3]
        matchSquad1['transfermarktId_sub5'] = player_sub_team1_ids[4]
        matchSquad1['transfermarktId_sub6'] = player_sub_team1_ids[5]
        matchSquad1['transfermarktId_sub7'] = player_sub_team1_ids[6]
        matchSquad1['transfermarktId_sub8'] = player_sub_team1_ids[7]
        matchSquad1['transfermarktId_sub9'] = player_sub_team1_ids[8]
        matchSquad1['transfermarktId_sub10'] = player_sub_team1_ids[9]
        matchSquad1['transfermarktId_sub11'] = player_sub_team1_ids[10]
        matchSquad1['transfermarktId_sub12'] = player_sub_team1_ids[11]
        matchSquad1['transfermarktId_sub13'] = player_sub_team1_ids[12]
        matchSquad1['transfermarktId_sub14'] = player_sub_team1_ids[13]
        matchSquad1['transfermarktId_sub15'] = player_sub_team1_ids[14]
        matchSquad1['transfermarktId_sub16'] = player_sub_team1_ids[15]
        matchSquad1['transfermarktId_sub17'] = player_sub_team1_ids[16]
        matchSquad1['transfermarktId_sub18'] = player_sub_team1_ids[17]
        matchSquad1['transfermarktId_sub19'] = player_sub_team1_ids[18]
        matchSquad1['transfermarktId_sub20'] = player_sub_team1_ids[19]

        yield matchSquad1
        
        matchSquad2['transfermarktMatchId'] = matchSquad1['transfermarktMatchId']
        matchSquad2['match_day'] = matchSquad1['match_day']
        matchSquad2['date'] = matchSquad1['date']
        matchSquad2['season'] = matchSquad1['season']
        matchSquad2['team_id'] = functions.ExtractTeamIdFromTransfermarkt(matchSquad2_url)
        matchSquad2['team_name'] =  response.css('a[class = "sb-vereinslink"]::text').extract()[1]
        matchSquad2['leauge'] = matchSquad1['leauge']

        matchSquad2['formation'] = formations[1]
        matchSquad2['formation'] = str(functions.RemoveNotUsedCharInFormation(matchSquad2['formation']))
        
        matchSquad2['player1'] = player_start_names[11]
        matchSquad2['player2'] = player_start_names[12] 
        matchSquad2['player3'] = player_start_names[13]
        matchSquad2['player4'] = player_start_names[14]
        matchSquad2['player5'] = player_start_names[15]
        matchSquad2['player6'] = player_start_names[16]
        matchSquad2['player7'] = player_start_names[17]
        matchSquad2['player8'] = player_start_names[18]
        matchSquad2['player9'] = player_start_names[19]
        matchSquad2['player10'] = player_start_names[20]
        matchSquad2['player11'] = player_start_names[21]
        matchSquad2['sub1'] = player_sub_team2_names[0]
        matchSquad2['sub2'] = player_sub_team2_names[1]
        matchSquad2['sub3'] = player_sub_team2_names[2]
        matchSquad2['sub4'] = player_sub_team2_names[3]
        matchSquad2['sub5'] = player_sub_team2_names[4]
        matchSquad2['sub6'] = player_sub_team2_names[5]
        matchSquad2['sub7'] = player_sub_team2_names[6]
        matchSquad2['sub8'] = player_sub_team2_names[7]
        matchSquad2['sub9'] = player_sub_team2_names[8]
        matchSquad2['sub10'] = player_sub_team2_names[9]
        matchSquad2['sub11'] = player_sub_team2_names[10]
        matchSquad2['sub12'] = player_sub_team2_names[11]
        matchSquad2['sub13'] = player_sub_team2_names[12]
        matchSquad2['sub14'] = player_sub_team2_names[13]
        matchSquad2['sub15'] = player_sub_team2_names[14]
        matchSquad2['sub16'] = player_sub_team2_names[15]
        matchSquad2['sub17'] = player_sub_team2_names[16]
        matchSquad2['sub18'] = player_sub_team2_names[17]
        matchSquad2['sub19'] = player_sub_team2_names[18]
        matchSquad2['sub20'] = player_sub_team2_names[19]


        matchSquad2['transfermarktId_player1'] = player_start_ids[11]
        matchSquad2['transfermarktId_player2'] = player_start_ids[12]
        matchSquad2['transfermarktId_player3'] = player_start_ids[13]
        matchSquad2['transfermarktId_player4'] = player_start_ids[14]
        matchSquad2['transfermarktId_player5'] = player_start_ids[15]
        matchSquad2['transfermarktId_player6'] = player_start_ids[16]
        matchSquad2['transfermarktId_player7'] = player_start_ids[17]
        matchSquad2['transfermarktId_player8'] = player_start_ids[18]
        matchSquad2['transfermarktId_player9'] = player_start_ids[19]
        matchSquad2['transfermarktId_player10'] = player_start_ids[20]
        matchSquad2['transfermarktId_player11'] = player_start_ids[21]
        matchSquad2['transfermarktId_sub1'] = player_sub_team2_ids[0]
        matchSquad2['transfermarktId_sub2'] = player_sub_team2_ids[1]
        matchSquad2['transfermarktId_sub3'] = player_sub_team2_ids[2]
        matchSquad2['transfermarktId_sub4'] = player_sub_team2_ids[3]
        matchSquad2['transfermarktId_sub5'] = player_sub_team2_ids[4]
        matchSquad2['transfermarktId_sub6'] = player_sub_team2_ids[5]
        matchSquad2['transfermarktId_sub7'] = player_sub_team2_ids[6]
        matchSquad2['transfermarktId_sub8'] = player_sub_team2_ids[7]
        matchSquad2['transfermarktId_sub9'] = player_sub_team2_ids[8]
        matchSquad2['transfermarktId_sub10'] = player_sub_team2_ids[9]
        matchSquad2['transfermarktId_sub11'] = player_sub_team2_ids[10]
        matchSquad2['transfermarktId_sub12'] = player_sub_team2_ids[11]
        matchSquad2['transfermarktId_sub13'] = player_sub_team2_ids[12]
        matchSquad2['transfermarktId_sub14'] = player_sub_team2_ids[13]
        matchSquad2['transfermarktId_sub15'] = player_sub_team2_ids[14]
        matchSquad2['transfermarktId_sub16'] = player_sub_team2_ids[15]
        matchSquad2['transfermarktId_sub17'] = player_sub_team2_ids[16]
        matchSquad2['transfermarktId_sub18'] = player_sub_team2_ids[17]
        matchSquad2['transfermarktId_sub19'] = player_sub_team2_ids[18]
        matchSquad2['transfermarktId_sub20'] = player_sub_team2_ids[19]

        yield matchSquad2
        