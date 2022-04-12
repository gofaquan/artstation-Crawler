import json
# 引入网络请求库
from urllib import request

# 地址
url_component1 = "https://www.artstation.com/api/v2/community/explore/projects/trending.json?page="
url_page = 1
url_component2 = "&dimension=all&per_page=100"
component1 = "https://www.artstation.com/projects/"
component2 = ".json"

# url = "https://www.artstation.com/projects.json?page=1&sorting=trending"
# https://www.artstation.com/api/v2/community/explore/projects/trending.json?page=1&dimension=all&per_page=10
# https://www.artstation.com/projects/DAOOxe.json
# tags 本身有 tag
# categories 里包含tag
# medium/mediums  包含 tag


# 添加UA标识讲这个爬虫程序伪装成浏览器访问
user_agent = "User-Agent"
user_agent_value = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"

while url_page <= 500:
    url = url_component1 + str(url_page) + url_component2
    print(url)
    url_page += 1
# # 发起网络请求，获取到返回的html
# resp = request.Request(url)
# # 模拟浏览器
# resp.add_header(user_agent, user_agent_value)
# resp = request.urlopen(resp)
# # 网页返回的数据
# raw_json = resp.read().decode("utf-8")
#
# content = json.loads(raw_json)
# print(content['data'][0])
