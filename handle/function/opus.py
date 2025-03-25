import subprocess
from pathlib import Path

class OpusDecoder:
    """
    OPUS 数据解码器，使用 ffmpeg 将 OPUS 文件解码为 PCM 或保存为 WAV 格式。
    """

    @staticmethod
    def decode_to_wav(input_file, output_file):
        """
        解码 OPUS 文件为 WAV 格式并保存到文件。
        :param input_file: 输入的 Opus 文件路径
        :param output_file: 输出的 WAV 文件路径
        """
        try:
            # 调用 ffmpeg 解码 Opus 文件为 WAV 文件
            command = [
                "ffmpeg",
                "-y",              # 覆盖同名文件
                "-i", input_file,  # 输入 Opus 文件路径
                "-f", "wav",       # 输出格式为 WAV
                "-ar", "16000",    # 采样率 16kHz
                "-ac", "1",        # 单声道
                output_file        # 输出文件路径
            ]
            subprocess.run(command, check=True)
            print(f"Decoded OPUS file saved to: {output_file}")
        except Exception as e:
            print(f"Error decoding OPUS file: {e}")
            raise

class OpusEncoder:
    """
    OPUS 数据编码器，使用 ffmpeg 将音频文件编码为 OPUS 格式。
    """

    @staticmethod
    def encode_to_opus(input_file, output_file, bitrate="32k"):
        """
        编码音频文件为 OPUS 格式并保存到文件。
        :param input_file: 输入的音频文件路径
        :param output_file: 输出的 OPUS 文件路径
        :param bitrate: 编码比特率，默认 32kbps
        """
        try:
            # 调用 ffmpeg 编码音频文件为 OPUS 文件
            command = [
                "ffmpeg",
                "-y",              # 覆盖同名文件
                "-i", input_file,  # 输入音频文件路径
                "-c:a", "libopus", # 使用 libopus 编码器
                "-b:a", bitrate,   # 设置比特率
                "-ar", "16000",    # 采样率 16kHz
                "-ac", "1",        # 单声道
                output_file        # 输出文件路径
            ]
            subprocess.run(command, check=True)
            print(f"Encoded audio file saved to: {output_file}")
        except Exception as e:
            print(f"Error encoding audio file to OPUS: {e}")
            raise