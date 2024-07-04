dict1 = {"a": 100, "b": 200, "c": 300}
dict2 = {v: k for k, v in dict1.items()}

print(dict2)
