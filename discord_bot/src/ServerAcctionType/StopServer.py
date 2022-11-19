from src.ServerAcctionType.Sever import Server

class StopServer(Server):
    explanation = '\stop\t\tEC2サーバを停止します'

    def __init__(self, instance_id=None, client=None) -> None:
        super().__init__(instance_id, self.explanation, client)

    async def action(self, message):
        channel = message.channel
        await channel.send('サーバを停止しています...')

        instance = super().getInstance()

        print('EC2インスタンス停止処理開始')
        instance.stop()

        instance.wait_until_stopped()
        print("インスタンス停止完了")

        return {
            'status': True,
            'data': {
                'message': f"サーバを停止しました"
            }
        }
