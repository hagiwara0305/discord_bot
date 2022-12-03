import re
from src.ServerAcctionType.HelpServer import HelpServer
from src.ServerAcctionType.ConfigServer import ConfigServer
from src.ServerAcctionType.StartServer import StartServer
from src.ServerAcctionType.StopServer import StopServer
from src.ServerAcctionType.PriceServer import PriceServer

class ServerManager:
    def __init__(self, instance_id, client):
        self.instance_id = instance_id

        self.serverInterface = {
            '\start': StartServer(self.instance_id, client),
            '\stop': StopServer(self.instance_id, client),
            '\price': PriceServer(self.instance_id, client),
            '\config': ConfigServer(self.instance_id, client)
        }
        self.serverInterface['\list'] = HelpServer(serverInterface=self.serverInterface)


    async def getMessage(self, message):
        # コマンドを示す\で始まる場合
        if message.content[0] == '\\':
            if ' ' in message.content:
                # コマンドに値がある場合、それを除き検索
                match_index = message.content.find(' ')
                target_instance = self.serverInterface.get(message.content[0 : match_index])
            else:
                # 単一のコマンドの場合
                target_instance = self.serverInterface.get(message.content)

            if target_instance is None:
                return
        else:
            return

        return_message = await target_instance.action(message)

        if return_message['status']:
            return {
                'status': False,
                'data': return_message['data']
            }
        else:
            return {
                'status': True,
                'data': return_message['data']
            }

