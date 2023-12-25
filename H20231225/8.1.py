# 1.	爬取“站长之家”的中文网站排行榜，并将其中的排名、网站、网站得分存入XLSX文件。
# 提示：https://top.chinaz.com/alltop/index.html

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# 发送请求获取网页内容
url = 'https://top.chinaz.com/alltop/index.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# 创建一个Excel工作簿
wb = Workbook()
ws = wb.active
ws.append(['排名', '网站', 'Alexa排名', '得分'])

# 定位网站排行榜内容所在的标签
site_list = soup.find_all('div', class_='ContTit ulli clearfix')
for site in site_list:
    rank = site.find('div', class_='w90 col-red03 fz16').text.strip()
    name = site.find('div', class_='w320 PCop').text.strip()

    # 分别找到Alexa排名和得分
    alexas_rank = site.find_all('div', class_='w120')[0].text.strip()  # 第一个w120元素为Alexa排名
    score = site.find_all('div', class_='w120')[1].text.strip()  # 第二个w120元素为得分

    # 将数据写入Excel文件
    ws.append([rank, name, alexas_rank, score])

# 保存Excel文件
wb.save('站长之家排行榜.xlsx')

