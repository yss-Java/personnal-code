import json
from datetime import datetime


# 日期编码
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        return json.JSONEncoder.default(self, obj)


d = {'date': datetime.now()}
json_str = json.dumps(d, cls=DateEncoder)
print(json_str)


# 日期解码
class DateDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict_to_object)

    def dict_to_object(self, d):
        if 'date' in d:
            d['date'] = datetime.strptime(d['date'], '%Y-%m-%d %H:%M:%S')
        return d


data = json.loads(json_str, cls=DateDecoder)

print(data)
