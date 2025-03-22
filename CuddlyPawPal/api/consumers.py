from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ChipConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 接受 WebSocket 连接
        await self.accept()
        await self.send(text_data=json.dumps({"message": "Connected to server"}))

    async def disconnect(self, close_code):
        # 处理断开连接
        print(f"WebSocket disconnected: {close_code}")

    async def receive(self, text_data):
        # 接收客户端消息
        data = json.loads(text_data)
        print(f"Received data from client: {data}")

        # 构造返回消息
        user_message = data.get("message", "")
        greeting = f"Hello {user_message}!"

        # 返回响应
        response = {"message": greeting}
        await self.send(text_data=json.dumps(response))