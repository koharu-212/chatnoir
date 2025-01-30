## 起動方法
- このプロジェクトではDockerを使用しているので、`docker`コマンドを使います。

### 起動
```bash
docker compose up
```

### 更新ビルド
```bash
docker compose up --build -d
```

### コンテナ削除(作業終了したら...)
```bash
docker compose down --rmi all