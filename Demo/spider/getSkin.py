# 发送请求的模块 pip install requests
import requests
# 解析html代码的工具 lxml    pip install lxml
from lxml import etree
import os
from time import sleep

# 伪装自己
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'}

# 获取英雄列表的URL
hero_list_url = 'https://pvp.qq.com/web201605/js/herolist.json'
# 发送HTTP请求获取英雄列表数据
hero_list_resp = requests.get(hero_list_url, headers=headers)

# 遍历英雄列表数据
for h in hero_list_resp.json():
    # 获取英雄的ID和中文名
    ename = h.get('ename')
    cname = h.get('cname')
    # 如果英雄目录不存在，则创建
    if not os.path.exists(cname):
        os.makedirs(cname)

    # 访问英雄主页
    hero_info_url = f'https://pvp.qq.com/web201605/herodetail/{ename}.shtml'
    hero_info_resp = requests.get(hero_info_url, headers=headers)
    hero_info_resp.encoding = 'gbk'
    e = etree.HTML(hero_info_resp.text)

    # 提取皮肤名称
    names = e.xpath('//ul[@class="pic-pf-list pic-pf-list3"]/@data-imgname')[0]
    names = [name[0:name.index('&')] for name in names.split('|')]

    # 遍历每个皮肤名称
    for i, n in enumerate(names):
        # 构建皮肤图片的URL
        resp = requests.get(
            f'http://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/{ename}/{ename}-bigskin-{i + 1}.jpg',
            headers=headers)

        # 保存皮肤图片
        with open(f'{cname}/{n}.jpg', 'wb') as f:
            f.write(resp.content)

        # 打印已下载的皮肤信息
        print(f'已下载:{n} 的皮肤')

        # 等待1秒，避免请求频率过快
        sleep(1)

