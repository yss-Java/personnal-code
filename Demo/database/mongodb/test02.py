from pymongo import MongoClient

client = MongoClient("mongodb://192.168.88.100:27017/")
db = client["mydb"]
collection = db["user"]
# 插入订单信息
order = {
    "order_id": 12345,
    "customer_name": "John Doe",
    "items": [
        {"product_id": 1, "quantity": 2},
        {"product_id": 2, "quantity": 1}
    ],
    "total": 100.0
}
db.orders.insert_one(order)

# 查询订单信息
order = db.orders.find_one({"order_id": 12345})
print(order)

# 更新文档
collection.update_one({"name": "Alice"}, {"$set": {"age": 29}})

# 插入订单信息
order = {
    "order_id": 12345,
    "customer_name": "John Doe",
    "items": [
        {"product_id": 1, "quantity": 2},
        {"product_id": 2, "quantity": 1}
    ],
    "total": 100.0
}
db.orders.insert_one(order)
# 查询订单信息
order = db.orders.find_one({"order_id": 12345})
print(order)
