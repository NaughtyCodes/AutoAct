from selenium import webdriver  
from selenium.common.exceptions import NoSuchElementException  
from selenium.webdriver.common.keys import Keys  
from bs4 import BeautifulSoup

eqList = []
eqList.append('20MICRONS')
eqList.append('3IINFOTECH')
eqList.append('3MINDIA')

browser = webdriver.Chrome()
for eq in eqList:
    browser.get('https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?symbol='+eq+'&illiquid=0&smeFlag=0&itpFlag=0')  
    html_source = browser.page_source
    htmlText = BeautifulSoup(html_source,'html.parser')
    companyName = htmlText.find('span', attrs={'id':'companyName'})
    companyName = companyName.text
    print companyName

browser.quit()

#comments = soup.findAll('div',{'class':'postText'})  
#print comments
