import json
from function.opus import OpusDecoder, OpusEncoder
from function.speech_to_text import SpeechToText
from function.text_to_text import TextToText
from function.text_to_speech import TextToSpeech
async def handle_audio_message(connection, message):
    decoder = OpusDecoder()
    decoder.decode(message,"handle/temp/opus_data.wav")
    stt = SpeechToText()
    text = stt.transcribe("handle/temp/opus_data.wav")
    ttt = TextToText()
    response = ttt.generate_text(text)
    tts = TextToSpeech()
    audio_data = tts.tts(response)
    encoder = OpusEncoder()
    encoder.encode_to_opus(audio_data,"handle/temp/test_submit.opus")
    with open("handle/temp/test_submit.opus", "rb") as opus_file:
        opus_data = opus_file.read()

    # 发送 Opus 数据
    await connection.websocket.send(opus_data)
    
def test_handle_audio_message():
    decoder = OpusDecoder()
    decoder.decode_to_wav("/home/ubuntu/KDPP/handle/temp/test.opus","/home/ubuntu/KDPP/handle/temp/opus_data.wav")
    stt = SpeechToText()
    text = stt.transcribe("handle/temp/test.wav")
    print(text)
    ttt = TextToText()
    response = ttt.generate_text(text)
    print(response)
    tts = TextToSpeech()
    audio_data = tts.tts(response)
    # encoder = OpusEncoder()
    # encoder.encode_to_opus(audio_data,"/home/ubuntu/KDPP/handle/temp.opus")
    with open("handle/temp/test_submit.wav", "wb") as file_to_save:
        file_to_save.write(audio_data)
    print("Audio file saved as test_submit.wav")
test_handle_audio_message()