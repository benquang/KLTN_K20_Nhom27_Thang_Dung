import scrapy
from crawlFootball.items import *
from crawlFootball.spiders.functions import *
class CrawlplayerstatsSpider(scrapy.Spider):
    name = "crawlPlayerStats"
    allowed_domains = ["sofifa.com"]

    custom_settings = {
        'FEEDS':{
            'player_attr.csv':{'format':'csv','overwrite':True}
            },
        'LOG_STDOUT' : {True},
        "LOG_FILE" :'./scrapy_output.txt'
    }
    start_urls = ["https://sofifa.com/"]
    start_url = "https://www.sofifa.com/"
    # leauges = ['13',#Premier Leauge
    #           '16',#Leauge 1
    #           '19',#Bundesliga
    #           '31',#Seria A
    #           '53'#La Liga
    #           ]
    # numOfVersions = 10
    # version = 230053
    leauges = ['13']#Premier Leauge

    numOfVersions = 1
    version = 230054
    
    def parse(self, response):
        currentURL = self.start_url
        currentURL = self.AddFilterToURL(currentURL)
        yield response.follow(currentURL,callback = self.parse_on_versions,
                              meta = {'currentURL':currentURL}
                              )
    def AddFilterToURL(self, url):
        url += '?type=all'
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
        players = response.css('td[class="col-name"] a[role="tooltip"][data-tip-pos = "top"]::attr(href)').extract()
        for player in players:
            yield response.follow(self.start_url+player,callback = self.parse_on_players,
                                    meta = {'player':player}
                                    )
        next_page_url = response.xpath('//a[@class="bp3-button bp3-intent-primary pjax" and ./span/text() = "Next"]/@href').get()
        # if (next_page_url!=''):
        if (next_page_url is not None):
            yield response.follow(self.start_url+next_page_url,callback = self.parse_on_pages,
                                    meta = {'currentURL':next_page_url}
                                    )
        
    def parse_on_players(self,response):
        functions = Functions()

        playerStats = PlayerStats()
        workRates = response.xpath('//li[@class = "ellipsis" and ./label/text()="Work rate"]/span/text()').get()
        workRates = functions.ExtractWorkRates(workRates)
        playerStats['attacking_work_rate'] = workRates[0]
        playerStats['defensive_work_rate'] = workRates[1]
        ratings = response.xpath('//div[./div[@class="sub"]]/span/text()').extract()
        playerStats['overall_rating'] = ratings[0]
        playerStats['potential'] = ratings[1]
        playerStats['player_fifaId'] = response.xpath('//li[@class = "ellipsis" and ./label/text()="ID"]/text()').get()
        playerStats['preferred_foot'] = response.xpath('//li[@class = "ellipsis" and ./label/text()="Preferred foot"]/text()').get()
        playerStats['position'] = response.xpath('//li[label[text() = "Best Position"]]/span/text()').get()
        playerStats['position'] = playerStats['position'].replace(" ", "")
        playerStats['weak_foot'] = response.xpath('//li[./label/text() = "Weak foot"]/text()').get()
        updateDate = response.css('span[class="bp3-button-text"]::text').extract()[1]
        updateDate = functions.ConvertUpdateDate(updateDate)
        playerStats['update_date'] = updateDate
        stats = response.xpath('//li[./span[@role="tooltip"]]/span[not(@role="tooltip")]/text()').extract()
        playerStats['crossing'] = stats[0]
        playerStats['finishing'] = stats[1]
        playerStats['heading_accuracy'] = stats[2]
        playerStats['short_passing'] = stats[3]
        playerStats['volleys'] = stats[4]
        playerStats['dribbling'] = stats[5]
        playerStats['curve'] = stats[6]
        playerStats['fk_accuracy'] = stats[7]
        playerStats['long_passing'] = stats[8]
        playerStats['ball_control'] = stats[9]
        playerStats['acceleration'] = stats[10]
        playerStats['sprint_speed'] = stats[11]
        playerStats['agility'] = stats[12]
        playerStats['reactions'] = stats[13]
        playerStats['balance'] = stats[14]
        playerStats['shot_power'] = stats[15]
        playerStats['jumping'] = stats[16]
        playerStats['stamina'] = stats[17]
        playerStats['strength'] = stats[18]
        playerStats['long_shots'] = stats[19]
        playerStats['aggression'] = stats[20]
        playerStats['interceptions'] = stats[21]
        playerStats['positioning'] = stats[22]
        playerStats['vision'] = stats[23]
        playerStats['penalties'] = stats[24]
        playerStats['composure'] = stats[25]
        playerStats['defensive_awareness'] = stats[26]
        playerStats['standing_tackle'] = stats[27]
        playerStats['sliding_tackle'] = stats[28]
        playerStats['gk_diving'] = stats[29]
        playerStats['gk_handling'] = stats[30]
        playerStats['gk_kicking'] = stats[31]
        playerStats['gk_positioning'] = stats[32]
        playerStats['gk_reflexes'] = stats[33]

        yield playerStats
