import json

async def handle_json_message(connection, message):
    msg_json = json.loads(message)
    if msg_json["type"] == "hello":
        print("welcome")
        await connection.websocket.send(json.dumps(connection.config["welcome_message"]))
    elif msg_json["type"] == "bye":
        print("bye")