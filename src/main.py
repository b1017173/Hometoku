import os
# Use the package we installed
from slack_bolt import App

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# Add functionality here
# @app.event("app_home_opened") etc

# 'homeru'モーダルを Submit したことをリッスン
@app.view("modal_homeru")
def handle_submission(ack, body, client, view, logger):
    ack()
    _user = body["user"]["id"]                                                              # 投稿ユーザ
    _targets = view["state"]["values"]["homepeople"]["select_homepeople"]["selected_users"] # 褒めたい人・チャンネル
    _prise_writing = view["state"]["values"]["homemove"]["input_homemove"]["value"]         # 褒めたいこと
    print("user: ", _user)
    print("targets: ", _targets)
    print("prise writing: ", _prise_writing)
    # _prise_quantity = view["state"]["values"]["blockID"]["actionID"]
    
    # メッセージ送信の関数
    # xx.yyyyy(client, logger, _user, _targets, _prise_writing)
    # xx.yyyyy(client, logger, _user, _targets, _prise_writing, _prise_quantity)

    # DBへの書き込み 
    # xx.yyyy(_targets, _prise_quantity)

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))