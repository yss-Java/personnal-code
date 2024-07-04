# 使用 for 遍历打印列表信息
list = [
    {
        "id": 966024429,
        "number": 2341,
        "title": "Question about license.",
        "body": "I would like to create a [winget](https://github.com/microsoft/winget-cli) package for jq. 🙏🏻"
    },
    {

        "id": 962477084,
        "number": 2340,
        "title": "visibility of wiki pages",
        "body": "The visibility of wiki pages to search engines is generally limited; for example, the search result for \"jq Cookbook\" looks like this:"
    }
]
# 循环方式1
i = 0
for item in list:
    print('')
    print("## 第{}条信息".format(i))
    print("* id: {}".format(item['id']))
    print("* number: {}".format(item['number']))
    print("* title: {}".format(item['title']))
    print("* body: {}".format(item['body']))
    i += 1
# 循环方式2
for i in range(len(list)):
    item = list[i]
    print('')
    print("## 第{}条信息".format(i))
    print("* id: {}".format(item['id']))
    print("* number: {}".format(item['number']))
    print("* title: {}".format(item['title']))
    print("* body: {}".format(item['body']))
# 循环方式3
for i, item in enumerate(list):
    print('')
    print("## 第{}条信息".format(i))
    print("* id: {}".format(item['id']))
    print("* number: {}".format(item['number']))
    print("* title: {}".format(item['title']))
    print("* body: {}".format(item['body']))

# while循环方式1
i = 0
while i < len(list):
    item = list[i]
    print('')
    print("## 第{}条信息".format(i))
    print("* id: {}".format(item['id']))
    print("* number: {}".format(item['number']))
    print("* title: {}".format(item['title']))
    print("* body: {}".format(item['body']))
    i += 1

# while循环方式2
i = 0
while True:
    item = list[i]
    print('')
    print("## 第{}条信息".format(i))
    print("* id: {}".format(item['id']))
    print("* number: {}".format(item['number']))
    print("* title: {}".format(item['title']))
    print("* body: {}".format(item['body']))
    i += 1
    if i == len(list):
        break
