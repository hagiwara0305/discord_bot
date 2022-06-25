import boto3

class Server:
    # 各コマンドの説明文
    # クラスを実装する側に設定を行う
    explanation = None

    # 対象となるインスタンスID
    instance_id = None
    # EC2リソース
    ec2 = boto3.resource('ec2')
    # ec2インスタンスオブジェクト
    instance = None

    def __init__(self, instance_id=None, explanation=None) -> None:
        if instance_id is not None:
            # ターゲットとなるEC2インスタンスID
            self.instance_id = instance_id

            # ec2インスタンス起動
            self.setInstance(self.instance_id)

        self.explanation = explanation

    # インスタンスオブジェクトを生成
    def setInstance(self, instance_id):
        # 初回のインスタンス生成時のみ
        if instance_id is not None:
            self.instance = self.ec2.Instance(instance_id)

    def getInstance(self):
        return self.instance

    def getInstanceId(self):
        return self.instance_id

    def setExplantion(self, explantion):
        self.explanation = explantion

    def getExplanation(self):
        return self.explanation