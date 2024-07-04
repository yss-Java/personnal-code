def list_to_dict(list, key_func):
    d = {}
    for item in list:
        k = key_func(item)
        v = item
        list = d.get(k)
        if list is None:
            d[k] = [v]
        else:
            d[k].append(v)
    return d


if __name__ == '__main__':
    list = [
        {"name": "alice", "age": 100},
        {"name": "middle", "age": 100},
        {"name": "bob", "age": 200}
    ]
get_key = lambda item: item['age']
ret = list_to_dict(list, get_key)
print(ret)
