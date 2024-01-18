import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import math

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

url = 'https://www.statmuse.com/nba'

driver.get(url)


print('\n')
name = input('What Player: ')
print('\n\n')

driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[3]/div/astro-island/form/div[2]/div[1]/textarea').send_keys(name + " home stats regular season") 
driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[3]/div/astro-island/form/div[2]/div[1]/input').click()
time.sleep(3)
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
stats = soup.find_all(attrs={"class": "grid grid-cols-[1fr_min(1250px,_100%)_1fr] w-full px-3 md:px-[75px] [&>*]:col-span-1 [&>*]:col-start-2"})


for stat in stats:
    row_content = stat.find_all("td")
    hPPG = float(row_content[4].text.strip())
    hReb = float(row_content[5].text.strip())
    hAst = float(row_content[6].text.strip())
    hStl = float(row_content[7].text.strip())
    hBlk = float(row_content[8].text.strip())
    hTOV = float(row_content[9].text.strip())
    hFG = float(row_content[12].text.strip())
    break


driver.find_element(By.XPATH,'/html/body/div[1]/div[1]/a').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[3]/div/astro-island/form/div[2]/div[1]/textarea').send_keys(name + " away stats regular season") 
driver.find_element(By.XPATH,'//*[@id="home"]/div[3]/div[3]/div/astro-island/form/div[2]/div[1]/input').click()
time.sleep(3)
page = driver.page_source
soup = BeautifulSoup(page, 'html.parser')
stats = soup.find_all(attrs={"class": "grid grid-cols-[1fr_min(1250px,_100%)_1fr] w-full px-3 md:px-[75px] [&>*]:col-span-1 [&>*]:col-start-2"})



for stat in stats:
    row_content = stat.find_all("td")
    aPPG = float(row_content[4].text.strip())
    aReb = float(row_content[5].text.strip())
    aAst = float(row_content[6].text.strip())
    aStl = float(row_content[7].text.strip())
    aBlk = float(row_content[8].text.strip())
    aTOV = float(row_content[9].text.strip())
    aFG = float(row_content[12].text.strip())
    break

print('Home Statistics:',hPPG,' PPG ', hReb,' RPG ', hAst,' APG ', hStl,' SPG ', hBlk,' BPG ', hTOV,' TPG ', hFG,' FG% ')
print('Away Statistics:',aPPG,' PPG ', aReb,' RPG ', aAst,' APG ', aStl,' SPG ', aBlk,' BPG ', aTOV,' TPG ', aFG,' FG% ')

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

print(name,'averaged a\n',PPG,'percent change in PPG\n',REB,'percent change in Rebounds\n',AST,'percent change in Assits\n',STL,'percent change in Steals\n',BLK,'percent change in Blocks\n',TOV,'percent change in Turn Overs\n',FG,'percent change in Field Goal Percentage\n')

print('\n\n\n')
