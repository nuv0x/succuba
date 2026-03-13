# 💋 Succuba: Automated Video Production Engine

**Succuba** is a high-performance, industrial-grade automated video factory built on Python 3.12+. Designed for content creators and marketers, it transforms raw Excel scripts into polished videos featuring high-quality AI voiceovers, dynamic subtitles, and synchronized background music.

---

## ✨ Core Features

* **Multi-Language Dubbing**: Powered by Google Cloud TTS (Wavenet/Neural2), supporting Mandarin, English, Japanese, and more.
* **Precision Audio Control**: Full support for SSML, allowing granular control over **Rate** (speed) and **Pitch** (tone).
* **Automated Visuals**: Automatically pairs scripts with background images and overlays beautiful, wrap-around subtitles.
* **Smart Audio Mixing**: Includes auto-ducking logic to ensure the background music (BGM) doesn't drown out the voiceover.
* **Modern Pipeline**: Built with `uv` for lightning-fast dependency resolution and `Pathlib` for cross-platform compatibility.

---

## 📂 Project Structure

```text
succuba/
├── data/
│   ├── raw/                # Place your input_scripts.xlsx here
│   ├── background_imgs/    # Image assets (e.g., bg.jpg)
│   └── bgm/                # Background music assets (e.g., chill.mp3)
├── output/
│   ├── audio/              # Generated intermediate MP3 files
│   └── video/              # Final .mp4 production exports
├── src/
│   └── succuba/            # Core source code
│       ├── core/           # Engine, TTS, and Video Builder logic
│       └── utils/          # Data processors and helpers
├── .env                    # Secret API credentials (ignored by git)
├── pyproject.toml          # Project metadata and dependencies
└── README.md