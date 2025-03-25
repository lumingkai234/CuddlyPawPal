import threading
import websockets
from handle.json_handle import handle_json_message
from handle.audio_handle import handle_audio_message

class ConnectionHandler:
    def __init__(self, config):
        self.config = config
        pass

    async def handle_connection(self, websocket):
        self.websocket = websocket
        try:
            async for message in self.websocket:
                await self.route_message(message)
        except websockets.exceptions.ConnectionClosed:
            pass

    async def route_message(self, message):
        """消息路由"""
        if isinstance(message, str):
            await handle_json_message(self, message)
        elif isinstance(message, bytes):
            await handle_audio_message(self, message)
