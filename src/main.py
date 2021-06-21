import os
# Use the package we installed
from slack_bolt import App
import app_server.shortcut as sc
import send

# Initializes your app with your bot token and signing secret

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

userid = ['user1','user2']
contents = "ガンバです"

# 'shortcut_homeru' という callback_id のショートカットをリッスン
@app.shortcut("shortcut_homeru")
def open_modal(ack, shortcut, client):
    print("shortcut")
    # リクエストを受け付け
    ack()
    sc.view_modal_from_shortcut(client, shortcut)

# 'homeru'モーダルを Submit したことをリッスン
@app.view("modal_homeru")
def handle_submission(ack, client):
    print("modal")
    ack()
    send.contents_to_slack(client, userid, contents)                        

# 'hello' を含むメッセージをリッスンします
# 指定可能なリスナーのメソッド引数の一覧は以下のモジュールドキュメントを参考にしてください：
# https://slack.dev/bolt-python/api-docs/slack_bolt/kwargs_injection/args.html
@app.message("hello")
def message_hello(message, say):
    # イベントがトリガーされたチャンネルへ say() でメッセージを送信します
    say(f"Hey <@{message['user']}>!")

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))