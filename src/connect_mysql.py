import mysql.connector
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime

# コネクションの作成
_conn = mysql.connector.connect(
    host='localhost',
    port='3306'
)

# コネクションが切れた時に再接続してくれるよう設定
_conn.ping(reconnect=True)

# 接続できているかどうか確認
print(_conn.is_connected())

# DB操作用にカーソルを作成
_cur = _conn.cursor(buffered=True)

# hometokuデータベースの作成
_cur.execute("CREATE DATABASE IF NOT EXISTS `hometoku`")
# hometokuデータベースの使用
_cur.execute("use `hometoku`")

 # hometokuに編集権限をふよ
_cur.execute("CREATE USER IF NOT EXISTS 'hometoku'@'localhost' IDENTIFIED BY 'vPZrDNYjLfsV'")
_cur.execute("GRANT all ON *.* TO 'hometoku'@'localhost'")

# usersテーブルの作成 ： ユーザーID、ほめられた回数、ワークスペースのIDを管理する #
_cur.execute("""CREATE TABLE IF NOT EXISTS `users` (
    `workspace_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
    `user_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
    `price` int(11) NOT NULL DEFAULT 0,
    PRIMARY KEY (workspace_id, user_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

# channelsテーブルの作成 ： usersのユーザーが所属しているチャンネルを紐づけて管理する #
_cur.execute("""CREATE TABLE IF NOT EXISTS `channels` (
    `workspace_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
    `channel_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
    PRIMARY KEY (workspace_id, channel_id),
    FOREIGN KEY (workspace_id) REFERENCES users(workspace_id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

# 褒められた回数と褒められた人を登録する関数 #
def setClapNum(target_id_list, workspase_id, channel_id, claps):
    _target_id_list = target_id_list # 褒められた人の変数
    _workspace_id   = workspase_id   # ワークスペースIDの変数
    _channel_id     = channel_id     # チャンネルIDの変数
    _claps          = claps          # クラップの回数

    # コネクションが切れた時に再接続してくれるよう設定
    _conn.ping(reconnect=True)
    # DB操作用にカーソルを作成
    _cur = _conn.cursor(buffered=True)
    # hometokuデータベースを使用
    _cur.execute("use `hometoku`")

    # 褒めピーポーの追加 #

    for _home_people in _target_id_list:
        # 褒めピーポーがDBに居るかいないかをチェックする
        _cur.execute("select exists (select * from users where workspace_id = %s and user_id = %s)",(_workspace_id, _home_people))
        if _cur.fetchone()[0] == 0 : # 1:データが存在するとき, 0:データが存在しないとき
            insertUserInfo(_home_people, _workspace_id, _channel_id) #褒められた人がDBにいない時追加
            print("褒めピーポーがDBにいなかったので、新しく追加したよ")

        _cur.execute("update users set price = price + 1 + %s where user_id = %s and workspace_id = %s",(_claps, _home_people, _workspace_id))
        _conn.commit()
        print("homeポイント追加したよ")

    # DB操作が終わったらカーソルとコネクションを閉じる
    _cur.close()
    _conn.close()

 # 褒められた回数を返す関数 #
def getClapNum(workspace_id):
    _workspace_id = workspace_id
    _result = []

    # コネクションが切れた時に再接続してくれるよう設定
    _conn.ping(reconnect=True)
    # DB操作用にカーソルを作成
    _cur = _conn.cursor(buffered=True)
    # hometokuデータベースを使用
    _cur.execute("use `hometoku`")

    # ワークスペースIDが存在するか確認
    _cur.execute("select exists (select * from users where workspace_id = %s)", (_workspace_id,))

    if _cur.fetchone()[0] == 1 : # 1:データが存在するとき, 0:データが存在しないとき
         # 内部結合したテーブルの中で引数のworkspace_idと一致するものを褒められた順で取得
        _cur.execute("select u.workspace_id, c.channel_id, u.user_id, u.price from users u join channels c on u.workspace_id = c.workspace_id where u.workspace_id = %s order by u.price desc;", (_workspace_id,))
        print("褒められ度を降順で取得したよ!")
    else:
        print("ワークスペースIDがないから、褒められた度を取得できなかったよ(泣)")

    # 取得したデータをreslutに入れる
    _result = _cur.fetchall()
    print(_result)

    # DB操作が終わったらカーソルとコネクションを閉じる
    _cur.close()
    _conn.close()

    return _result

# チャンネルIDを更新する関数
def updateChannelID(workspace_id, prev_channel_id, next_channel_id) :
    _workspace_id = workspace_id
    _prev_channel_id = prev_channel_id #変える前のチャンネルID
    _next_channel_id = next_channel_id #変えた後のチャンネルID

    # コネクションが切れた時に再接続してくれるよう設定
    _conn.ping(reconnect=True)
    # DB操作用にカーソルを作成
    _cur = _conn.cursor(buffered=True)
    # hometokuデータベースを使用
    _cur.execute("use `hometoku`")

    # ワークスペースIDとチャンネルIDが存在するか確認
    _cur.execute("select exists (select * from channels where workspace_id = %s and channel_id = %s)", (_workspace_id, _prev_channel_id))
    
    if _cur.fetchone()[0] == 1 : # 1:データが存在するとき, 0:データが存在しないとき
         # channelsテーブルの中で、ワークスペースIDと変える前のチャンネルID(prev_channel_id)が等しい行を変えた後のチャンネルID(next_channel_id)に変更する #
        _cur.execute("update channels set channel_id = %s where workspace_id = %s and channel_id = %s", (_next_channel_id, _workspace_id, _prev_channel_id))
        # 変更をDB側にコミットする
        _conn.commit()
        print("チャンネルIDを変更したよ。")
    else :
        print("変更するIDが見つかりませんでした。")

    # DB操作が終わったらカーソルとコネクションを閉じる
    _cur.close()
    _conn.close()

# ユーザー情報を登録する関数 #
def insertUserInfo(user_id, workspase_id, channel_id):
    _user_id        = user_id
    _workspace_id   = workspase_id
    _channel_id     = channel_id

    try:
        #usersテーブルとbelongsテーブルの中でidが同じものを内部結合し、user_id, workspace_id, channel_idが全部一致するか確認する。
        _sql = "select exists(select * from users u INNER join channels c on u.workspace_id = c.workspace_id where u.workspace_id = %s and u.user_id = %s)"
        _cur.execute(_sql, (_workspace_id, _user_id))

        #一致するものがない場合は、それぞれのテーブルにデータを追加する。
        if(_cur.fetchone()[0] == 0): # 1:データが存在するとき, 0:データが存在しないとき

            # userID, workspace_idがusersテーブルになければ追加#
            _cur.execute("select exists (select user_id, workspace_id from users where user_id = %s and workspace_id = %s)", (_user_id, _workspace_id))
            if _cur.fetchone()[0] == 0 : # 1:データが存在するとき, 0:データが存在しないとき
                _cur.execute("INSERT INTO users (user_id, price, workspace_id) VALUES (%s, %s, %s)", (_user_id, 0, _workspace_id))
                _conn.commit()

            # channels_id,  workspace_idがchannelsテーブルになければ追加#
            _cur.execute("select exists (select * from channels where channel_id = %s and workspace_id = %s)",(_channel_id, _workspace_id))
            print(1)
            if _cur.fetchone()[0] == 0 : # 1:データが存在するとき, 0:データが存在しないとき
                print(2)
                _cur.execute("INSERT INTO channels (workspace_id, channel_id) VALUES (%s, %s)", (_workspace_id, _channel_id))
                _conn.commit()

            print("データは挿入は成功したよ")

        else:
            print("データは存在するので追加しませんでした。")

    # 挿入する情報が重複した場合のエラー処理:
    except mysql.connector.errors.IntegrityError:
        print("挿入する情報が重複しています。")

def resetClapNum():
    _now = datetime.datetime.now()

    # コネクションが切れた時に再接続してくれるよう設定
    _conn.ping(reconnect=True)

    # DB操作用にカーソルを作成
    _cur = _conn.cursor(buffered=True)

    _cur.execute("use `hometoku`")

    #_cur.execute("update users set price = 0 where price > 0")
    #_conn.commit()
    #_cur.execute("select user_id, price from users")
    #_result = _cur.fetchall()
    #print(_result)

    _cur.execute("update users set price = 0 where price > 0")
    _cur.execute("select user_id, price from users")
    _result = _cur.fetchall()
    print(_result)
    
    _cur.close()
    _conn.close()



# テスト用 #
#引数：褒められた人(基本リスト)、ワークスペースID、チャンネルID、褒められ度
#返り値：なし
setClapNum(["ooncm"],"eomrrdp", "z", 0)

#引数：褒められた人()、ワークスペースID
#返り値：指定したワークスペースIDに所属する人の情報(ワークスペースID、チャンネルID、ユーザーID, 褒められ度)を返す。変える順番は、褒められた度をが大きい順
getClapNum("smmdoidoodp")

#引数：ワークスペースID、変更前のチャンネルID、変更後のチャンネルID
#返り値：なし
updateChannelID("eomrrdp","z","aiueo")
