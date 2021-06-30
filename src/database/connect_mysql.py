import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host = "localhost",
            port = "3306",
        )
        
        self.open_db(True)

        # hometokuに編集権限を付与
        self.cur.execute("CREATE USER IF NOT EXISTS 'hometoku'@'localhost' IDENTIFIED BY 'vPZrDNYjLfsV'")
        self.cur.execute("GRANT all ON *.* TO 'hometoku'@'localhost'")

        # channelsテーブルの生成 ： usersのユーザーが所属しているチャンネルを紐づけて管理する #
        self.cur.execute("""CREATE TABLE IF NOT EXISTS `channels` (
                `workspace_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
                `channel_id` varchar(100) COLLATE utf8mb4_unicode_ci,
                PRIMARY KEY (workspace_id)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

        # usersテーブルの生成 ： ユーザーID、ほめられた回数、ワークスペースのIDを管理する #
        self.cur.execute("""CREATE TABLE IF NOT EXISTS `users` (
                `workspace_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
                `user_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
                `score` int(11) NOT NULL DEFAULT 0,
                PRIMARY KEY (workspace_id, user_id),
                FOREIGN KEY (workspace_id) REFERENCES channels(workspace_id)
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

        self.close_db()

    # DBへの書き込み
    def write_score(self, workspace_id:str, target_ids:list, claps:int):
        self.open_db()

        # 褒められピーポーの追加
        # → userID, workspace_idがusersテーブルになければ追加
        for target_id in target_ids:
            try :
                # 褒められた人がDBにいない時追加
                self.cur.execute("SELECT user_id, workspace_id FROM users WHERE user_id = '{0}' AND workspace_id = '{1}'".format(target_id, workspace_id))
                if len(self.cur.fetchall()) < 1:    # データが存在しないとき
                    self.cur.execute("INSERT INTO users (user_id, score, workspace_id) VALUES ('{0}', '{1}', '{2}')".format(target_id, 0, workspace_id))
                    self.conn.commit()
                    print("Insert new record into users table.\n('{0}', '{1}', '{2}')".format(target_id, 0, workspace_id))
                
                # 褒めスコアの追加
                _score = 8 + claps  # ベーススコア: 8
                self.cur.execute("UPDATE users SET score = score + '{0}' WHERE user_id = '{1}' AND workspace_id = '{2}'".format(_score, target_id, workspace_id))
                self.conn.commit()
                print("Update score.")

            # 挿入する情報が重複した場合のエラー処理:
            except mysql.connector.errors.IntegrityError as e:
                print("Error: Failed to reflect score.\n'{0}'".format(e))

        self.close_db()

    # DBの更新(スコアのリセット)
    def reset_score(self):
        self.open_db()
        
        self.cur.execute("UPDATE users SET score = '0'")
        self.conn.commit()
        print("Reset users score.")

        self.close_db()

    # DBへの読み込み
    def read_score(self, workspace_id:str, range:int):
        _result = []

        self.open_db()
        # 引数に与えられたidを持つユーザの取得
        self.cur.execute("SELECT * FROM users WHERE workspace_id = '{0}'".format(workspace_id))

        if 0 < len(self.cur.fetchall()):    # ユーザが存在するとき
            # 内部結合したテーブルの中で引数のworkspace_idと一致するものを褒められた順で取得
            # users: u, channels: c
            self.cur.execute("SELECT workspace_id, user_id, score FROM users WHERE workspace_id = '{0}' ORDER BY score DESC".format(workspace_id))
            _result = self.cur.fetchall()
            print("Selected score ranking.\n'{0}'".format(_result))
            _result = _result[:range]
            print("result: ", _result)

        self.close_db()

        return _result

    # チャンネルIDを登録する関数
    def set_channel_id(self, workspace_id, channel_id) :
        self.open_db()

        # ワークスペースIDが存在するか確認
        self.cur.execute("SELECT workspace_id FROM channels WHERE workspace_id = '{0}'".format(workspace_id))
        
        if 0 < len(self.cur.fetchall()):    # ワークスペースの登録があるとき
            # チャンネルIDの書き換え
            self.cur.execute("UPDATE channels SET channel_id = '{0}' WHERE workspace_id = '{1}'".format(channel_id, workspace_id))
            self.conn.commit()
            print("Update channel id: '{0}' from warkspase:'{1}'".format(channel_id, workspace_id))
        else :
            # 初回登録の際はワークスペースIDとチャンネルIDを登録する。
            self.cur.execute("INSERT INTO channels (workspace_id, channel_id) VALUES ('{0}', '{1}')".format(workspace_id, channel_id))
            self.conn.commit()
            print("Insert new record into channels table.\n('{0}', '{1}')".format(workspace_id, channel_id))

        self.close_db()
    
    # ワークスペースIDからチャンネルIDを返す
    def get_channel_id(self, workspace_id):
        _channel_id = ""
        self.open_db()
        self.cur.execute("SELECT channel_id FROM channels WHERE workspace_id = '{0}'".format(workspace_id))
        _response = self.cur.fetchone()
        if _response != None:
            _channel_id =  _response[0]
            print("Get channel id: '{0}' from workspace id: '{1}'.".format(_channel_id, workspace_id))

        self.close_db()
        return _channel_id

    # DBの操作を開始する
    def open_db(self, isInit = False):
        try:
            # コネクションが切れた時に再接続してくれるよう設定
            self.conn.ping(reconnect=True)

            # 接続できているかどうか確認
            if self.conn.is_connected():
                print("Success to connect")
            else:
                print("Failed to connect")

            # DB操作用にカーソルを生成
            self.cur = self.conn.cursor(buffered=True)

            if isInit:  # 最初の一回
                # hometokuデータベースの生成
                self.cur.execute("CREATE DATABASE IF NOT EXISTS `hometoku`")

            # hometokuデータベースを使用
            self.cur.execute("use `hometoku`")
        except Exception as e:
            print("Error: An error occurred while connecting to the database.\n'{0}'".format(e))

    # DB操作が終わったらカーソルとコネクションを閉じる
    def close_db(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception as e:
            print("Error: An error occurred while disconnecting to the database.\n'{0}'".format(e))


    def debug_db(self):
        _workspace_id ="WORKSPACEID"
        _channel_id = "CHANNELID"
        _channel_id_updated = "MEGACHANNELID"
        _user_ids = ["USER1", "USER2", "USER3"]
        _claps = [4, 1, 78]

        print("Debug: チャンネルの登録")
        self.set_channel_id(_workspace_id, _channel_id)

        print("Debug: チャンネルIDの取得")
        print("正誤: ", self.get_channel_id(_workspace_id) == _channel_id)
        print("Debug: スコアの書き込み")
        print("- 対象人数: 3人 -")
        print("-- 1回目/clap:4 ---")
        self.write_score(_workspace_id, _user_ids, _claps[0])
        print("-- 2回目/clap:78 ---")
        self.write_score(_workspace_id, _user_ids, _claps[2])
        print("- 対象人数: 1人 -")
        print("-- 1回目/clap:4 ---")
        self.write_score(_workspace_id, _user_ids[:1], _claps[0])
        print("-- 2回目/clap:1 ---")
        self.write_score(_workspace_id, _user_ids[:1], _claps[1])

        print("Debug: スコアの読み込み")
        self.read_score(_workspace_id, 2)

        print("Debug: スコアのリセット")
        self.reset_score()

        print("Debug: スコアの読み込み(リセット後)")
        self.read_score(_workspace_id, 3)

        print("Debug: 登録チャンネルの書き換え")
        self.set_channel_id(_workspace_id, _channel_id_updated)

        print("Debug: チャンネルIDの取得(チャンネル変更後)")
        print("正誤: ", self.get_channel_id(_workspace_id) == _channel_id_updated)

        self.open_db()
        self.cur.execute("DELETE FROM users")
        self.cur.execute("DELETE FROM channels")
        self.conn.commit()
        self.close_db()
