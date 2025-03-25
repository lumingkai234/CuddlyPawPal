import base64
import json
import uuid
import requests


class TextToSpeech:
    def __init__(self, cluster="volcano_tts", host="openspeech.bytedance.com"):
        # 将 appid 和 access_token 写死到类中
        self.appid = "4080460959"
        self.access_token = "qO6N_TJfp1lOGL8HtyS9wuawO7oZkVTQ"
        self.cluster = cluster
        self.host = host
        self.api_url = f"https://{host}/api/v1/tts"
        self.header = {"Authorization": f"Bearer;{self.access_token}"}

    def tts(self, text, voice_type="BV001_streaming", encoding="wav", speed_ratio=1.0, volume_ratio=1.0, pitch_ratio=1.0):
        """
        调用字节跳动语音合成接口，将文本转换为语音文件。

        :param text: 要合成的文本
        :param voice_type: 语音类型，默认 "BV001_streaming"
        :param encoding: 音频编码格式，默认 "wav"
        :param speed_ratio: 语速比例，默认 1.0
        :param volume_ratio: 音量比例，默认 1.0
        :param pitch_ratio: 音高比例，默认 1.0
        :return: 合成的音频文件内容（字节流）
        """
        request_json = {
            "app": {
                "appid": self.appid,
                "token": self.access_token,
                "cluster": self.cluster
            },
            "user": {
                "uid": str(uuid.uuid4())
            },
            "audio": {
                "voice_type": voice_type,
                "encoding": encoding,
                "speed_ratio": speed_ratio,
                "volume_ratio": volume_ratio,
                "pitch_ratio": pitch_ratio,
            },
            "request": {
                "reqid": str(uuid.uuid4()),
                "text": text,
                "text_type": "plain",
                "operation": "query",
                "with_frontend": 1,
                "frontend_type": "unitTson"
            }
        }

        try:
            resp = requests.post(self.api_url, json.dumps(request_json), headers=self.header)
            resp_json = resp.json()
            if "data" in resp_json:
                data = resp_json["data"]
                return base64.b64decode(data)
            else:
                raise Exception(f"TTS API Error: {resp_json}")
        except Exception as e:
            raise Exception(f"Error during TTS request: {str(e)}")


# 示例用法
if __name__ == '__main__':
    tts_client = TextToSpeech()
    try:
        audio_data = tts_client.tts("字节跳动语音合成")
        with open("test_submit.wav", "wb") as file_to_save:
            file_to_save.write(audio_data)
        print("Audio file saved as test_submit.wav")
    except Exception as e:
        print(f"Error: {e}")