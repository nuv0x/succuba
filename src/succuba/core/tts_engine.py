from google.cloud import texttospeech

class TTSEngine:
    def __init__(self):
        """初始化 Google Cloud TTS 客户端"""
        self.client = texttospeech.TextToSpeechClient()

    def create_audio(self, text, output_path, rate="medium", pitch="0st", lang="cmn-CN"):
        """
        合成语音
        :param rate: 语速 (e.g., 'slow', '120%')
        :param pitch: 音高 (e.g., 'low', '+2st', '-2st')
        :param lang: 语言代码
        """
        voice_map = {
            "cmn-CN": "cmn-CN-Wavenet-A",
            "en-US": "en-US-Wavenet-D"
        }
        voice_name = voice_map.get(lang, "cmn-CN-Wavenet-A")

        # 构建 SSML，同时包含 rate 和 pitch 控制
        ssml = f"""
        <speak>
            <prosody rate="{rate}" pitch="{pitch}">
                {text}
            </prosody>
        </speak>
        """
        
        synthesis_input = texttospeech.SynthesisInput(ssml=ssml)
        
        voice = texttospeech.VoiceSelectionParams(
            language_code=lang, 
            name=voice_name
        )
        
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3
        )

        try:
            response = self.client.synthesize_speech(
                input=synthesis_input, 
                voice=voice, 
                audio_config=audio_config
            )
            with open(output_path, "wb") as out:
                out.write(response.audio_content)
        except Exception as e:
            print(f"❌ TTS 失败: {e}")