# 编写websocket服务器代码

import asyncio
import websockets


# 定义处理WebSocket连接的逻辑
async def handle_websocket(websocket, path):
    print("WebSocket连接已建立")
    try:
        while True:
            # 接收客户端发送的消息
            message = await websocket.recv()
            print(f"接收到消息：{message}")

            # 发送消息给客户端
            response = f"服务器已收到消息：{message}"
            await websocket.send(response)
            print(f"已发送响应：{response}")
    except websockets.exceptions.ConnectionClosedOK:
        print("WebSocket连接已关闭")


# 启动WebSocket服务器
start_server = websockets.serve(handle_websocket, "localhost", 8000)

# 运行事件循环
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
