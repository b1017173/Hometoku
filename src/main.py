import os
import datetime

from mysql.connector import connect


# Use the package we installed
from slack_bolt import App
import app_server.shortcut as sc
import app_server.update_channel as uc
import app_server.home as hm

from connect_mysql import setClapNum, getClapNum, updateChannelID

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# アプリのDMを開いた時にヘルプを表示
@app.event("app_home_opened")
def send_help(client, event, logger):
    _user_id = event["user"]
    hm.view_help_message(client, _user_id, logger)

# ホームタブのチャンネル更新ボタンが押された時にモーダル表示
@app.action("update_channel")
def open_modal_update_channel(ack, body, client):
    ack()
    hm.view_modal_from_help(body, client)

# チャンネルセレクトで何かが選ばれた時に呼ばれる．今は処理なんも必要ないのでダミー関数実装
@app.action("select_channel")
def dummy(ack):
    ack()

# チャンネル登録のモーダルのリスナー
@app.view("modal_update_channel")
def handle_update_channel_submission(ack, say, body, client, view, logger):
    ack()
    # 入力されたチャンネルIDの取得
    _channel_id = view["state"]["values"]["selecter"]["select_channel"]["selected_conversation"]
    _user_id = body["user"]["id"]
    if _channel_id == None:
        return
    print("channel id: ", _channel_id)
    print("user id: ", _user_id)

    _db = None
    _joined_channel_id = "" # TODO: dbにアクセスしてチャンネル情報がすでにあるかを確認する
    if _joined_channel_id == "":
        uc.setup_channel(say, _channel_id, client, _db)
    else:
        uc.update_channel(say, _channel_id, _joined_channel_id, client, _db)
    hm.view_help_message(client, _user_id, logger)

# チャンネル登録のコマンドのリスナー
@app.command("/hometoku_set_channel")
def get_channel_command(ack, say, command, client):
    ack()
    _channel_id = command["channel_id"] # コマンドが呼ばれたチャンネルID用の変数
    _user_id = command["user_id"] # コマンドを呼び出した人のユーザーID用の変数

    _db = None
    _joined_channel_id = "" # TODO: dbにアクセスしてチャンネル情報がすでにあるかを確認する
    if _joined_channel_id == "":
        uc.setup_channel(say, _channel_id, client, _db)
    else:
        uc.cant_setup_channel(say, _channel_id, _joined_channel_id, _user_id, client)

# 'shortcut_homeru' という callback_id のショートカットをリッスン
@app.shortcut("shortcut_homeru")
def open_modal_homeru(ack, shortcut, client):
    # リクエストを受け付け
    ack()
    sc.view_modal_from_shortcut(client, shortcut)

# 'prise_countup' アクションをリッスン(褒めたい度の更新)
@app.action("prise_countup")
def countup_prise(ack, body, client):
    # リクエストを受け付け
    ack()
    sc.update_modal_from_countup(body, client)

# 'homeru'モーダルを Submit したことをリッスン
@app.view("modal_homeru")
def handle_homeru_submission(ack, body, client, view, logger):
    # リクエストを受け付け
    ack()
    _user = body["user"]["id"]                                                              # 投稿ユーザ
    _targets = view["state"]["values"]["homepeople"]["select_homepeople"]["selected_users"] # 褒めたい人・チャンネル
    _prise_writing = view["state"]["values"]["homemove"]["input_homemove"]["value"]         # 褒めたいこと
    
    _workspace_id = body["team"]["id"]
    _clap_num = view["blocks"][4]["elements"][0]["text"].count("clap")
    _timestamp = datetime.datetime.now()
    print("user: ", _user)
    print("targets: ", _targets)
    print("prise writing: ", _prise_writing)
    print("workspace id: ", _workspace_id)
    print("clap num: ", _clap_num)
    print("timestamp: ", _timestamp)
    # _prise_quantity = view["state"]["values"]["blockID"]["actionID"]
    
    # メッセージ送信の関数
    # xx.yyyyy(client, logger, _user, _targets, _prise_writing)
    # xx.yyyyy(client, logger, _user, _targets, _prise_writing, _prise_quantity)

    # DBへの書き込み
    _test_user = "DOGPG"
    _test_targets = ["DODDPPD","AAPOO"]
    _test_workspace_id = "KAKAK"
    _test_channel_id = "GFFFP"
    _test_clap_num = 5
    setClapNum(_targets, _test_workspace_id, _test_channel_id, _test_clap_num)
    _result = getClapNum("smmdoidoodp")
    [print(i) for i in _result]
    updateChannelID(_test_workspace_id, _test_channel_id, "next_channel_id")
    # xx.yyyy(_targets, _prise_quantity)

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))