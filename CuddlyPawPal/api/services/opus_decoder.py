import subprocess
from pathlib import Path

def decode_opus(input_file, output_file):
    """
    使用 ffmpeg 解码 OPUS 文件为 PCM 格式
    :param input_file: 输入的 OPUS 文件路径
    :param output_file: 输出的 PCM 文件路径
    """
    try:
        # 确保输入文件存在
        if not Path(input_file).exists():
            raise FileNotFoundError(f"Input file not found: {input_file}")

        # 调用 ffmpeg 解码 OPUS 文件
        command = [
            "ffmpeg",
            "-i", input_file,  # 输入文件
            "-f", "wav",       # 输出格式为 WAV
            "-ar", "16000",    # 采样率 16kHz
            "-ac", "1",        # 单声道
            output_file        # 输出文件
        ]
        subprocess.run(command, check=True)
        print(f"Decoded OPUS file saved to: {output_file}")
    except Exception as e:
        print(f"Error decoding OPUS file: {e}")
        raise
decode_opus("input.opus", "output.wav")