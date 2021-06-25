import mysql.connector

# コネクションの作成
_conn = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='hometoku',
    password='vPZrDNYjLfsV',
    database='hometoku'
)

# コネクションが切れた時に再接続してくれるよう設定
_conn.ping(reconnect=True)

# 接続できているかどうか確認
print(_conn.is_connected())

# DB操作用にカーソルを作成
_cur = _conn.cursor(buffered=True)

def accessMysql(user_id, target_id_list, workspase_id, channel_id, claps):
    _user_id  = user_id
    _target_id_list = target_id_list
    _workspace_id = workspase_id
    _channel_id = channel_id
    _claps = claps

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

    # ユーザーの登録
    insertMysql(_user_id, _workspace_id, _channel_id)
    # 褒めピーポーの追加
    for _home_people in _target_id_list:
        _cur.execute("select exists (select * from users where workspace_id = %s and user_id = %s)",(_workspace_id, _home_people))
        if _cur.fetchone()[0] == 0 :
            insertMysql(_home_people, _workspace_id, _channel_id)
            print("褒めピーポーがDBにいなかったので、新しく追加したよ")

        _cur.execute("update users set price = price + 1 + %s where user_id = %s and workspace_id = %s",(_claps, _home_people, _workspace_id))
        _conn.commit()
        print("homeポイント追加")

    # DB操作が終わったらカーソルとコネクションを閉じる
    _cur.close()
    _conn.close()

def returnClapNum(workspace_id):
    # コネクションが切れた時に再接続してくれるよう設定
    _conn.ping(reconnect=True)

    # DB操作用にカーソルを作成
    _cur = _conn.cursor(buffered=True)

    _workspace_id = workspace_id
    _result = []

    # 内部結合したテーブルの中で引数のworkspace_idと一致するものを褒められた順で取得
    _cur.execute("select u.workspace_id, c.channel_id, u.user_id, u.price from users u join channels c on u.workspace_id = c.workspace_id where u.workspace_id = %s order by u.price desc;", (_workspace_id,))
    
    # 取得したデータをreslutに入れる
    _result = _cur.fetchall()
    print(_result)

    # DB操作が終わったらカーソルとコネクションを閉じる
    _cur.close()
    _conn.close()
    return _result


def insertMysql(user_id, workspase_id, channel_id):
    _user_id        = user_id
    _workspace_id   = workspase_id
    _channel_id     = channel_id

    try:
        #usersテーブルとbelongsテーブルの中でidが同じものを内部結合し、user_id, workspace_id, channel_idが全部一致するか確認する。
        _sql = "select exists(select * from users u INNER join channels c on u.workspace_id = c.workspace_id where u.workspace_id = %s and u.user_id = %s)"
        _cur.execute(_sql, (_workspace_id, _user_id))

        #一致するものがない場合は、それぞれのテーブルにデータを追加する。
        if(_cur.fetchone()[0] == 0):

            # userID, workspace_idがusersテーブルになければ追加#
            _cur.execute("select exists (select user_id, workspace_id from users where user_id = %s and workspace_id = %s)", (_user_id, _workspace_id))
            if _cur.fetchone()[0] == 0 :
                _cur.execute("INSERT INTO users (user_id, price, workspace_id) VALUES (%s, %s, %s)", (_user_id, 0, _workspace_id))
                _conn.commit()

            # channels_id,  workspace_idがchannelsテーブルになければ追加#
            _cur.execute("select exists (select * from channels where channel_id = %s and workspace_id = %s)",(_channel_id, _workspace_id))
            print(1)
            if _cur.fetchone()[0] == 0 :
                print(2)
                _cur.execute("INSERT INTO channels (workspace_id, channel_id) VALUES (%s, %s)", (_workspace_id, _channel_id))
                _conn.commit()

            print("データは挿入は成功したよ")

        else:
            print("データは存在するので追加しませんでした。")

    # except mysql.connector.errors.IntegrityError:
    except mysql.connector.errors.IntegrityError:
        print("挿入する情報が重複しています。")

# テスト用 #
accessMysql("eeoOSC",["ooncm"],"eomrrdp", "z", 0)
returnClapNum("smmdoidoodp")