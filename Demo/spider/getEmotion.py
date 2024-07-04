# 地址
url = 'http://www.netbian.com/mei/'

import requests
from lxml import etree

# 发送请求获取网页内容
resp = requests.get(url, headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'})
resp.encoding = 'gbk'  # 告诉软件，要用中文给我显示
print(resp.text)  # 打印文本结果

# 使用lxml解析HTML内容
xp = etree.HTML(resp.text)

# 提取图片URL和名称
img_urls = xp.xpath('//ul/li/a/img/@src')
img_names = xp.xpath('//ul/li/a/img/@alt')

# 遍历图片URL和名称，并下载保存到本地
for u, n in zip(img_urls, img_names):
    print(f'正在下载：图片名：{n}')
    img_resp = requests.get(u, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'})
    with open(f'D:/美女图片/img_f/{n}.jpg', 'wb') as f:
        f.write(img_resp.content)
