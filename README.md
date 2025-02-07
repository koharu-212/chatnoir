このプロジェクトは、Flask (Python) をバックエンドとして使用し、PostgreSQL をデータベースに採用した Web アプリケーションです。開発環境は Docker を利用して構築されています。

環境構成

バックエンド: Flask (Python)

データベース: PostgreSQL

環境構築: Docker

前提条件

本プロジェクトを実行するには、以下のソフトウェアが事前にインストールされている必要があります。

Docker Desktop（最新バージョン推奨）

起動方法

Docker Desktopを起動

プロジェクトディレクトリへ移動

cd final ver

コンテナの起動

docker compose up

ブラウザでアクセス

http://localhost:5000/

更新ビルド（変更を適用する場合）

プロジェクトディレクトリへ移動

cd final ver

再ビルドとバックグラウンド起動

docker compose up --build -d

コンテナの停止と削除（作業終了時）

プロジェクトディレクトリへ移動

cd final ver

コンテナと関連リソースの削除

docker compose down --rmi all

補足

docker compose up -d を使用すると、バックグラウンドでコンテナを起動できます。

docker ps で実行中のコンテナを確認できます。

docker logs <コンテナID> でログを確認できます。
