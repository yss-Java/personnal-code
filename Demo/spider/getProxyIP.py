import requests
from lxml import etree

# 定义保存结果的文件
with open('IP代理.txt', 'w', encoding='utf-8') as f:
    # 循环爬取多个页面
    for i in range(1, 10):
        # 构造完整的URL
        url = f'http://www.66ip.cn/{i}.html'
        print(f'正在获取{url}')

        # 伪装浏览器请求头
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        }

        # 发送GET请求
        resp = requests.get(url, headers=headers)

        # 设置响应的编码为GBK
        resp.encoding = 'utf-8'
        # print(resp.text)
        # 解析HTML
        e = etree.HTML(resp.text)

        # 提取IP、Port和地址信息
        ips = e.xpath('//div[1]/table//tr/td[1]/text()')
        ports = e.xpath('//div[1]/table//tr/td[2]/text()')
        addrs = e.xpath('//div[1]/table//tr/td[3]/text()')

        # 将提取的代理信息写入文件
        for ip, port, addr in zip(ips, ports, addrs):
            f.write(f'IP地址：{ip}----port端口号：{port}-----地址：{addr}\n')
