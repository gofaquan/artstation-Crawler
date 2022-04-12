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

tag_component1 = "https://www.artstation.com/projects/"
tag_component2 = ".json"

# tag 所在
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


class img:
    def __init__(self, JSON):
        self.hash_id = JSON['hash_id']
        self.url = JSON['url']
        self.hide_as_adult = JSON['hide_as_adult']
        self.smaller_square_cover_url = JSON['smaller_square_cover_url']
        self.title = JSON['title']

    def toDict(self):
        return {
            'hash_id': self.hash_id,
            'url': self.url,
            'hide_as_adult': self.hide_as_adult,
            'smaller_square_cover_url': self.smaller_square_cover_url,
            'title': self.title,
        }


class user:
    def __init__(self, JSON):
        self.username = JSON['username']
        self.medium_avatar_url = JSON['medium_avatar_url']
        self.is_staff = JSON['is_staff']
        self.pro_member = JSON['pro_member']
        self.is_plus_member = JSON['is_plus_member']
        self.is_studio_account = JSON['is_studio_account']
        self.is_school_account = JSON['is_school_account']
        self.full_name = JSON['full_name']

    def toDict(self):
        return {
            'username': self.username,
            'medium_avatar_url': self.medium_avatar_url,
            'is_staff': self.is_staff,
            'pro_member': self.pro_member,
            'is_plus_member': self.is_plus_member,
            'is_studio_account': self.is_studio_account,
            'is_school_account': self.is_school_account,
            'full_name': self.full_name,
        }


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
    imgSlice = []
    userSlice = []
    for i in range(0, 10):
        print(i)
        imgSlice.append(img(data[i]).toDict())
        userSlice.append(user(userSlice[i]['user']).toDict())

    # print(imgSlice)


    # 插入多个
    img_collection.insert_many(imgSlice)
    user_collection.insert_many(userSlice)
    # user_collection.insert_one(user_data)

    # 导入 tag

    url_page += 1
