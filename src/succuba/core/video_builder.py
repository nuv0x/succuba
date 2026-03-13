from moviepy.editor import ImageClip, AudioFileClip, TextClip, CompositeVideoClip, CompositeAudioClip

class VideoBuilder:
    @staticmethod
    def build_video(audio_path, img_path, output_path, text, bgm_path=None):
        """合成视频、动态字幕、背景音乐"""
        try:
            # 配音与图片
            voice = AudioFileClip(str(audio_path))
            bg_clip = ImageClip(str(img_path)).set_duration(voice.duration)

            # 字幕 (需系统支持字体)
            txt_clip = TextClip(
                text, fontsize=40, color='white', font='SimHei',
                method='caption', size=(bg_clip.w * 0.8, None)
            ).set_duration(voice.duration).set_position(('center', 'bottom'))

            # 背景音乐混合
            final_audio = voice
            if bgm_path and bgm_path.exists():
                bgm = AudioFileClip(str(bgm_path)).volumex(0.1).set_duration(voice.duration)
                final_audio = CompositeAudioClip([voice, bgm])

            # 合成并输出
            video = CompositeVideoClip([bg_clip, txt_clip]).set_audio(final_audio)
            video.write_videofile(str(output_path), fps=24, codec="libx264", logger=None)
            
            video.close()
            voice.close()
            return True
        except Exception as e:
            print(f"视频合成出错: {e}")
            return False