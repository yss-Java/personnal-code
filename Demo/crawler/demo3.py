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

# with open('example.html','r') as f:
#     soup = BeautifulSoup(f, 'html.parser')


# from bs4 import BeautifulSoup
# import requests
#
# url = 'https://www.baidu.com'
# html = requests.get(url)
# html.encoding='utf-8'
# html_text = html.text
# soup = BeautifulSoup(html_text, 'html.parser')
# title = soup.title.string
# print(title)

# from bs4 import BeautifulSoup
#
# html_doc = """
# <html>
# <head><title>这是标题</title></head>
# <body>
# <p class="para1">第一段落</p>
# <p class="para2">第二段落</p>
# </body>
# </html>
# """
#
# soup = BeautifulSoup(html_doc, 'html.parser')
# for p in soup.body.children:
#     if p.name == 'p':
#         print(p.string)

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
p_list = soup.select('p.para1')
for p in p_list:
    print(p.text)
