import configparser
import discord

from src.ServerManager import ServerManager

config_ini = configparser.ConfigParser()
server = None

CONFIG_PAS = 'config.ini'

# 接続に必要なオブジェクトを生成
client = discord.Client(intents=discord.Intents.all())

# 起動時に動作する処理
@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')

# メッセージ受信時に動作する処理
@client.event
async def on_message(message):
    if message.author.bot:
        return

    print('get message: ')
    print(message.content)

    global server
    return_message = await server.getMessage(message)

    if return_message is None:
        return

    print('status: ')
    print(return_message['status'])

    print('send message: ')
    print(return_message['data']['message'])

    await message.channel.send(return_message['data']['message'])

def main():
    with open(CONFIG_PAS, encoding='utf-8') as fp:
        config_ini.read_file(fp)

        token = config_ini['DEFAULT'].get('discord_token')
        ec2_instance_id = config_ini['DEFAULT'].get('ec2_instance_id')

        # サーバマネージャインスタンス生成
        global server
        server = ServerManager(ec2_instance_id, client)

    # Botの起動とDiscordサーバーへの接続
    client.run(token)

if __name__ == '__main__':
    main()
