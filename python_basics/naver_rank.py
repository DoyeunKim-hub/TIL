import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.naver.com').text
soup = BeautifulSoup(response, 'html.parser')

#a = soup.select_one("#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(1) > a > span.ah_k").text
#print(a)
#soup.select
#for i in range(10):
 #   a= soup.select(f'div > ul > li:nth-child({i}) > a > span.ah_k').text
  #  print(a)

tags = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul .ah_k')
with open('naver.txt', 'w', encoding='utf-8') as f:
    f.write('네이버 검색어 순위 \n')
    for i, tag in enumerate(tags):
        f.write(f'{i+1}.{tag.text} \n')
    
