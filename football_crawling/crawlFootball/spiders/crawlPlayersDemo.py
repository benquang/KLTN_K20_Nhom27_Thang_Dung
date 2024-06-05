import scrapy
import pandas as pd
import os
import pandas as pd
from crawlFootball.items import *
from crawlFootball.spiders.functions import *
class CrawlplayersSpider(scrapy.Spider):
    name = "crawlPlayersDemo"
    allowed_domains = ["sofifa.com"]
    
    custom_settings = {
        'FEEDS':{
            'player_attr_demo.csv':{'format':'csv','overwrite':True}
            },
        'ITEM_PIPELINES':{
            "crawlFootball.pipelines.GoogleCloudStoragePipeline": 300,
        },
        'LOG_STDOUT' : {True},
        "LOG_FILE" :'./logs/crawlPlayers_log.txt',
        'DOWNLOAD_DELAY' : 0.5,
        'CONCURRENT_REQUESTS' : 1,
    }
    start_urls = ["https://sofifa.com"]
    start_url = "https://sofifa.com"
    leauges = ['13'
               ] 
    numOfVersions = 1
    
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
        versions = response.xpath('//select[@name="version"]/option/@value').extract()
        # Remove the first element because it is FC 24, which is already done
        versions = versions[1:self.numOfVersions]
        for version in versions:
            current_url = self.start_url+version
            yield response.follow(current_url,callback = self.parse_on_updates,
                                meta = {'current_url':current_url}
                                )
    
    def parse_on_updates(self,response):
        function = Functions()
        update_urls = response.xpath('//select[@name="roster"]/option/@value').extract()
        update_dates = response.xpath('//select[@name="roster"]/option/text()').extract()
        update = pd.DataFrame({'url':update_urls,'date':update_dates})
        update = function.GetFirstDaysOfEachMonth(update)
        next_urls = update['url'].tolist()

        for next_url in next_urls:
            yield response.follow(self.start_url+next_url,callback = self.parse_on_pages,
                                    meta = {'current_url':self.start_url+next_url}
                                    )


    def parse_on_pages(self,response):
        players = response.xpath('//tr/td/a[@data-tippy-top]/@href').extract()
        for player in players:
            yield response.follow(self.start_url+player,callback = self.parse_on_players,
                                  meta = {'current_url':self.start_url+player}
                                  )
        # next_page_url = response.xpath('//div[@class="pagination"]/a[contains(text(), "Next")]/@href').get()
        next_page_url = None
        if (next_page_url is not None):
            yield response.follow(self.start_url+next_page_url,callback = self.parse_on_pages,
                                    meta = {'current_url':next_page_url}
                                    )
    
    def parse_on_players(self, response):
        functions = Functions()
        player = Player()
        
        player['update_date'] = response.xpath('//select[@name="roster"]/option[@selected]/text()').get()
        all_positions = response.xpath('//p[./a[@rel="nofollow"]]/span/text()').extract()
        player['all_positions'] =''
        for i,position in enumerate(all_positions):
            player['all_positions'] += position
            if i!=len(all_positions)-1:
                player['all_positions'] += ' '
        
        player['player_full_name'] = response.xpath("(//h1)[2]/text()").get()
        player['player_name'] = response.xpath("(//h1)[1]/text()").get()
        player['nationality'] = response.xpath('//p/a[@rel="nofollow"]/@title').get()
        infos = response.xpath('(//p[./a[@rel="nofollow"]]/text())[last()]').get()
        infos = functions.ExtractInfosString(infos)
        player['age'] = infos[0]
        player['birthday'] = infos[1]
        player['height'] = infos[2]
        player['weight'] = infos[3]
        player['overall_rating'] = response.xpath('//div[@class="grid"]/div[./div/text()="Overall rating"]/em/text()').get()
        player['potential'] = response.xpath('//div[@class="grid"]/div[./div/text()="Potential"]/em/text()').get()
        player['value'] = response.xpath('//div[@class="grid"]/div[./div/text()="Value"]/em/text()').get()
        player['wage'] = response.xpath('//div[@class="grid"]/div[./div/text()="Wage"]/em/text()').get()

        #Profile
        player['preferred_foot'] = response.xpath('//p[./label[text()="Preferred foot"]]/text()').get()[1:] #Remove reduntdant space by remove first space
        player['skill_moves'] = response.xpath('//p[./label[text()="Skill moves"]]/text()').get()[0] # Remove reduntdant space by only get first character
        player['weak_foot'] = response.xpath('//p[./label[text()="Weak foot"]]/text()').get()[0]
        player['reputation'] = response.xpath('//p[./label[text()="International reputation"]]/text()').get()[0]
        
        workRates = response.xpath('//p[./label[text()="Work rate"]]/text()').get()
        workRates = functions.ExtractWorkRates(workRates)
        player['attacking_work_rate'] = workRates[0]
        player['defensive_work_rate'] = workRates[1]
        player['body_type'] = response.xpath('//p[./label[text()="Body type"]]/text()').get()
        player['real_face'] = response.xpath('//p[./label[text()="Real face"]]/text()').get()[1:]
        player['sofifa_id'] = response.xpath('//p[./label[text()="ID"]]/text()').get()[1:]

        #Specialities //div[@class = "card" and ./h5/text()="Player specialities"]/ul/li/a/text()
        specialities = response.xpath('//div[@class="col" and ./h5/text() = "Player specialities"]//a/text()').extract()
        player['specialities'] = ''
        for speciality in specialities:
            player['specialities']+=speciality
        #Teams
        player['club'] = response.xpath('(//div[./h5/text()="Club"]//a)[1]/text()').get()
        if player['club'] is not None:
            player['club'] = player['club'][1:]
        player['club_league'] = response.xpath('(//div[./h5/text()="Club"]//a)[2]/text()').get()
        if player['club_league'] is not None:
            player['club_league'] = player['club_league'][1:]
        player['club_rating'] = response.xpath('(//div[./h5/text()="Club"]/p)[3]/text()').get()[:-1]
        if player['club_rating'] is not None:
            player['club_rating'] = player['club_rating'][:-1]
        player['club_position'] = response.xpath('(//div[./h5/text()="Club"])//p[./label/text()="Position"]/span/text()').get()
        player['club_kitnum']=response.xpath('(//div[./h5/text()="Club"])//p[./label/text()="Kit number"]/text()').get()
        if player['club_kitnum'] is not None:
            player['club_kitnum'] = player['club_kitnum'][1:]
        player['club_loaned_from']=response.xpath('(//div[./h5/text()="Club"])//p[./label/text()="Loaned from"]/a/text()').get()
        player['club_joined'] = response.xpath('(//div[./h5/text()="Club"])//p[./label/text()="Joined"]/text()').get()
        if player['club_joined'] is not None:
            player['club_joined'] = player['club_joined'][1:]
        player['club_contract'] = response.xpath('(//div[./h5/text()="Club"])//p[./label/text()="Contract valid until"]/text()').get()
        if player['club_contract'] is not None:
            player['club_contract'] = player['club_contract'][1:]
        
        player['national_team'] = response.xpath('(//div[./h5/text()="National team"]//a)[1]/text()').get()
        if player['national_team'] is not None:
            player['national_team'] = player['national_team'][1:]
        player['national_team_rating'] = response.xpath('(//div[./h5/text()="National team"]/p)[3]/text()').get()
        if player['national_team_rating'] is not None:
            player['national_team_rating'] = player['national_team_rating'][:-1]
        player['national_team_position'] = response.xpath('(//div[./h5/text()="National team"])//p[./label/text()="Position"]/span/text()').get()
        player['national_team_kitnum']=response.xpath('(//div[./h5/text()="National team"])//p[./label/text()="Kit number"]/text()').get()
        if player['national_team_kitnum'] is not None:
            player['national_team_kitnum'] = player['national_team_kitnum'][1:]
        
        # updateDate = response.css('span[class="bp3-button-text"]::text').extract()[1]
        # updateDate = functions.ConvertUpdateDate(updateDate)
        # player['update_date'] = updateDate
        #Attacking
        player['crossing'] = response.xpath('//p[./span/text()="Crossing"]/em/text()').get()
        player['finishing'] = response.xpath('//p[./span/text()="Finishing"]/em/text()').get()
        player['heading_accuracy'] = response.xpath('//p[./span/text()="Heading accuracy"]/em/text()').get()
        player['short_passing'] = response.xpath('//p[./span/text()="Short passing"]/em/text()').get()
        player['volleys'] = response.xpath('//p[./span/text()="Volleys"]/em/text()').get()
        #Skill
        player['dribbling'] = response.xpath('//p[./span/text()="Dribbling"]/em/text()').get()
        player['curve'] = response.xpath('//p[./span/text()="Curve"]/em/text()').get()
        player['fk_accuracy'] =  response.xpath('//p[./span/text()="FK Accuracy"]/em/text()').get()
        player['long_passing'] = response.xpath('//p[./span/text()="Long passing"]/em/text()').get()
        player['ball_control'] = response.xpath('//p[./span/text()="Ball control"]/em/text()').get()
        #Movement
        player['acceleration'] = response.xpath('//p[./span/text()="Acceleration"]/em/text()').get()
        player['sprint_speed'] = response.xpath('//p[./span/text()="Sprint speed"]/em/text()').get()
        player['agility'] = response.xpath('//p[./span/text()="Agility"]/em/text()').get()
        player['reactions'] = response.xpath('//p[./span/text()="Reactions"]/em/text()').get()
        player['balance'] = response.xpath('//p[./span/text()="Balance"]/em/text()').get()
        #Power
        player['shot_power'] = response.xpath('//p[./span/text()="Shot power"]/em/text()').get()
        player['jumping'] = response.xpath('//p[./span/text()="Jumping"]/em/text()').get()
        player['stamina'] = response.xpath('//p[./span/text()="Stamina"]/em/text()').get()
        player['strength'] = response.xpath('//p[./span/text()="Strength"]/em/text()').get()
        player['long_shots'] = response.xpath('//p[./span/text()="Long shots"]/em/text()').get()
        #Mentality
        player['aggression'] = response.xpath('//p[./span/text()="Aggression"]/em/text()').get()
        player['interceptions'] = response.xpath('//p[./span/text()="Interceptions"]/em/text()').get()
        player['positioning'] = response.xpath('//p[./span/text()="Att. Position"]/em/text()').get()
        player['vision'] = response.xpath('//p[./span/text()="Vision"]/em/text()').get()
        player['penalties'] = response.xpath('//p[./span/text()="Penalties"]/em/text()').get()
        player['composure'] = response.xpath('//p[./span/text()="Composure"]/em/text()').get()
        #DEFENDING
        player['marking'] = response.xpath('//p[./span/text()="Marking"]/em/text()').get()
        player['defensive_awareness'] = response.xpath('//p[./span/text()="Defensive Awareness"]/em/text()').get()
        player['standing_tackle'] = response.xpath('//p[./span/text()="Standing tackle"]/em/text()').get()
        player['sliding_tackle'] = response.xpath('//p[./span/text()="Sliding tackle"]/em/text()').get()
        #GOALKEEPING
        player['gk_diving'] = response.xpath('//p[./span/text()="GK Diving"]/em/text()').get()
        player['gk_handling'] = response.xpath('//p[./span/text()="GK Handling"]/em/text()').get()
        player['gk_kicking'] = response.xpath('//p[./span/text()="GK Kicking"]/em/text()').get()
        player['gk_positioning'] = response.xpath('//p[./span/text()="GK Positioning"]/em/text()').get()
        player['gk_reflexes'] = response.xpath('//p[./span/text()="GK Reflexes"]/em/text()').get()

        play_styles = response.xpath('//div[./h5/text()="PlayStyles"]//span/text()').extract()
        player['play_styles'] = ''
        for play_style in play_styles:
            player['play_styles']+='#'
            player['play_styles']+=play_style
        yield player


