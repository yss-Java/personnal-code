# from lxml import etree
#
# xml = '''
# <bookstore>
#   <book category="cooking">
#     <title lang="en">Everyday Italian</title>
#     <author>Giammarco Tomaselli</author>
#     <year>2010</year>
#     <price>30.00</price>
#   </book>
#   <book category="children">
#     <title lang="en">Harry Potter</title>
#     <author>J.K. Rowling</author>
#     <year>2005</year>
#     <price>29.99</price>
#   </book>
# </bookstore>
# '''
#
# selector = etree.XML(xml)
# result = selector.xpath('//book[1]/title/text()')
# print(result[0])


from lxml import etree

xml = '''
<ns:bookstore xmlns:ns="http://www.example.com">
  <ns:book category="cooking">
    <ns:title lang="en">Everyday Italian</ns:title>
    <ns:author>Giammarco Tomaselli</ns:author>
    <ns:year>2010</ns:year>
    <ns:price>30.00</ns:price>
  </ns:book>
  <ns:book category="children">
    <ns:title lang="en">Harry Potter</ns:title>
    <ns:author>J.K. Rowling</ns:author>
    <ns:year>2005</ns:year>
    <ns:price>29.99</ns:price>
  </ns:book>
</ns:bookstore>
'''

selector = etree.XML(xml)
ns = {'ns': 'http://www.example.com'}
result = selector.xpath('//ns:book[1]/ns:title/text()', namespaces=ns)
print(result[0])
