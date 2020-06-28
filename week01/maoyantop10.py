import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'Cookie': 'uuid_n_v=v1; uuid=551E9B80B85D11EAB4E28FB161D5B82B20B7B3F6B30D4415BD87C8FC120EA552; _csrf=b2fac22b64d62204dae47f958d75d3f3aa76ff800b3dab6cbd64d50d5ac9c13e; _lxsdk_cuid=172f53aa891c8-0dc14be1817201-31607402-13c680-172f53aa891c8; _lxsdk=551E9B80B85D11EAB4E28FB161D5B82B20B7B3F6B30D4415BD87C8FC120EA552; mojo-uuid=e6244ceab3bb39859e17a77dce2a70e6; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593252162,1593252182; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593275271; __mta=221493543.1593252162022.1593275252543.1593275271827.19; _lxsdk_s=172f69a3bc3-933-662-261%7C%7C11',
    'Connection': 'keep-alive',
    }
url = "https://maoyan.com/films?showType=3&sortId=1"

response = requests.get(url, headers=headers)
# print(f'返回码是：{response.status_code}')


bs_info = bs(response.text, "html.parser")
# print(bs_info.prettify())

tags = bs_info.find_all('div', attrs={'class': 'movie-hover-info'}, limit=10)
# print(tags)

# MaoyanMovieTop10 = pd.DataFrame(columns=('电影名称', '电影类型', '上映时间'))
Maoyan_Movie_Top_10 = pd.DataFrame()

for tag in tags:
    # 获取电影名称film_name
    film_name = tag.find('span').text
    # print(f'电影名称：{film_name}')
    # 获取电影类型film_type
    film_type = tag.find_all('span')[2].next_sibling.strip()
    # print(f'电影类型：{film_type}')
    # 获取上映时间film_date
    film_date = tag.find_all('span')[-1].next_sibling.strip()
    # print(f'上映时间：{film_date}')
    # print('\n')
    movie_info = [film_name, film_type, film_date]
    Maoyan_Movie_Top_10 = Maoyan_Movie_Top_10.append(pd.DataFrame([movie_info]))
    # print(movie_info)

print(Maoyan_Movie_Top_10)
Maoyan_Movie_Top_10.to_csv('/Users/zzz/Python001-class01/week01/Maoyan_Movie_Top_10_bs4.csv', encoding='utf8', index=False, header=False)