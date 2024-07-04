# 编写websocket客户端

import asyncio
import websockets


async def connect():
    async with websockets.connect("ws://localhost:8000") as websocket:
        print("已经连接到服务器")

        # 发送消息到服务器
        await websocket.send("Hello,Server!")

        # 接手服务器发送的消息
        message = await websocket.recv()
        print(f'接收到消息：{message}')

        # 关闭连接
        await websocket.close()
        print("连接已关闭")


# 运行客户端
asyncio.get_event_loop().run_until_complete(connect())
