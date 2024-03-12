import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import time
from functions import *
import pandas as pd
from kafka import KafkaProducer
import json
import csv
def crawlUpComingMatch():
    data = {
        'Match_Date': [],
        'League': [],
        'Home_Team': [],
        'Away_Team': [],
        'Home_Player1': [],
        'Home_Player2': [],
        'Home_Player3': [],
        'Home_Player4': [],
        'Home_Player5': [],
        'Home_Player6': [],
        'Home_Player7': [],
        'Home_Player8': [],
        'Home_Player9': [],
        'Home_Player10': [],
        'Home_Player11': [],
        'Away_Player1': [],
        'Away_Player2': [],
        'Away_Player3': [],
        'Away_Player4': [],
        'Away_Player5': [],
        'Away_Player6': [],
        'Away_Player7': [],
        'Away_Player8': [],
        'Away_Player9': [],
        'Away_Player10': [],
        'Away_Player11': []
    }

    df = pd.DataFrame(data)
    leauge = ['Premier Leauge']

    options = ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.sportsgambler.com/lineups/football/england-premier-league/")
    print(driver.title)
    try:
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[./span[text()='Predicted Lineups']]"))
        )
        predicted_lineup_buttons = driver.find_elements(By.XPATH, "//a[./span[text()='Predicted Lineups']]")
        for predicted_lineup_button in predicted_lineup_buttons:
            driver.execute_script("arguments[0].click();", predicted_lineup_button)
        dates = driver.find_elements(By.XPATH,"//div[@class='content-block team-news-container']//h3[@class = 'date-headline']")
        dates = [CustomFuncs.UCM_convert_date(date.text) for date in dates]
        time.sleep(7)
        for index_date,date in enumerate(dates):
            number_of_match_in_dates = len(driver.find_elements(By.XPATH,"//div[@class = 'content-block team-news-container']\
                                                                         //div[@class='fxs-table table-for-lineups'][{}]\
                                                                        //div[@class='table-row-loneups' and \
                                                                        .//span[text() = 'Predicted Lineups']]".format(index_date+1)))
            if (number_of_match_in_dates == 0):
                continue
            
            for index_match in range(number_of_match_in_dates):
                xpath_infor_row = "//div[@class = 'content-block team-news-container']//div[@class='fxs-table table-for-lineups'][{}]\
                                                                                        //div[@class='table-row-loneups' and .\
                                                                                        //span[text() = 'Predicted Lineups']][{}]"\
                                                                                        .format(index_date+1,index_match+1)
                home_team = driver.find_element(By.XPATH,xpath_infor_row+"//span[@class='fxs-team home']").text
                away_team = driver.find_element(By.XPATH,xpath_infor_row+"//span[@class='fxs-team']").text
                xpath_home_lineup = "(//div[@class = 'content-block team-news-container']//div[@class='fxs-table table-for-lineups'][{}]\
                                                                                        //div[@class='table-row-loneups' and \
                                                                                        .//span[text() = 'Predicted Lineups']]\
                                                                                        //div[@class='lineups-home reverse'])[{}]"\
                                                                                        .format(index_date+1,index_match+1)
                xpath_away_lineup = "(//div[@class = 'content-block team-news-container']//div[@class='fxs-table table-for-lineups'][{}]//div[@class='table-row-loneups' and .//span[text() = 'Predicted Lineups']]//div[@class='lineups-away'])[{}]".format(index_date+1,index_match+1)
                home_kits = driver.find_elements(By.XPATH,xpath_home_lineup+"//span[@class = 'player-profile']")
                home_kits = [kit.text for kit in home_kits]
                away_kits = driver.find_elements(By.XPATH,xpath_away_lineup+"//span[@class = 'player-profile']")
                away_kits = [kit.text for kit in away_kits]
                home_player_names = driver.find_elements(By.XPATH,xpath_home_lineup+"//span[@class = 'player-name']")
                home_player_names = [name.text for name in home_player_names]
                away_player_names = driver.find_elements(By.XPATH,xpath_away_lineup+"//span[@class = 'player-name']")
                away_player_names = [name.text for name in away_player_names]
                print(away_player_names)
                
                row_data = data = {
                    'Match_Date': date,
                    'League': 'Premier League',
                    'Home_Team': home_team,
                    'Away_Team': away_team,
                    'Home_Player1': [home_player_names[0]],
                    'Home_Player2': [home_player_names[1]],
                    'Home_Player3': [home_player_names[2]],
                    'Home_Player4': [home_player_names[3]],
                    'Home_Player5': [home_player_names[4]],
                    'Home_Player6': [home_player_names[5]],
                    'Home_Player7': [home_player_names[6]],
                    'Home_Player8': [home_player_names[7]],
                    'Home_Player9': [home_player_names[8]],
                    'Home_Player10': [home_player_names[9]],
                    'Home_Player11': [home_player_names[10]],
                    'Away_Player1': [away_player_names[0]],
                    'Away_Player2': [away_player_names[1]],
                    'Away_Player3': [away_player_names[2]],
                    'Away_Player4': [away_player_names[3]],
                    'Away_Player5': [away_player_names[4]],
                    'Away_Player6': [away_player_names[5]],
                    'Away_Player7': [away_player_names[6]],
                    'Away_Player8': [away_player_names[7]],
                    'Away_Player9': [away_player_names[8]],
                    'Away_Player10': [away_player_names[9]],
                    'Away_Player11': [away_player_names[10]],
                    'Home_Kit1': [home_kits[0]],
                    'Home_Kit2': [home_kits[1]],
                    'Home_Kit3': [home_kits[2]],
                    'Home_Kit4': [home_kits[3]],
                    'Home_Kit5': [home_kits[4]],
                    'Home_Kit6': [home_kits[5]],
                    'Home_Kit7': [home_kits[6]],
                    'Home_Kit8': [home_kits[7]],
                    'Home_Kit9': [home_kits[8]],
                    'Home_Kit10': [home_kits[9]],
                    'Home_Kit11': [home_kits[10]],
                    'Away_Kit1': [away_kits[0]],
                    'Away_Kit2': [away_kits[1]],
                    'Away_Kit3': [away_kits[2]],
                    'Away_Kit4': [away_kits[3]],
                    'Away_Kit5': [away_kits[4]],
                    'Away_Kit6': [away_kits[5]],
                    'Away_Kit7': [away_kits[6]],
                    'Away_Kit8': [away_kits[7]],
                    'Away_Kit9': [away_kits[8]],
                    'Away_Kit10': [away_kits[9]],
                    'Away_Kit11': [away_kits[10]],
                }
                df = pd.concat([df, pd.DataFrame(row_data, index=[0])], ignore_index=True)
    finally:
        df.to_csv('data.csv', index=False, encoding='utf-8-sig',header=True)
        driver.quit()

def kafka_producer():
    producer = KafkaProducer(
            bootstrap_servers = 'localhost:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    with open('data.csv', 'r',encoding='utf-8-sig') as f:
        for row in f:
            row = row.strip()
            row=row.strip('\n')
            producer.send('UpComingMatch_Topic',row)
            producer.flush() # Đợi cho tất cả message cho queue được gửi đi
            print(row)

def main():
    crawlUpComingMatch()
    kafka_producer()

if __name__ == "__main__":
    main()

