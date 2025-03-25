import requests

class TextToText:
    # 写死 API 端点和密钥
    _API_URL = "https://ark.cn-beijing.volces.com/api/v3/chat/completions"
    _API_KEY = "49dbac58-8efc-45db-9338-1682cf7b8fd9"

    def __init__(self):
        """
        初始化 TextToTextAPI 类
        """
        self.headers = {
            "Authorization": f"Bearer {self._API_KEY}",
            "Content-Type": "application/json"
        }

    def generate_text(self, input_text, model="doubao-1.5-pro-32k-250115", max_tokens=50, temperature=0.7):
        """
        调用 API 生成文本
        :param input_text: 用户输入文本
        :param model: 使用的模型
        :param max_tokens: 最大生成的 token 数
        :param temperature: 生成文本的随机性
        :return: 生成的文本
        """
        data = {
            "model": model,
            "messages": [
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": input_text}
            ],
            "max_tokens": max_tokens,
            "temperature": temperature
        }

        response = requests.post(self._API_URL, headers=self.headers, json=data, verify=False)

        if response.status_code == 200:
            result = response.json()
            return result["choices"][0]["message"]["content"]
        else:
            raise Exception(f"请求失败，状态码：{response.status_code}，错误信息：{response.text}")
