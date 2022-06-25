from src.ServerAcctionType.Sever import Server

class StopServer(Server):
    explanation = '\stop\t\tEC2サーバを停止します'

    def __init__(self, instance_id=None) -> None:
        super().__init__(instance_id, self.explanation)

    async def action(self):
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
