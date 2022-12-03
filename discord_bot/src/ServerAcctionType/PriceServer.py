from src.ServerAcctionType.Sever import Server
import boto3
import re
import datetime
import calendar

class PriceServer(Server):
    explanation = '''\price < now | [yyyy-mm] > \利用請求額を出力します
        [now]: 先月の利用請求額を取得
        [yyyy-mm]: 指定した年月の利用請求額を取得'''

    def __init__(self, instance_id=None, client=None) -> None:
        super().__init__(instance_id, self.explanation, client)

    async def action(self, message):
        channel = message.channel
        await channel.send('利用請求額を取得しています...')

        # メッセージ内容の取得
        match_date = re.match(r'^\\price (now|[0-9]{4}-(0[1-9]|1[0-2]))', message.content)
        if match_date is None:
            return {
                'status': True,
                'data': {
                    'message': 'コマンドの実行形式が違います\n\n' + self.explanation
                }
            }
        else:
            # 先月
            if 'now' in message.content:
                date = datetime.date.today()
            else:
                print(match_date.group(1)[0 : 4])
                print(match_date.group(1)[5 : 7])
                date = datetime.date(
                    int(match_date.group(1)[0 : 4]),  # 年 yyyy
                    int(match_date.group(1)[5 : 7]),  # 月 mm
                    1                           # 日
                )
            
            print(self.get_first_date(date).strftime('%Y/%m/%d') + '\n' + self.get_last_date(date).strftime('%Y/%m/%d'))

        client = boto3.client('ce', region_name='ap-northeast-1')
        
        start_date_str = self.get_first_date(date).strftime('%Y-%m-%d')
        end_date_str = self.get_last_date(date).strftime('%Y-%m-%d')
        try:
            response = client.get_cost_and_usage(
                TimePeriod={
                    'Start': start_date_str,
                    'End': end_date_str
                },
                Granularity='MONTHLY',
                Metrics=[
                    'AmortizedCost'
                ],
            )
            print(response)
        except Exception as e:
            return {
            'status': True,
            'data': {
                'message': f'AWSのデータ取得でエラーが発生しました\ntype: '
                + str(type(e))
                + '\nmessage: ' + str(e.args)
            }
        }


        return {
            'status': True,
            'data': {
                'message': f'{start_date_str} ~ {end_date_str} までの利用請求額\n'+
                f'''{response['ResultsByTime'][0]['Total']['AmortizedCost']['Unit']}: {response['ResultsByTime'][0]['Total']['AmortizedCost']['Amount']}'''
            }
        }

    def get_first_date(self, dt):
        return dt.replace(day=1)

    def get_last_date(self, dt):
        return dt.replace(day=calendar.monthrange(dt.year, dt.month)[1])