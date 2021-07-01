import os
import datetime
import database.connect_mysql as cm
import datetime
import threading


# Use the package we installed
from slack_bolt import App
from slack_sdk.web import client
import app_server.shortcut as sc
import app_server.update_channel as uc
import app_server.home as hm
import app_server.send as sd
import app_server.monthly_ranking as mr

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# データベースのインスタンス生成
db = cm.Database()
# デバッグ用
#db.debug_db()

# アプリのDMを開いた時にヘルプを表示
@app.event("app_home_opened")
def send_help(client, event, logger):
    _user_id = event["user"]
    _workspace_id = event["view"]["team_id"]
    _channel_id = db.get_channel_id(_workspace_id)
    hm.view_help_message(client, _user_id, _channel_id, logger)

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
    
    _workspace_id = body["team"]["id"]
    _channel_id = view["state"]["values"]["selecter"]["select_channel"]["selected_conversation"]
    _user_id = body["user"]["id"]
    if _channel_id == None: # 未入力で送信された場合は，何も処理しない
        return
    print("workspace id: ", _workspace_id)
    print("  channel id: ", _channel_id)
    print("     user id: ", _user_id)

    _joined_channel_id = db.get_channel_id(_workspace_id)
    if _joined_channel_id == "":
        uc.setup_channel(say, _workspace_id, _channel_id, client, db)
    else:
        uc.update_channel(say, _workspace_id, _channel_id, _joined_channel_id, client, db)
    hm.view_help_message(client, _user_id, _channel_id, logger)

# チャンネル登録のコマンドのリスナー
@app.command("/hometoku_set_channel")
def get_channel_command(ack, say, command, client):
    ack()
    # ワークスペースIDが欲しい
    _workspace_id = command["team_id"]
    _channel_id = command["channel_id"] # コマンドが呼ばれたチャンネルID用の変数
    _user_id = command["user_id"] # コマンドを呼び出した人のユーザーID用の変数

    _joined_channel_id = db.get_channel_id(_workspace_id)

    if _joined_channel_id == "":
        uc.setup_channel(say, _workspace_id, _channel_id, client, db)
    else:
        uc.cant_setup_channel(_joined_channel_id, _user_id, client)

# チャンネル更新のコマンドリスナー
@app.command("/hometoku_update_channel")
def get_update_channel_command(ack, say, command, client):
    ack()
    _workspace_id = command["team_id"]
    _channel_id = command["channel_id"] # コマンドがよばれたチャンネルID用の変数
    _user_id = command["user_id"] # コマンドを呼び出した人のユーザーID用の変数

    _joined_channel_id = db.get_channel_id(_workspace_id)

    if _joined_channel_id != _channel_id:  # 既に参加しているチャンネルIDとコマンドがよばれたチャンネルIDが不一致なら更新する
        uc.update_channel(say, _workspace_id, _channel_id, _joined_channel_id, client, db)
    else:  # すでに参加しているチャンネルでコマンドがよばれた場合
        uc.cant_setup_channel(_joined_channel_id, _user_id, client)

# 'shortcut_homeru' という callback_id のショートカットをリッスン
@app.shortcut("shortcut_homeru")
def open_modal_homeru(ack, shortcut, client):
    ack()

    # チャンネルの登録の有無に合わせたモーダル表示
    _workspace_id = shortcut["team"]["id"]
    _channel_id = db.get_channel_id(_workspace_id)
    if _channel_id != "":
        sc.view_modal_from_shortcut(client, shortcut)
    else:
        sc.view_modal_not_set_channel(client, shortcut)

# 'prise_countup' アクションをリッスン(褒めたい度の更新)
@app.action("prise_countup")
def countup_prise(ack, body, client):
    # リクエストを受け付け
    ack()
    sc.update_modal_from_countup(body, client)

# デバッグ用
@app.message("debug_post_ranking")
def debug_post_ranking():
    _client = app.client
    mr.post_ranking(_client, db, 3)



# 'homeru'モーダルを Submit したことをリッスン
@app.view("modal_homeru")
def handle_homeru_submission(ack, say, body, view, logger):
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
    db.write_score(_workspace_id,_targets,_clap_num)
    sd.view_praise_message(say, _workspace_id, _targets, _prise_writing, _clap_num, db, logger) # modalに入力された内容をSlackで表示させる

# Start your app
if __name__ == "__main__":
    auto_post_ranking = threading.Thread(target=mr.post_permonth_ranking, args=(app.client, db, 3))
    auto_post_ranking.start()
    app.start(port=int(os.environ.get("PORT", 3000)))

