import websocket
import json
import time

def on_message(ws, message):
    print(f"收到消息: {message}")
    try:
        # 解析服务器返回的 JSON 消息
        response = json.loads(message)
        if response.get("type") == "hello" and response.get("transport") == "websocket":
            print("服务器已就绪，音频通道打开成功")
        else:
            print("收到未知消息，可能需要检查协议")
    except json.JSONDecodeError:
        print("收到非 JSON 消息")

def on_error(ws, error):
    print(f"发生错误: {error}")

def on_close(ws, close_status_code, close_msg):
    print("连接关闭")

def on_open(ws):
    print("连接已建立")
    # 构造并发送客户端 'hello' 消息
    hello_message = {
        "type": "hello",
        "version": 1,
        "transport": "websocket",
        "audio_params": {
            "format": "opus",
            "sample_rate": 16000,
            "channels": 1,
            "frame_duration": 60
        }
    }
    ws.send(json.dumps(hello_message))
    print("已发送客户端 'hello' 消息")

if __name__ == "__main__":
    websocket_url = "ws://175.27.227.48/ws/chip/"
    ws = websocket.WebSocketApp(websocket_url,
                                 on_message=on_message,
                                 on_error=on_error,
                                 on_close=on_close)
    ws.on_open = on_open
    # 设置超时时间，防止无限等待
    ws.run_forever(ping_interval=5, ping_timeout=2)