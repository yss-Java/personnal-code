import asyncio
import websockets


async def chat_client():
    async with websockets.connect("ws://localhost:8000/chat") as websocket:
        print("已连接到聊天室")

        while True:
            message = input("输入消息: ")
            await websocket.send(message)

            response = await websocket.recv()
            print(f"接收到消息: {response}")


# 运行聊天客户端
asyncio.get_event_loop().run_until_complete(chat_client())
