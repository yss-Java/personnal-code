import json

data = [{'name': '张三', 'age': 18}, {'name': '李四', 'age': 20}]
json_str = json.dumps(data)
print(type(json_str))
result = json.loads(json_str)
print(type(result))
