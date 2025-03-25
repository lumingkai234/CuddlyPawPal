
import asyncio
import pathlib
import ssl
import websockets

async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")

    greeting = f"Hello {name}!"

    await websocket.send(greeting)
    print(f"> {greeting}")

async def main():
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    localhost_pem = pathlib.Path(__file__).with_name("cert.pem")
    localhost_key = pathlib.Path(__file__).with_name("key.pem")
    ssl_context.load_cert_chain(localhost_pem, keyfile=localhost_key)

    # 启动 WebSocket 服务器
    async with websockets.serve(hello, "0.0.0.0", 8080, ssl=ssl_context):
        print("WebSocket server started on wss://0.0.0.0:8080")
        await asyncio.Future()  # 保持服务器运行

# 使用 asyncio.run() 启动事件循环
if __name__ == "__main__":
    asyncio.run(main())