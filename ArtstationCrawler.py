# 引入网络请求库
import requests
from pymongo import MongoClient

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


# 伪装成浏览器访问
headers = {"Connection": "keep-alive",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "Upgrade-Insecure-Requests": "1",
           "DNT": "1",
           "Accept-Language": "zh-CN,zh;q=0.8",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"}

client = MongoClient('mongodb://root:123456@localhost:27017/')
# print(client.list_database_names())
db = client['test']
img_collection = db['image']
user_collection = db['user']

while url_page <= 1:
    url = url_component1 + str(url_page) + url_component2
    # url = "https://www.baidu.com"
    print(url)

    # 发起网络请求，获取到返回的html
    resp = requests.get(url, headers=headers, timeout=10, proxies={"https": "http://172.22.224.1:7890", })

    # 网页返回的数据
    raw_json = resp.json()
    data = raw_json['data']
    # print(len(data))

    # 原来可以 直接 insert_many 识别格式，多写了
    # for i in range(1, 100):
        ## 图像数据
        # img_data = {'id': data[i]['id'],
        #             'hash_id': data[i]['hash_id'],
        #             'url': data[i]['url'],
        #             "smaller_square_cover_url": data[i]['smaller_square_cover_url'],
        #             "title": data[i]['title'],
        #             "hide_as_adult": data[i]['hide_as_adult'],
        #             }

    # 插入多个
    img_collection.insert_many(data)

        # # user 数据
        # user_data = {
        #     "id": data[i]['user']['id'],
        #     "username": data[i]['user']['username'],
        #     "medium_avatar_url": data[i]['user']['medium_avatar_url'],
        #     "is_staff": data[i]['user']['is_staff'],
        #     "pro_member": data[i]['user']['pro_member'],
        #     "is_plus_member": data[i]['user']['is_plus_member'],
        #     "is_studio_account": data[i]['user']['is_studio_account'],
        #     "is_school_account": data[i]['user']['is_school_account'],
        #     "full_name": data[i]['user']['full_name'],
        # }
        # user_collection.insert_one(user_data)



    url_page += 1
