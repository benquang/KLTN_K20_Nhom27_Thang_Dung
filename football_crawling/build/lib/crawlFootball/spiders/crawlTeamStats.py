import scrapy
from crawlFootball.items import *
from crawlFootball.spiders.functions import *

class CrawlteamstatsSpider(scrapy.Spider):
    name = "crawlTeamStats"
    allowed_domains = ["sofifa.com"]
    start_urls = ["https://sofifa.com/"]
    start_url = "https://www.sofifa.com/"
    custom_settings = {
        'FEEDS':{
            'team_attr.csv':{'format':'csv','overwrite':True}
            },
        # 'LOG_STDOUT' : {True},
        # "LOG_FILE" :'./scrapy_output.txt'
    }

    # leauges = ['13',#Premier Leauge
    #           '16',#Leauge 1
    #           '19',#Bundesliga
    #           '31',#Seria A
    #           '53'#La Liga
    #           ]
    # numOfVersions = 10
    # version = 230053
    leauges = ['13']
    numOfVersions = 1
    version = 230054
    def parse(self, response):
        currentURL = self.start_url
        currentURL = self.AddFilterToURL(currentURL)
        yield response.follow(currentURL,callback = self.parse_on_versions,
                              meta = {'currentURL':currentURL}
                              )
        
    def AddFilterToURL(self,url):
        url += '/teams?type=all'
        for leauge in self.leauges:
            url+='&lg%5B%5D='+leauge
        return url
    def parse_on_versions(self,response):
        for i in range(0,self.numOfVersions):
            currentURL=response.meta.get('currentURL')
            currentVersion = self.version-i
            currentURL = currentURL+'&set=true&r='+str(currentVersion)
            yield response.follow(currentURL,callback = self.parse_on_pages,
                                meta = {'currentURL':currentURL}
                                )
    def parse_on_pages(self,response):
        teams = response.xpath("//td[@class = 'col-name-wide']/div/a[not(@rel)]/@href").extract()
        for team in teams:
            currentURL = self.start_url
            currentURL += team
            yield response.follow(currentURL,callback = self.parse_on_team,meta = {'currentURL':currentURL})

    def parse_on_team(self,response):
        teamStats = TeamStats()
        functions = Functions()
        currentURL = response.meta.get('currentURL')
        teamStats['team_id'] =  functions.ExtractTeamIdsFromURL(currentURL)
        teamStats['team_name'] =response.css('h1::text').get()
        teamStats['leauge'] = response.css('div [class = "meta ellipsis"] a:not([title])::text').get()
        teamStats['update_date'] = response.css('span[class="bp3-button-text"]::text').extract()[1]
        teamStats['update_date'] = functions.ConvertUpdateDate(teamStats['update_date'])
        stat = response.css('div[class = block-quarter] div span::text').extract()
        teamStats['overall'] = stat[0]
        teamStats['attack'] = stat[1]
        teamStats['midfield'] = stat[2]
        teamStats['defence'] = stat[3]

        tatics = response.xpath("//div[@class = 'card' and ./h5/text() = 'Tactics']/dl/dd/span/span/text()").extract()

        teamStats['defensive_style'] = tatics[0]
        teamStats['defence_width'] = tatics[1]
        teamStats['defence_depth'] = tatics[2]
        teamStats['build_up_play'] =  tatics[3]
        teamStats['chance_creation'] = tatics[4]
        teamStats['offense_width'] = tatics[5]
        teamStats['players_in_box'] = tatics[6]
        teamStats['corners'] = tatics[7]
        teamStats['free_kicks'] = tatics[8]
        yield teamStats
