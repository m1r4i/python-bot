import discord # インストールした discord.py

client = discord.Client() # 接続に使用するオブジェクト

# 起動時に通知してくれる処理
@client.event
async def on_ready():
    print('ログインしました')

# 「/neko」と発言したら「にゃーん」が返る処理
@client.event
async def on_message(message):
    if message.content.startswith('/neko'):
        reply = 'にゃーん'
        await client.send_message(message.channel, reply)
    elif message.content.startswith("!r first"):
        reply = "First.\nまずはPythonをインストールしましょう\n~~今回はpython 3.7.0~~\nDiscordBOTということでPython 3.6.6 ( https://www.python.org/ftp/python/3.6.6/python-3.6.6-webinstall.exe )\nを使います"
        await client.send_message(message.channel, reply)
    elif message.content.startswith("!r second"):
        reply = "コマンドプロンプトを起動して\n`pip install discord`\nと入力してください\nこれは何かといいますと今回DiscordBOTを作るうえで使うライブラリーを\nインストールしています\nライブラリーについては...詳しくは省きますね"
        await client.send_message(message.channel, reply)
    if client.user.id in message.content: # 話しかけられたかの判定
        reply = f'{message.author.mention} !r [文字 exp, first,second]で説明を表示\n/neko で今回作るBOTの見本を表示します ' # 返信文の作成
        await client.send_message(message.channel, reply) 
# botの接続と起動
# （tokenにはbotアカウントのアクセストークンを入れてください）
client.run('NDkxOTAxMDk5ODEzNjM0MDQ.DoOoQw.U_r2mRjQ2PHvhUB5nk_TD05c2Xk') # DUMMY LIKE REAL TOKEN
