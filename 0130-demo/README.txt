## プロジェクト構成

- **バックエンド:** Flask (Python)
- **データベース:** PostgreSQL
- **環境構築:** Docker

---

### ⚠ 前提条件
事前に[Docker Desktop](https://www.docker.com/ja-jp/products/docker-desktop/)をインストールしておいてください。

---

## 起動方法
- このプロジェクトではDockerを使用しているので、`docker`コマンドを使います。

### 起動
dockerのデスクトップアプリを起動した状態で
cdコマンドで0130-demoのディレクトリまで移動

docker compose up

### 更新ビルド
cdコマンドでdemo-0130のディレクトリまで移動

docker compose up --build -d

### コンテナ削除(作業終了したら...)
cdコマンドでdemo-0130のディレクトリまで移動

docker compose down --rmi all
