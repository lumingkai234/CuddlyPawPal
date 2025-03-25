import asyncio
import websockets
import ssl
import os
from core.connection import ConnectionHandler


class Server:
    def __init__(self, config):
        # config
        self.config = config

        # ssl
        current_dir = os.path.dirname(os.path.abspath(__file__))
        localhost_pem = os.path.join(current_dir, "../cert/cert.pem")
        localhost_key = os.path.join(current_dir, "../cert/key.pem")
        self.ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        self.ssl_context.load_cert_chain(localhost_pem, keyfile=localhost_key)

    async def start(self):
        server_config = self.config["server"]
        host = server_config["ip"]
        port = server_config["port"]
        async with websockets.serve(self._handle_connection, host, port,ssl = self.ssl_context):
            await asyncio.Future()

    async def _handle_connection(self, websocket):
        """处理新连接，每次创建独立的ConnectionHandler"""
        handler = ConnectionHandler(self.config)
        await handler.handle_connection(websocket)
