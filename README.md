# 動作方法
1. docker-composeをインストール
2. docker-compose.yamlファイルにAWSのAIM設定を追加
```
    environment:
      - AWS_ACCESS_KEY_ID=EC2にアクセス権限があるAIMユーザのアクセスキー
      - AWS_SECRET_ACCESS_KEY=シークレットキー
      - AWS_DEFAULT_REGION=EC2の対象リージョン
```
3. config.iniファイルに起動を自動化するEC2のインスタンスIDを追加
```
[DEFAULT]
discord_token=Discordのbotトークン
ec2_instance_id=起動する対象のEC2インスタンスID
```
4. 起動コマンド
```
# cd クローンしたbotのディレクトリ
# docker-compose up -d --build
```