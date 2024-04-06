import scrapy
from crawlFootball.items import *
from crawlFootball.spiders.functions import *
class CrawlsquadSpider(scrapy.Spider):
    name = "crawlSquad"
    allowed_domains = ["transfermarkt.com"]
    start_urls = ["https://www.transfermarkt.com/premier-league/startseite/wettbewerb/GB1/plus/",
                  "https://www.transfermarkt.com/bundesliga/startseite/wettbewerb/L1",
                  "https://www.transfermarkt.com/laliga/startseite/wettbewerb/ES1",
                  "https://www.transfermarkt.com/serie-a/startseite/wettbewerb/IT1",
                  "https://www.transfermarkt.com/ligue-1/startseite/wettbewerb/FR1",
                  ]
    root_url = "http://www.transfermarkt.com"
    season = 2023
    # numOfSeasons = 32
    numOfSeasons = 1
    custom_settings = {
        'FEEDS':{
            'squad.csv':{'format':'csv','overwrite':True}
            },
        'LOG_STDOUT' : {True},
        "LOG_FILE" :'./scrapy_output.txt'
    }
    def parse(self, response):
        for start_url in self.start_urls:
            yield response.follow(url=start_url, callback=self.parse_on_season,
                                  meta = {'current_url': start_url})
    def parse_on_season(self, response):
        for numOfSeason in range(0,self.numOfSeasons):
            season = self.season - numOfSeason
            current_url = response.meta.get('current_url')
            current_url +='?saison='+str(season)
            yield response.follow(url=current_url, callback=self.parse_on_team,
                                  meta = {
                                      'season':season,
                                      'current_url':current_url
                                  })
    def parse_on_team(self,response):
        teams = response.xpath('//td[@class = "hauptlink no-border-links"]/a[@title]/@href').extract()
        team_titles = response.xpath('//td[@class = "hauptlink no-border-links"]/a[@title]/@title').extract()
        i= 0
        for team in teams:
            response.meta['team_title'] = team_titles[i]
            response.meta['current_url'] = self.root_url+team
            yield response.follow(url=response.meta['current_url'], callback=self.parse_squad,
                                 meta = response.meta
                                 )
            i = i+1

    def parse_squad(self,response):
        players = response.xpath('//td[@class = "hauptlink span-va-middle"]/a/@href').extract()
        for player in players:
            response_meta = response.meta
            response_meta['current_url'] = self.root_url+player
            yield response.follow(url=response_meta['current_url'], callback=self.parse_player,
                                 meta=response_meta
                                 )
    def parse_player(self,response):
        current_url = response.meta.get('current_url')
        functions = Functions()
        teamSquad = TeamSquad()
        player_shortName = response.xpath('//h1[@class="data-header__headline-wrapper"]/text()[normalize-space()]').get()
        player_shortName+=response.css('h1[class= data-header__headline-wrapper] strong::text').get()
        player_shortName = functions.RemoveAllExtraSpaceAndEnter(player_shortName)
        teamSquad['player_shortName'] = player_shortName
        
        player_fullName = response.xpath('//div[span[starts-with(text(), "Full name:")]]/span[@class = "info-table__content info-table__content--bold"]/text()').get()
        if player_fullName is None or player_fullName == '':
            player_fullName = response.xpath('//div[span[starts-with(text(), "Name in home country:")]]/span[@class = "info-table__content info-table__content--bold"]/text()').get()
        if player_fullName is None or player_fullName == '':
            teamSquad['player_fullName'] = player_shortName
        else:
            teamSquad['player_fullName'] = player_fullName

        teamSquad['player_transfermarktId'] = functions.ExtractTransfermarktIdFromURL(current_url)
        teamSquad['birthday']= response.css('span[class = "info-table__content info-table__content--bold"] a::text').extract()[0]
        teamSquad['birthday']= functions.ConvertUpdateDate(teamSquad['birthday'])
        teamSquad['team'] = response.meta.get('team_title')
        teamSquad['position'] = response.xpath("//li[starts-with(text(), 'Position:')]/span/text()").get()
        teamSquad['position'] = functions.RemoveAllExtraSpaceAndEnter(teamSquad['position'])
        teamSquad['season'] = response.meta.get('season')
        yield teamSquad
