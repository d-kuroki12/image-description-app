"""
最小テスト版アプリ
"""

import streamlit as st
import os

# Azure環境の検出
IS_AZURE = os.getenv('WEBSITE_SITE_NAME') is not None

# アプリ設定
st.set_page_config(
    page_title="🧪 テストアプリ",
    page_icon="🧪"
)

def main():
    st.title("🧪 Azure デプロイテスト")
    
    # 環境表示
    if IS_AZURE:
        st.success("🎉 Azure App Service デプロイ成功！")
        st.balloons()
    else:
        st.info("💻 ローカル環境で動作中")
    
    st.markdown("## ✅ 動作確認")
    st.write("このページが表示されれば、デプロイは成功しています！")
    
    # 簡単な機能テスト
    st.markdown("## 🧪 機能テスト")
    
    name = st.text_input("あなたの名前を入力してください")
    if name:
        st.write(f"こんにちは、{name}さん！")
    
    if st.button("テストボタン"):
        st.success("ボタンが正常に動作しています！")
    
    # 環境情報
    st.markdown("## 📋 環境情報")
    st.write(f"**実行環境**: {'Azure App Service' if IS_AZURE else 'ローカル'}")
    
    if IS_AZURE:
        st.write("**Azure Free Tier で動作中**")
        st.info("🔄 次のステップ: 段階的に機能を追加していきます")

if __name__ == "__main__":
    main()
