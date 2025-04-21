import requests
import pandas as pd
import re
from tqdm import tqdm
from bs4 import BeautifulSoup

tags = []
space_names = []
model_cards = []
urls = pd.read_csv('data/urls_3000_common_250201.csv')
base_url = 'https://huggingface.co'


for i in tqdm(range(urls.shape[0])):
    # url 접속
    response = requests.get(base_url + urls['url'][i])
    
    # content 수집
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')


    #model card
    card_div = soup.find('div', {'class': re.compile(r"^model-card-content prose")})
    
    if card_div:
        model_card = card_div.text.strip()
    else:
        model_card = ['no model card']

    model_cards.append(model_card)
    
    # tag가 없는 모델 처리
    # try:
    divs = soup.find_all('div', {'class': 'tag tag-white'})
    tag = [div.find('span').text for div in divs]
    tags.append(tag)
        
    # space가 없는 모델 처리
    try:
        navs = soup.find_all('nav', {'class': 'flex max-w-full flex-wrap gap-x-2.5 gap-y-2'})
        spaces = [nav.find_all('div', {'class': 'truncate group-hover:underline'}) for nav in navs][0]
        spaces = [space.text for space in spaces]
        space_names.append(spaces)

    except IndexError:
        spaces = ['no space']
        space_names.append(spaces)
        continue



print(len(tags))
print(len(urls['url']))
print(len(space_names))
print(len(model_cards))

# pd.Series(space_names).to_csv('space_names.csv', index=False)

# 결과 저장
pd.DataFrame(data={
    'model': urls['url'], 
    'tag': tags,
    'space': space_names,
    'modelcard': model_cards
     }).to_csv('data/huggingface_250201_bs4.csv', index=False)  
