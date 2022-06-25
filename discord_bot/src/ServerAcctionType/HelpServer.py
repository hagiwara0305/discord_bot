from src.ServerAcctionType.Sever import Server

class HelpServer(Server):
    explanation = '\list\t\t各コマンドの説明を返却します'

    def __init__(self, serverInterface) -> None:
        super().__init__(explanation=self.explanation)

        self.helpExplanationStr = f""
        for item in serverInterface:
            self.helpExplanationStr += serverInterface[item].getExplanation() + '\n'
        self.helpExplanationStr += self.explanation

    async def action(self):
        return {
            'status': True,
            'data': {
                'message': self.helpExplanationStr
            }
        }

