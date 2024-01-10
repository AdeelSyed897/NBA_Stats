import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import math

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")


driver = webdriver.Chrome(options=options)

url = 'https://www.statmuse.com/nba'

driver.get(url)


print('\n')
name = input('What Player: ')
print('\n\n')

driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[2]/div/ask-bar/form/div/div[1]/textarea').send_keys(name + " 2022-2023 regular season home stats") #can be home/away to compare those stats
driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[2]/div/ask-bar/form/div/div[1]/input').click()
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')


stats = soup.find_all(attrs={"class": "text-sm font-semibold"})


for stat in stats:
    row_content = stat.find_all("td")
    hPPG = float(row_content[8].text.strip())
    hReb = float(row_content[9].text.strip())
    hAst = float(row_content[10].text.strip())
    hStl = float(row_content[11].text.strip())
    hBlk = float(row_content[12].text.strip())
    hTOV = float(row_content[13].text.strip())
    hFG = float(row_content[16].text.strip())
    break


driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/a').click()

driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[2]/div/ask-bar/form/div/div[1]/textarea').send_keys(name + " 2022-2023 regular season away stats") #can be home/away to compare those stats
driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[2]/div/ask-bar/form/div/div[1]/input').click()
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')


stats = soup.find_all(attrs={"class": "text-sm font-semibold"})


for stat in stats:
    row_content = stat.find_all("td")
    aPPG = float(row_content[8].text.strip())
    aReb = float(row_content[9].text.strip())
    aAst = float(row_content[10].text.strip())
    aStl = float(row_content[11].text.strip())
    aBlk = float(row_content[12].text.strip())
    aTOV = float(row_content[13].text.strip())
    aFG = float(row_content[16].text.strip())
    break

PPG = ((aPPG-hPPG)/hPPG)*100
PPG = math.ceil(PPG*100)/100

REB = ((aReb-hReb)/hReb)*100
REB = math.ceil(REB*100)/100

AST = ((aAst-hAst)/hAst)*100
AST = math.ceil(AST*100)/100

STL = ((aStl-hStl)/hStl)*100
STL = math.ceil(STL*100)/100

BLK = ((aBlk-hBlk)/hBlk)*100
BLK = math.ceil(BLK*100)/100

TOV = ((aTOV-hTOV)/hTOV)*100
TOV = math.ceil(TOV*100)/100

FG = ((aFG-hFG)/hFG)*100
FG = math.ceil(FG*100)/100

print(name,'had a\n',PPG,'percent change in PPG\n',REB,'percent change in Rebounds\n',AST,'percent change in Assits\n',STL,'percent change in Steals\n',BLK,'percent change in Blocks\n',TOV,'percent change in Turn Overs\n',FG,'percent change in Field Goal Percentage\n')

print('\n\n\n')

