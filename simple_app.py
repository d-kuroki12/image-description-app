"""
軽量テスト版アプリ
"""

import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="🧪 テスト版画像アプリ",
    page_icon="🧪",
    layout="wide"
)

st.title("🧪 テスト版画像アプリ")
st.write("まずは基本的な画像アップロード機能をテストします。")

# 画像アップロード
uploaded_file = st.file_uploader(
    "画像をアップロードしてください",
    type=['png', 'jpg', 'jpeg', 'gif', 'bmp']
)

if uploaded_file is not None:
    try:
        # 画像を読み込み
        image = Image.open(uploaded_file)
        
        # 画像を表示
        st.image(image, caption="アップロードされた画像", use_column_width=True)
        
        # 画像情報を表示
        st.write(f"**ファイル名**: {uploaded_file.name}")
        st.write(f"**サイズ**: {image.size[0]} x {image.size[1]} pixels")
        st.write(f"**フォーマット**: {image.format}")
        
        st.success("✅ 基本的な画像処理は正常に動作しています！")
        st.info("AI機能を有効にするには、PyTorchとTransformersの問題を解決する必要があります。")
        
    except Exception as e:
        st.error(f"エラーが発生しました: {str(e)}")
else:
    st.info("画像をアップロードしてください。")

st.markdown("---")
st.markdown("### 📋 次のステップ")
st.markdown("""
1. この軽量版が動作すれば、Streamlit自体は正常です
2. PyTorchとNumPyの互換性を解決します
3. AI機能を追加します
""")