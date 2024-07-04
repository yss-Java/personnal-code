import requests

# url='https://www.baidu.com'
# response = requests.get(url)
# print(response.text)

# url = 'http://xxxx.org/post'  # 这里使用xxxx.org来演示POST请求
# data = {'key1': 'value1', 'key2': 'value2'}
# response = requests.post(url, data=data)
# print(response.text)

# from lxml import etree
# import requests
#
# url = 'https://www.baidu.com'
# html = requests.get(url).text
# selector = etree.HTML(html)
# result = selector.xpath('//title/text()')
# print(result[0])
#


from bs4 import BeautifulSoup

html_doc = """
<html>
<head><title>这是标题</title></head>
<body>
<p class="para1">第一段落</p>
<p class="para2">第二段落</p>
</body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
p = soup.find('p', class_='para1')
p['class'] = 'new_class'
print(p)

