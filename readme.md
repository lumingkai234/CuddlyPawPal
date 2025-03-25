
```
KDPP/
├─ main.py              # 程序入口
├─ config.yaml          # 配置文件
├─ config.py            # 读取及管理配置
├─ core/
│  ├─ server.py         # 服务器相关逻辑
│  └─ connection.py     # 连接管理
├─ handle/
│  ├─ json_handle.py    # JSON 消息处理
│  └─ audio_handle.py   # 音频消息处理
├─ cert/
│  ├─ cert.pem
│  └─ key.pem
├─ tests/
│  ├─ test_server.py    # 测试示例
│  └─ test_connection.py
```