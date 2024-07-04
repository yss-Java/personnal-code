# import re
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
# pattern = re.compile('^p.*?1$')  # 匹配所有以p开头并且以1结尾的类名
# p_list = soup.find_all(class_=pattern)
# for p in p_list:
#     print(p.text)

from bs4 import BeautifulSoup

xml_doc = """
<?xml version="1.0" encoding="UTF-8"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
</data>
"""

soup = BeautifulSoup(xml_doc, 'xml')
for country in soup.find_all('country'):
    print(country['name'])
    print(country.rank.text)
    print(country.year.text)
    print(country.gdppc.text)
    for neighbor in country.find_all('neighbor'):
        print(neighbor['name'], neighbor['direction'])
