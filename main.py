import asyncio
import sys
import signal
from core.server import Server
from config import read_config


async def wait_for_exit():
    """Windows 和 Linux 兼容的退出监听"""
    loop = asyncio.get_running_loop()
    stop_event = asyncio.Event()

    if sys.platform == "win32":
        await loop.run_in_executor(None, sys.stdin.read)
    else:

        def stop():
            stop_event.set()

        loop.add_signal_handler(signal.SIGINT, stop)
        loop.add_signal_handler(signal.SIGTERM, stop)
        await stop_event.wait()


async def main():
    # config
    config = read_config()

    # server
    ws_server = Server(config)
    ws_task = asyncio.create_task(ws_server.start())
    try:
        # 监听退出信号
        await wait_for_exit()
    except asyncio.CancelledError:
        print("任务被取消，清理资源中...")
    finally:
        # 取消 WebSocket 服务器任务
        ws_task.cancel()
        try:
            # 等待取消操作完成
            await ws_task
        except asyncio.CancelledError:
            pass
        print("服务器已关闭，程序退出。")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("手动中断，程序终止。")
