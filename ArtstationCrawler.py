import json
# 引入网络请求库
# from urllib import request
import requests

# 地址
url_component1 = "https://www.artstation.com/api/v2/community/explore/projects/trending.json?page="
url_page = 1
url_component2 = "&dimension=all&per_page=10"
component1 = "https://www.artstation.com/projects/"
component2 = ".json"

# url = "https://www.artstation.com/projects.json?page=1&sorting=trending"
# https://www.artstation.com/api/v2/community/explore/projects/trending.json?page=1&dimension=all&per_page=10
# https://www.artstation.com/projects/DAOOxe.json
# tags 本身有 tag
# categories 里包含tag
# medium/mediums  包含 tag


# 添加UA标识讲这个爬虫程序伪装成浏览器访问
headers = {"Connection": "keep-alive",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "Upgrade-Insecure-Requests": "1",
           "DNT": "1",
           "Accept-Language": "zh-CN,zh;q=0.8",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}


while url_page <= 1:
    url = url_component1 + str(url_page) + url_component2
    # url = "https://www.baidu.com"
    print(url)

    # 发起网络请求，获取到返回的html
    resp = requests.get(url,headers=headers,timeout=1)
    print(resp)



    # 网页返回的数据
    # raw_json = resp.json()
    #
    # content = json.loads(raw_json)
    # print(content)

    url_page += 1
