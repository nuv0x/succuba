import pandas as pd
from pathlib import Path

def load_and_clean_data(file_path: Path):
    """读取并预处理 Excel 脚本"""
    if not file_path.exists():
        raise FileNotFoundError(f"找不到 Excel 文件: {file_path}")
    
    df = pd.read_excel(file_path)
    # 过滤 text 为空的行
    df = df.dropna(subset=['text'])
    
    # 设置默认值，防止 Excel 漏填
    df['id'] = df.get('id', range(len(df)))
    df['rate'] = df.get('rate', 'medium')
    df['lang'] = df.get('lang', 'cmn-CN')
    df['image'] = df.get('image', 'default.jpg')
    df['bgm'] = df.get('bgm', None)
    
    return df