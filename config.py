"""
アプリ設定ファイル（Azure対応版）
"""
import os

# Azure環境の検出
IS_AZURE = os.getenv('WEBSITE_SITE_NAME') is not None

# アプリの基本設定
APP_TITLE = "📸 画像説明アプリ（無料版）"
APP_ICON = "📸"

# 画像設定（Azureでは制限を厳しく）
MAX_IMAGE_SIZE = (600, 400) if IS_AZURE else (800, 600)
SUPPORTED_FORMATS = ['png', 'jpg', 'jpeg', 'gif', 'bmp']
MAX_FILE_SIZE_MB = 5 if IS_AZURE else 10

# BLIPモデル設定（Azureでは軽量化）
BLIP_MODEL = "Salesforce/blip-image-captioning-base"
MAX_TOKENS = 30 if IS_AZURE else 50
NUM_BEAMS = 3 if IS_AZURE else 5

# 日本語翻訳辞書
TRANSLATION_DICT = {
    # 人物
    "a woman": "女性",
    "a man": "男性", 
    "a person": "人",
    "a girl": "女の子",
    "a boy": "男の子",
    "people": "人々",
    
    # 動物
    "a cat": "猫",
    "a dog": "犬",
    "a bird": "鳥",
    "a horse": "馬",
    
    # 物
    "a car": "車",
    "a house": "家",
    "a tree": "木",
    "a flower": "花",
    "a book": "本",
    "a phone": "電話",
    
    # 動作
    "sitting": "座っている",
    "standing": "立っている",
    "walking": "歩いている",
    "running": "走っている",
    "smiling": "笑っている",
    "looking": "見ている",
    "wearing": "着ている",
    "holding": "持っている",
    
    # 場所・位置
    "in front of": "の前に",
    "next to": "の隣に",
    "on": "の上に",
    "in": "の中に",
    "with": "と一緒に",
    
    # 色
    "black": "黒い",
    "white": "白い",
    "red": "赤い",
    "blue": "青い",
    "green": "緑の",
    
    # その他
    "the": "",
    "and": "と"
}

# サポート言語
SUPPORTED_LANGUAGES = {
    "ja": "日本語",
    "en": "English"
}