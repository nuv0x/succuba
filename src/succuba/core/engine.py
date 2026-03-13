import os
from pathlib import Path
from dotenv import load_dotenv
from succuba.utils.processor import load_and_clean_data
from succuba.core.tts_engine import TTSEngine
from succuba.core.video_builder import VideoBuilder

load_dotenv()

def run_pipeline():
    # 1. 路径锚定
    BASE = Path(__file__).resolve().parent.parent.parent.parent
    EXCEL = BASE / "data/raw/input_scripts.xlsx"
    OUT_V = BASE / "output/video"
    OUT_A = BASE / "output/audio"
    [d.mkdir(parents=True, exist_ok=True) for d in [OUT_V, OUT_A]]

    # 2. 初始化
    df = load_and_clean_data(EXCEL)
    tts = TTSEngine()
    vb = VideoBuilder()

    # 3. 循环处理
    for _, row in df.iterrows():
        print(f"🚀 处理中: {row['id']}")
        
        audio_p = OUT_A / f"{row['id']}.mp3"
        video_p = OUT_V / f"{row['id']}.mp4"
        img_p = BASE / "data/background_imgs" / row['image']
        bgm_p = BASE / "data/bgm" / str(row['bgm']) if row['bgm'] else None

        # 执行流程
        tts.create_audio(row['text'], audio_p, row['rate'], row['pitch'], row['lang'])
        vb.build_video(audio_p, img_p, video_p, row['text'], bgm_p)

    print("✨ 全部完成!")