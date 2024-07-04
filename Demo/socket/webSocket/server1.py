import asyncio
import websockets

# 存储所有已连接的客户端
connected_clients = set()


# 定义处理WebSocket连接的逻辑
async def handle_websocket(websocket, path):
    print("WebSocket连接已建立")
    # 将新的客户端添加到已连接的客户端集合中
    connected_clients.add(websocket)

    try:
        while True:
            # 接收客户端发送的消息
            message = await websocket.recv()
            print(f"接收到消息：{message}")

            # 将消息发送给所有连接的客户端
            for client in connected_clients:
                await client.send(message)
                print(f"已发送消息给客户端：{message}")
    except websockets.exceptions.ConnectionClosedOK:
        print("WebSocket连接已关闭")
    finally:
        # 将断开连接的客户端从集合中移除
        connected_clients.remove(websocket)


# 启动WebSocket服务器
start_server = websockets.serve(handle_websocket, "localhost", 8000)

# 运行事件循环
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
