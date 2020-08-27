import requests
import json
import pandas as pd

print("""
    1-纪录片；2-传记；3-犯罪；4-历史；5-动作；
    6-情色；7-歌舞；8-儿童；10-悬疑；11-剧情；
    12-灾难；13-爱情；14-音乐；15-冒险；16-奇幻；
    17-科幻；18-运动；19-惊悚；20-恐怖；22-战争；
    23-短篇；24-喜剧；25-动画；26-同性；27-西部；
    28-家庭；29-武侠；30-古装；31-黑色电影
""")
type_name = input('请输入电影类型序号：')
numbers = input('您想查看排名前多少位的电影：')
agent = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'
}
url = 'https://movie.douban.com/j/chart/top_list'
data = {
    'type': type_name,
    'interval_id': '100:90',
    'action':'',
    'start': '0',
    'limit': numbers
}
response = requests.get(url=url, headers=agent,params=data).text
dict_list = json.loads(response)
dict_name =[i["title"]for i in dict_list]
pingfen =[i["score"]for i in dict_list]
leixing =[i["types"]for i in dict_list]
guojia =[i["regions"]for i in dict_list]
shangying=[i["release_date"]for i in dict_list]
zhuyan =[i["actors"]for i in dict_list]
wangzhi =[i["url"]for i in dict_list]

data_list = pd.DataFrame({'name':dict_name,'pingfen':pingfen,'leixing':leixing,'guojia':guojia,'shangying':shangying,'zhuyan':zhuyan,'wangzhi':wangzhi})
data_list.index = data_list.index + 1
data_list.to_excel('/Users/jin/Documents/pythonProject/dingying.xlsx')

