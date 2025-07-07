"""
画像説明アプリ（無料版）- メインファイル
"""

import streamlit as st
from PIL import Image
from config import APP_TITLE, APP_ICON, SUPPORTED_LANGUAGES, IS_AZURE
from utils import (
    validate_image, 
    preprocess_image, 
    get_image_info,
    load_blip_model, 
    describe_image_with_blip,
    get_model_info
)

# アプリケーションの設定
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

def show_header():
    """ヘッダー部分の表示"""
    st.title(APP_TITLE)
    
    # 実行環境の表示
    if IS_AZURE:
        st.success("🌐 Azure App Service 上で動作中")
    else:
        st.info("💻 ローカル環境で動作中")
    
    st.markdown("""
    写真をアップロードすると、AIが自動で説明を生成します。  
    **完全無料** で使用できるオープンソースのBLIPモデルを使用しています。
    """)
    
    # 注意事項
    with st.expander("⚠️ 初回利用時の注意"):
        st.warning("""
        **初回実行時にはAIモデルのダウンロードが発生します**
        - ダウンロードサイズ: 約1-2GB
        - 所要時間: 5-10分程度（回線速度による）
        - インターネット接続が必要です
        
        一度ダウンロードされれば、次回からはオフラインでも使用できます。
        """)

def show_sidebar():
    """サイドバーの表示"""
    with st.sidebar:
        st.header("⚙️ 設定")
        
        # 言語選択
        language = st.selectbox(
            "出力言語",
            options=list(SUPPORTED_LANGUAGES.keys()),
            format_func=lambda x: SUPPORTED_LANGUAGES[x],
            index=0  # デフォルトは日本語
        )
        
        st.markdown("---")
        
        # 使い方
        st.markdown("### 📋 使い方")
        st.markdown("""
        1. **画像をアップロード**  
           左側のアップロードエリアに画像をドラッグ&ドロップ
        
        2. **説明を生成**  
           「説明を生成」ボタンをクリック
        
        3. **結果を確認**  
           右側にAIによる説明が表示されます
        """)
        
        st.markdown("---")
        
        # モデル情報
        st.markdown("### 🤖 AIモデル情報")
        model_info = get_model_info()
        for key, value in model_info.items():
            st.markdown(f"**{key}**: {value}")
        
        return language

def main():
    """メイン関数"""
    
    # ヘッダーの表示
    show_header()
    
    # サイドバーの表示
    language = show_sidebar()
    
    # BLIPモデルのロード
    processor, model = load_blip_model()
    
    if processor is None or model is None:
        st.error("❌ AIモデルの初期化に失敗しました。ページを再読み込みしてください。")
        st.stop()
    
    # メインコンテンツエリア
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📤 画像をアップロード")
        uploaded_file = st.file_uploader(
            "画像ファイルを選択してください",
            type=['png', 'jpg', 'jpeg', 'gif', 'bmp'],
            help="対応形式: PNG, JPG, JPEG, GIF, BMP（最大10MB）"
        )
        
        if uploaded_file is not None:
            # 画像の検証
            is_valid, error_message = validate_image(uploaded_file)
            if not is_valid:
                st.error(f"❌ {error_message}")
                return
            
            # 画像の読み込みと前処理
            try:
                image = Image.open(uploaded_file)
                processed_image = preprocess_image(image)
                
                # 画像の表示
                st.image(
                    processed_image, 
                    caption="📷 アップロードされた画像", 
                    use_column_width=True
                )
                
                # 画像情報の表示
                image_info = get_image_info(processed_image, uploaded_file.name)
                with st.expander("📊 画像の詳細情報"):
                    for key, value in image_info.items():
                        st.markdown(f"**{key}**: `{value}`")
                
            except Exception as e:
                st.error(f"❌ 画像の読み込みでエラーが発生しました: {str(e)}")
                return
        else:
            # 画像がアップロードされていない場合
            st.info("👆 上記のエリアに画像ファイルをドラッグ&ドロップするか、クリックしてファイルを選択してください。")
    
    with col2:
        st.header("🤖 AIによる画像説明")
        
        if uploaded_file is not None:
            if st.button("🚀 説明を生成", type="primary", use_container_width=True):
                
                with st.spinner("🧠 AIが画像を分析中..."):
                    description = describe_image_with_blip(processed_image, processor, model, language)
                
                # 結果の表示
                st.markdown("### 📝 生成された説明")
                st.success(description)
                
                # メタ情報
                st.markdown("---")
                st.caption(f"🤖 使用モデル: BLIP | 🌐 環境: {'Azure' if IS_AZURE else 'ローカル'}")
                st.caption("⚠️ この説明は機械学習モデルによって生成されており、完全に正確ではない場合があります。")
        else:
            st.info("👈 まず左側で画像をアップロードしてください。")

if __name__ == "__main__":
    main()