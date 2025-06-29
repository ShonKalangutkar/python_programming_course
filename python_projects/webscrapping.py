'''
https://www.scrapethissite.com/pages/

libs used:
requests 
beautifulsoup
html5lib
'''
import requests
import bs4


url = "https://www.scrapethissite.com/pages/"
response = requests.get(url)

soup = bs4.BeautifulSoup(response.content, 'html5lib')
# print(soup.prettify())

page_title_h3 = soup.find_all("h3", attrs={"class":"page-title"})
description_p = soup.find_all("p", attrs={"class":"session-desc"})
index = 1
for i in range(len(page_title_h3)):
    print(index, page_title_h3[i].a.text)
    print(description_p[i].text.strip())
    print()
    index += 1
    
    