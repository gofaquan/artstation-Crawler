import json
# 引入网络请求库
from urllib import request

# 首页地址
url = "https://www.artstation.com/projects.json?page=1&sorting=trending"

# 添加UA标识讲这个爬虫程序伪装成浏览器访问
user_agent = "User-Agent"
user_agent_value = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"

# 发起网络请求，获取到返回的html
resp = request.Request(url)
# 模拟浏览器
resp.add_header(user_agent, user_agent_value)
resp = request.urlopen(resp)
# 网页返回的数据
raw_json = resp.read().decode("utf-8")

content = json.loads(raw_json)
print(content['data'][0])
