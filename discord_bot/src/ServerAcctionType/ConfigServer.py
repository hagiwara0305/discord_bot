from src.ServerAcctionType.Sever import Server

class ConfigServer(Server):
    explanation = '\config\tEC2サーバの状態、起動している場合はIPアドレスを返却します'

    def __init__(self, instance_id=None) -> None:
        super().__init__(instance_id, self.explanation)

    async def action(self):
        instance = super().getInstance()

        status = instance.state
        print(f"状態コード：{status['Code']}")
        print(f"状態：{status['Name']}")

        if status['Code'] == 16:
            public_id = instance.public_ip_address
            print(f"IPアドレス: {public_id}")

            return {
                'status': True,
                'data': {
                    'message': f"サーバは起動中です\nIPアドレス: {public_id}"
                }
            }
        else:
            return {
                'status': True,
                'data': {
                    'message': f"サーバは停止中です\n起動してください（起動コマンド：\start)"
                }
            }
