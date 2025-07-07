# 📸 画像説明アプリ（無料版）

BLIPモデルを使用した無料の画像説明生成アプリです。ローカル環境とAzure App Serviceの両方で動作します。

## 🎯 特徴

- 🆓 **完全無料** - API料金なし
- 🤖 **BLIPモデル使用** - Salesforce製の高性能画像認識AI
- 🌐 **日本語対応** - 基本的な英日翻訳機能付き
- 🖼️ **多形式対応** - PNG, JPG, JPEG, GIF, BMP
- ⚡ **高速処理** - ローカルで動作
- ☁️ **Azure対応** - App Serviceでの本番運用可能
- 📱 **レスポンシブ** - モバイル・デスクトップ両対応

## 🚀 クイックスタート

### ローカル環境での実行

```bash
# リポジトリのクローン
git clone <your-repo-url>
cd my_image_app

# 仮想環境の作成
python -m venv venv
source venv/bin/activate  # macOS/Linux
# または
venv\Scripts\activate     # Windows

# 依存関係のインストール
pip install -r requirements.txt

# アプリの実行
streamlit run app.py
```

## 📁 プロジェクト構造

```
my_image_app/
├── app.py                 # メインアプリケーション
├── config.py              # 設定ファイル（Azure対応）
├── utils.py               # ユーティリティ関数（Azure最適化）
├── requirements.txt       # 依存関係
├── runtime.txt            # Python バージョン（Azure用）
├── startup.sh             # 起動スクリプト（Azure用）
├── .deployment            # デプロイ設定（Azure用）
├── .streamlit/
│   └── config.toml        # Streamlit設定
├── .gitignore             # Git除外設定
└── README.md              # このファイル
```

## 🖥️ 使い方

1. **アプリ起動** - ブラウザで http://localhost:8501 にアクセス
2. **環境確認** - ローカル/Azure環境が自動判別される
3. **画像選択** - 左側で画像をアップロード
4. **説明生成** - 「説明を生成」ボタンをクリック
5. **結果確認** - 右側にAIが生成した説明が表示

## ☁️ Azure App Service デプロイ

### 前提条件
- Azure アカウント
- GitHub アカウント
- Git の基本知識

### デプロイ手順

1. **GitHub リポジトリの作成**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Azure App Service の作成**
   - Azure Portal にログイン
   - App Service を新規作成
   - Runtime: Python 3.9, Linux
   - Pricing tier: F1 (Free)

3. **GitHub 連携の設定**
   - Deployment Center を開く
   - Source: GitHub
   - Repository と Branch を選択
   - Save

4. **自動デプロイの確認**
   - デプロイログを確認
   - アプリのURLにアクセス

## 📋 動作環境

### ローカル環境
- **Python**: 3.8以上
- **メモリ**: 最低4GB推奨
- **ストレージ**: 約2GB（モデルダウンロード用）
- **インターネット**: 初回のみ必要

### Azure App Service
- **Runtime**: Python 3.9
- **Pricing**: F1 (Free) 以上
- **制限**: メモリ1GB、CPU制限あり
- **最適化**: 自動的に軽量設定に切り替わります

## 🔧 トラブルシューティング

### ローカル環境

**モデルダウンロードエラー**
```bash
# パッケージの再インストール
pip install --upgrade transformers torch
```

**メモリエラー**
- より小さな画像を使用
- 他のアプリケーションを閉じる

### Azure環境

**デプロイエラー**
- requirements.txt の依存関係を確認
- ログを Azure Portal で確認

**パフォーマンス問題**
- 画像サイズを5MB以下に制限
- Free Tier の制限を確認

## 🤖 使用技術

- **Frontend**: Streamlit
- **AI Model**: BLIP (Salesforce)
- **Backend**: PyTorch, Transformers
- **Cloud**: Azure App Service
- **CI/CD**: GitHub Actions (自動デプロイ)

## ⚙️ 設定

### 環境別設定

アプリは実行環境を自動判別し、適切な設定に切り替わります：

| 設定項目 | ローカル | Azure |
|---------|---------|-------|
| 最大画像サイズ | 800x600 | 600x400 |
| ファイルサイズ上限 | 10MB | 5MB |
| 生成トークン数 | 50 | 30 |
| ビーム数 | 5 | 3 |

### カスタマイズ

設定を変更したい場合は `config.py` を編集してください。

## 📄 ライセンス

MIT License

## 🙋‍♂️ サポート

問題が発生した場合：
1. [Issues](link-to-issues) で報告
2. [Discussions](link-to-discussions) で質問
3. README のトラブルシューティングを確認

## 🤝 貢献

プルリクエストやイシューの報告を歓迎します！

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

**🌟 スターをいただけると開発の励みになります！**