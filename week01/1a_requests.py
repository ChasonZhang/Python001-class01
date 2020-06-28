import requests

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

# 模拟浏览器的头部
# 写法1
header = {'user-agent':user_agent}

# 写法2
# header = {}
# header['user-agent'] = user_agent


# url = "https://movie.douban.com/top250?start=0"
url = "https://movie.douban.com/top250?"

response = requests.get(url, headers=header)

print(response.text)
print(f'返回码是：{response.status_code}')