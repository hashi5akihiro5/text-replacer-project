# Pythonベースイメージを使用
FROM python:3.9-slim

WORKDIR /app

# 必要なPythonパッケージをインストール
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt