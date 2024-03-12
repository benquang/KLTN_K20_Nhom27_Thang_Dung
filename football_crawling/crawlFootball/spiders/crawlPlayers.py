import scrapy
import pandas as pd
import os
import pandas as pd
from crawlFootball.items import *
from crawlFootball.spiders.functions import *
class CrawlplayersSpider(scrapy.Spider):
    name = "crawlPlayers"
    allowed_domains = ["sofifa.com"]

    custom_settings = {
        'FEEDS':{
            'player_attr.csv':{'format':'csv','overwrite':True}
            },
        # 'LOG_STDOUT' : {True},
        # "LOG_FILE" :'./scrapy_output.txt',
        'DOWNLOAD_DELAY' : 0.5,
        'CONCURRENT_REQUESTS' : 8,
    }
    start_urls = ["https://sofifa.com"]
    start_url = "https://www.sofifa.com"

    numOfVersions = 11
    
    def parse(self, response):
        current_url = self.start_url
        current_url = self.AddFilterToURL(current_url)
        yield response.follow(current_url,callback = self.parse_on_versions,
                              meta = {'current_url':current_url}
                              )
    def AddFilterToURL(self, url):
        url += '/?type=all'
        for leauge in self.leauges:
            url+='&lg%5B%5D='+leauge
        return url
    def parse_on_versions(self,response):
        versions = response.xpath('//h2/div[1]/div[@class="bp3-menu"]/a/@href').extract()
        versions = versions[0:self.numOfVersions]
        
        for version in versions:
            current_url = self.start_url+version
            yield response.follow(current_url,callback = self.parse_on_updates,
                                meta = {'current_url':current_url}
                                )
    
    def parse_on_updates(self,response):
        function = Functions()
        update_urls = response.xpath('//h2/div[2]/div[@class="bp3-menu"]/a/@href').extract()
        update_dates = response.xpath('//h2/div[2]/div[@class="bp3-menu"]/a/text()').extract()
        update = pd.DataFrame({'url':update_urls,'date':update_dates})
        update = function.GetFirstDaysOfEachMonth(update)
        next_urls = update['url'].tolist()
        for next_url in next_urls:
            yield response.follow(self.start_url+next_url,callback = self.parse_on_pages,
                                    meta = {'current_url':self.start_url+next_url}
                                    )


    def parse_on_pages(self,response):
        players = response.css('td[class="col-name"] a[role="tooltip"]
                                  [data-tip-pos = "top"]::attr(href)').extract()
        for player in players:
            yield response.follow(self.start_url+player,callback = self.parse_on_players,
                                  meta = {'current_url':self.start_url+player}
                                  )
        next_page_url = response.xpath('//a[@class="bp3-button bp3-intent-primary pjax" 
                                        and ./span/text() = "Next"]/@href').get()
        # if (next_page_url!=''):
        if (next_page_url is not None):
            yield response.follow(self.start_url+next_page_url,callback = self.parse_on_pages,
                                    meta = {'current_url':next_page_url}
                                    )
    
    def parse_on_players(self, response):
        functions = Functions()
        player = Player()
        
        player['update_date'] = response.xpath('//div[@class="dropdown"][2]
                                                /a/span/text()').extract()
        all_positions = response.xpath('//div[@class = "meta ellipsis"]
                                        /span/text()').extract()
        player['all_positions'] =''
        for i,position in enumerate(all_positions):
            player['all_positions'] += position
            if i!=len(all_positions)-1:
                player['all_positions'] += ' '
        
        player['player_full_name'] = response.css("div[class= info] 
                                                   h1::text").extract()
        player['player_name'] = response.css("h1::text").get()
        player['nationality'] = response.css('div[class = "meta ellipsis"] 
                                              a::attr(title)').get()
        infos = response.xpath('//div[@class="info"]/div/text()').extract()
        infos = infos[-1]
        infos = functions.ExtractInfosString(infos)
        player['age'] = infos[0]
        player['birthday'] = infos[1]
        player['height'] = infos[2]
        player['weight'] = infos[3]
        ratings = response.xpath('//div[./div[@class="sub"]]/span/text()').extract()
        player['overall_rating'] = ratings[0]
        player['potential'] = ratings[1]
        player['value'] = response.xpath('//div[./div[@class="sub"]
                                          /text()="Value"]/text()').get()
        player['wage'] = response.xpath('//div[./div[@class="sub"]
                                          /text()="Wage"]/text()').get()

        #Profile
        player['preferred_foot'] = response.xpath('//li[@class = "ellipsis" 
                                                   and ./label/text()="Preferred foot"]
                                                   /text()').get()
        player['skill_moves'] = response.xpath('//li[@class = "ellipsis" 
                                                and ./label/text()="Skill moves"]
                                                /text()').get()[0]
        player['weak_foot'] = response.xpath('//li[@class = "ellipsis" 
                                            and ./label/text()="Weak foot"]
                                            /text()').get()[0]
        player['reputation'] = response.xpath('//li[@class = "ellipsis" 
                                            and ./label/text()="International reputation"]
                                            /text()').get()[0]
        
        workRates = response.xpath('//li[@class = "ellipsis" 
                                            and ./label/text()="Work rate"]/span/text()').get()
        workRates = functions.ExtractWorkRates(workRates)
        player['attacking_work_rate'] = workRates[0]
        player['defensive_work_rate'] = workRates[1]
        player['body_type'] = response.xpath('//li[@class = "ellipsis" 
                                                and ./label/text()="Body type"]/span/text()').get()
        player['real_face'] = response.xpath('//li[@class = "ellipsis" 
                                                and ./label/text()="Real face"]/span/text()').get()
        player['sofifa_id'] = response.xpath('//li[@class = "ellipsis" 
                                                and ./label/text()="ID"]/text()').get()

        #Specialities //div[@class = "card" and ./h5/text()="Player specialities"]/ul/li/a/text()
        specialities = response.xpath('//div[@class = "card" 
                                        and ./h5/text()="Player specialities"]/ul/li/a/text()').extract()
        player['specialities'] = ''
        for speciality in specialities:
            player['specialities']+=speciality
        #Teams
        teams = response.xpath("//div[@class='center'][1]//div[@class = 'card']/h5/a/text()").extract()
        player['team1'] = teams[0]
        player['team1'] = player['team1'][1:]
        player['team1_rating'] = response.xpath('//ul[@class = "ellipsis pl"]/li[1]/span/text()').get()
        player['team1_position'] = response.xpath('(//ul[@class = "ellipsis pl"]/li[./label/text()="Position"]
                                                    /span/text())[1]').get()
        player['team1_kitnum']=response.xpath('(//ul[@class = "ellipsis pl"]/li[./label/text()="Kit number"]
                                                /text())[1]').get()
        player['team1_loaned_from']=response.xpath('(//ul[@class = "ellipsis pl"]/li[./label/text()="Loaned from"]
                                                /a/text())[1]').get()
        player['team1_joined'] = response.xpath('(//ul[@class = "ellipsis pl"]/li[./label/text()="Joined"]
                                                /text())[1]').get()
        player['team1_contract'] = response.xpath('(//ul[@class = "ellipsis pl"]/li[./label/text()="Contract valid until"]
                                                /text())[1]').get()
        if (len(teams)>1):
            player['team2'] = teams[1]
            player['team2'] = player['team2'][1:]
            player['team2_rating'] = response.xpath('//ul[@class = "ellipsis pl"]/li[1]/span/text()').extract()[1]
            player['team2_position'] = response.xpath('(//ul[@class = "ellipsis pl"]/li[./label/text()="Position"]
                                                        /span/text())[2]').get()
            player['team2_kitnum']=response.xpath('(//ul[@class = "ellipsis pl"]/li[./label/text()="Kit number"]
                                                    /text())[2]').get()
        
        updateDate = response.css('span[class="bp3-button-text"]::text').extract()[1]
        updateDate = functions.ConvertUpdateDate(updateDate)
        player['update_date'] = updateDate
        #Attacking
        player['crossing'] = response.xpath('//ul/li[./span/text()="Crossing"]/span[1]/text()').get()
        player['finishing'] = response.xpath('//ul/li[./span/text()="Finishing"]/span[1]/text()').get()
        player['heading_accuracy'] = response.xpath('//ul/li[./span/text()="Heading accuracy"]/span[1]/text()').get()
        player['short_passing'] = response.xpath('//ul/li[./span/text()="Short passing"]/span[1]/text()').get()
        player['volleys'] = response.xpath('//ul/li[./span/text()="Volleys"]/span[1]/text()').get()
        #Skill
        player['dribbling'] = response.xpath('//ul/li[./span/text()="Dribbling"]/span[1]/text()').get()
        player['curve'] = response.xpath('//ul/li[./span/text()="Curve"]/span[1]/text()').get()
        player['fk_accuracy'] = response.xpath('//ul/li[./span/text()="FK Accuracy"]/span[1]/text()').get()
        player['long_passing'] = response.xpath('//ul/li[./span/text()="Long passing"]/span[1]/text()').get()
        player['ball_control'] = response.xpath('//ul/li[./span/text()="Ball control"]/span[1]/text()').get()
        #Movement
        player['acceleration'] = response.xpath('//ul/li[./span/text()="Acceleration"]/span[1]/text()').get()
        player['sprint_speed'] = response.xpath('//ul/li[./span/text()="Sprint speed"]/span[1]/text()').get()
        player['agility'] = response.xpath('//ul/li[./span/text()="Agility"]/span[1]/text()').get()
        player['reactions'] = response.xpath('//ul/li[./span/text()="Reactions"]/span[1]/text()').get()
        player['balance'] = response.xpath('//ul/li[./span/text()="Balance"]/span[1]/text()').get()
        #Power
        player['shot_power'] = response.xpath('//ul/li[./span/text()="Shot power"]/span[1]/text()').get()
        player['jumping'] = response.xpath('//ul/li[./span/text()="Jumping"]/span[1]/text()').get()
        player['stamina'] = response.xpath('//ul/li[./span/text()="Stamina"]/span[1]/text()').get()
        player['strength'] = response.xpath('//ul/li[./span/text()="Strength"]/span[1]/text()').get()
        player['long_shots'] = response.xpath('//ul/li[./span/text()="Long shots"]/span[1]/text()').get()
        #Mentality
        player['aggression'] = response.xpath('//ul/li[./span/text()="Aggression"]/span[1]/text()').get()
        player['interceptions'] = response.xpath('//ul/li[./span/text()="Interceptions"]/span[1]/text()').get()
        player['positioning'] = response.xpath('//ul/li[./span/text()="Positioning"]/span[1]/text()').get()
        player['vision'] = response.xpath('//ul/li[./span/text()="Vision"]/span[1]/text()').get()
        player['penalties'] = response.xpath('//ul/li[./span/text()="Penalties"]/span[1]/text()').get()
        player['composure'] = response.xpath('//ul/li[./span/text()="Composure"]/span[1]/text()').get()
        #DEFENDING
        player['marking'] = response.xpath('//ul/li[./span/text()="Marking"]/span[1]/text()').get()
        player['defensive_awareness'] = response.xpath('//ul/li[./span/text()="Defensive awareness"]/span[1]/text()').get()
        player['standing_tackle'] = response.xpath('//ul/li[./span/text()="Standing tackle"]/span[1]/text()').get()
        player['sliding_tackle'] = response.xpath('//ul/li[./span/text()="Sliding tackle"]/span[1]/text()').get()
        #GOALKEEPING
        player['gk_diving'] = response.xpath('//ul/li[./span/text()="GK Diving"]/span[1]/text()').get()
        player['gk_handling'] = response.xpath('//ul/li[./span/text()="GK Handling"]/span[1]/text()').get()
        player['gk_kicking'] = response.xpath('//ul/li[./span/text()="GK Kicking"]/span[1]/text()').get()
        player['gk_positioning'] = response.xpath('//ul/li[./span/text()="GK Positioning"]/span[1]/text()').get()
        player['gk_reflexes'] = response.xpath('//ul/li[./span/text()="GK Reflexes"]/span[1]/text()').get()

        traits = response.xpath('//div[./h5/text()="Traits"]/ul/li/span/text()').extract()
        player['traits'] = ''
        for trait in traits:
            player['traits']+='#'
            player['traits']+=trait
        yield player


