from src.ServerAcctionType.HelpServer import HelpServer
from src.ServerAcctionType.ConfigServer import ConfigServer
from src.ServerAcctionType.StartServer import StartServer
from src.ServerAcctionType.StopServer import StopServer

class ServerManager:
    def __init__(self, instance_id):
        self.instance_id = instance_id

        self.serverInterface = {
            '\start': StartServer(self.instance_id),
            '\stop': StopServer(self.instance_id),
            '\config': ConfigServer(self.instance_id)
        }
        self.serverInterface['\list'] = HelpServer(serverInterface=self.serverInterface)


    async def getMessage(self, message):
        target_instance = self.serverInterface.get(message)

        if target_instance is None:
            return

        return_message = await target_instance.action()

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

