from src.ServerAcctionType.Sever import Server

class StartServer(Server):
    explanation = '\start\t\tEC2サーバ起動します'

    def __init__(self, instance_id=None, client=None) -> None:
        super().__init__(instance_id, self.explanation, client)

    async def action(self, message):
        channel = message.channel
        await channel.send('サーバを起動しています...')

        instance = super().getInstance()

        print('EC2インスタンス起動開始')
        instance.start()

        instance.wait_until_running()
        print("インスタンス起動完了")

        ip = instance.public_ip_address
        print(f"IPアドレス: {ip}")

        return {
            'status': True,
            'data': {
                'message': f"サーバを起動しました\n IPアドレス: {ip}"
            }
        }
