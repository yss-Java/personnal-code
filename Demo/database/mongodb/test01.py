from pymongo import MongoClient

client = MongoClient("mongodb://192.168.88.100:27017/")
db = client["mydb"]
#print(db)
#插入单个文档
collection = db["mydb"]
document = {"name": "John", "age": 30, "city": "New York"}
collection.insert_one(document)

#插入多个文档
documents = [
    {"name": "Anna", "age": 25, "city": "London"},
    {"name": "Mike", "age": 32, "city": "San Francisco"}
]
collection.insert_many(documents)

#查询单个文档
result = collection.find_one({"name": "John"})
print(result)

# 查询多个文档
results = collection.find({"city": "New York"})
for doc in results:
    print(doc)

# 更新单个文档
collection.update_one({"name": "John"}, {"$set": {"age": 31}})

# 更新多个文档
collection.update_many({"city": "New York"}, {"$set": {"city": "Los Angeles"}})

# 删除单个文档
collection.delete_one({"name": "John"})

# 删除多个文档
collection.delete_many({"city": "Los Angeles"})
