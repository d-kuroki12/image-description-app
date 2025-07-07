"""
ユーティリティ関数（Azure対応版）
"""

import streamlit as st
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import gc
from config import *

# Azure環境での最適化
if IS_AZURE:
    torch.set_num_threads(2)
    import os
    os.environ["TORCH_NUM_THREADS"] = "2"
    os.environ["MKL_NUM_THREADS"] = "2"
    os.environ["OMP_NUM_THREADS"] = "2"

# ===== 画像処理関数 =====

def validate_image(uploaded_file):
    """画像の検証"""
    if uploaded_file is None:
        return False, "ファイルが選択されていません"
    
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension not in SUPPORTED_FORMATS:
        return False, f"サポートされていない形式です。({', '.join(SUPPORTED_FORMATS)}のみ対応)"
    
    if uploaded_file.size > MAX_FILE_SIZE_MB * 1024 * 1024:
        return False, f"ファイルサイズが{MAX_FILE_SIZE_MB}MBを超えています"
    
    return True, ""

def preprocess_image(image):
    """画像の前処理"""
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    if image.size[0] > MAX_IMAGE_SIZE[0] or image.size[1] > MAX_IMAGE_SIZE[1]:
        image.thumbnail(MAX_IMAGE_SIZE, Image.Resampling.LANCZOS)
    
    return image

def get_image_info(image, filename):
    """画像情報の取得"""
    return {
        "ファイル名": filename,
        "サイズ": f"{image.size[0]} x {image.size[1]} pixels",
        "フォーマット": image.format or "Unknown",
        "カラーモード": image.mode
    }

# ===== AI関連関数 =====

@st.cache_resource
def load_blip_model():
    """BLIPモデルのロード"""
    try:
        with st.spinner("AIモデルを初期化中...（初回のみ時間がかかります）"):
            st.info("📥 Hugging Faceからモデルをダウンロード中...")
            
            # よりシンプルな読み込み方法
            processor = BlipProcessor.from_pretrained(
                BLIP_MODEL,
                cache_dir="./model_cache"  # ローカルキャッシュディレクトリを指定
            )
            
            model = BlipForConditionalGeneration.from_pretrained(
                BLIP_MODEL,
                cache_dir="./model_cache",
                torch_dtype=torch.float32
            )
            
        st.success("✅ AIモデルの読み込みが完了しました！")
        return processor, model
        
    except Exception as e:
        st.error(f"❌ モデルのロードでエラー: {str(e)}")
        
        # デバッグ情報を追加
        st.markdown("### 🔍 デバッグ情報")
        st.write(f"**エラーの詳細**: {str(e)}")
        st.write(f"**モデル名**: {BLIP_MODEL}")
        
        # 対処法を表示
        st.markdown("### 💡 対処法")
        st.markdown("""
        1. **インターネット接続を確認**してください
        2. **VPNを使用している場合は一時的に無効**にしてください
        3. **しばらく時間をおいて再試行**してください
        4. **ページを再読み込み**してください
        """)
        
        return None, None

def translate_to_japanese(text):
    """基本的な英日翻訳"""
    text_lower = text.lower()
    for eng, jp in TRANSLATION_DICT.items():
        if eng in text_lower:
            text_lower = text_lower.replace(eng, jp)
    return text_lower

def describe_image_with_blip(image, processor, model, language="ja"):
    """BLIPモデルで画像を説明（Azure最適化版）"""
    try:
        inputs = processor(image, return_tensors="pt")
        
        # Azure環境での最適化設定
        generation_kwargs = {
            "max_length": MAX_TOKENS,
            "num_beams": NUM_BEAMS,
            "early_stopping": True,
            "do_sample": False if IS_AZURE else True,  # Azureでは決定論的生成
        }
        
        with torch.no_grad():
            out = model.generate(**inputs, **generation_kwargs)
        
        description = processor.decode(out[0], skip_special_tokens=True)
        
        if language == "ja":
            description = translate_to_japanese(description)
        
        # Azure環境でのメモリクリーンアップ
        if IS_AZURE:
            del inputs, out
            gc.collect()
        
        return description
        
    except Exception as e:
        error_msg = f"エラーが発生しました: {str(e)}"
        if IS_AZURE:
            error_msg += "\n（Azure環境での処理中）"
        return error_msg

def get_model_info():
    """使用モデルの情報を取得"""
    return {
        "モデル名": "BLIP (Bootstrapping Language-Image Pre-training)",
        "開発元": "Salesforce Research",
        "種類": "画像キャプション生成モデル",
        "実行環境": "Azure App Service" if IS_AZURE else "ローカル環境",
        "特徴": "無料で使用可能なオープンソースモデル"
    }