#!/bin/bash

echo "🚀 Starting Streamlit app on Azure..."

# Azure環境変数の設定
export STREAMLIT_SERVER_PORT=${PORT:-8000}
export STREAMLIT_SERVER_ADDRESS=0.0.0.0
export STREAMLIT_SERVER_HEADLESS=true
export STREAMLIT_BROWSER_GATHER_USAGE_STATS=false

# メモリ最適化
export TORCH_NUM_THREADS=2
export MKL_NUM_THREADS=2
export OMP_NUM_THREADS=2

# Streamlit起動
python -m streamlit run app.py \
    --server.port $STREAMLIT_SERVER_PORT \
    --server.address $STREAMLIT_SERVER_ADDRESS \
    --server.headless true \
    --browser.gatherUsageStats false
