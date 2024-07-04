from pymongo import MongoClient

client = MongoClient("mongodb://192.168.88.100:27017/")
db = client["mydb"]

# # 插入日志信息
# log_entry = {
#     "timestamp": "2024-05-19T12:34:56",
#     "level": "INFO",
#     "message": "User logged in",
#     "user_id": "john_doe"
# }
# db.logs.insert_one(log_entry)
#
# # 查询日志信息
# logs = db.logs.find({"user_id": "john_doe"})
# for log in logs:
#     print(log)

# 插入配置
config = {
    "app_name": "MyApp",
    "version": "1.0",
    "settings": {
        "theme": "dark",
        "notifications": True
    }
}
db.configs.insert_one(config)

# 查询配置
config = db.configs.find_one({"app_name": "MyApp"})
print(config)
