import mysql.connector

class AccessDB:

    def __init__(self):                  # コンストラクタ
        self.conn = mysql.connector.connect(
            host = 'localhost',
            port = '3306'
        )

        # コネクションが切れた時に再接続してくれるよう設定
        self.conn.ping(reconnect=True)

        # 接続できているかどうか確認
        print(self.conn.is_connected())

        # DB操作用にカーソルを作成
        self.cur = self.conn.cursor(buffered=True)

        # hometokuデータベースの作成
        self.cur.execute('CREATE DATABASE IF NOT EXISTS `hometoku`')
        # hometokuデータベースの使用
        self.cur.execute('use `hometoku`')

        # hometokuに編集権限をふよ
        self.cur.execute("CREATE USER IF NOT EXISTS 'hometoku'@'localhost' IDENTIFIED BY 'vPZrDNYjLfsV'")
        self.cur.execute("GRANT all ON *.* TO 'hometoku'@'localhost'")

        # channelsテーブルの作成 ： usersのユーザーが所属しているチャンネルを紐づけて管理する #
        self.cur.execute("""CREATE TABLE IF NOT EXISTS `channels` (
            `workspace_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
            `channel_id` varchar(100) COLLATE utf8mb4_unicode_ci,
            PRIMARY KEY (workspace_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

        # usersテーブルの作成 ： ユーザーID、ほめられた回数、ワークスペースのIDを管理する #
        self.cur.execute("""CREATE TABLE IF NOT EXISTS `users` (
            `workspace_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
            `user_id` varchar(100) COLLATE utf8mb4_unicode_ci NOT NULL,
            `price` int(11) NOT NULL DEFAULT 0,
            PRIMARY KEY (workspace_id, user_id),
            FOREIGN KEY (workspace_id) REFERENCES channels(workspace_id)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

        # DB操作が終わったらカーソルとコネクションを閉じる
        self.cur.close()
        self.conn.close()


    # 褒められた回数と褒められた人を登録する関数 #
    def set_clap_num(self, target_id_list, workspase_id, claps):
        self.target_id_list = target_id_list # 褒められた人の変数
        self.workspace_id   = workspase_id   # ワークスペースIDの変数
        self.claps          = claps          # クラップの回数

        # コネクションが切れた時に再接続してくれるよう設定
        self.conn.ping(reconnect=True)
        # DB操作用にカーソルを作成
        self.cur = self.conn.cursor(buffered=True)
        # hometokuデータベースを使用
        self.cur.execute('use `hometoku`')

        # 褒めピーポーの追加 #

        for home_people in self.target_id_list:
            try :
                # userID, workspace_idがusersテーブルになければ追加#
                print(1)

                #褒められた人がDBにいない時追加
                self.cur.execute('select exists (select user_id, workspace_id from users where user_id = %s and workspace_id = %s)', (home_people, self.workspace_id))
                if self.cur.fetchone()[0] == 0 : # 1:データが存在するとき, 0:データが存在しないとき
                    print(2)
                    self.cur.execute('INSERT INTO users (user_id, price, workspace_id) VALUES (%s, %s, %s)', (home_people, 0, self.workspace_id))
                    self.conn.commit()

                print("褒めピーポーがDBにいなかったので、新しく追加したよ")
                
                self.cur.execute('update users set price = price + 1 + %s where user_id = %s and workspace_id = %s', (self.claps, home_people, self.workspace_id))
                self.conn.commit()
                print("homeポイント追加したよ")

            # 挿入する情報が重複した場合のエラー処理:
            except mysql.connector.errors.IntegrityError as e:
                print(e)

        # DB操作が終わったらカーソルとコネクションを閉じる
        self.cur.close()
        self.conn.close()

    # 褒められた回数を返す関数 #
    def get_clap_num(self, workspace_id):
        self.workspace_id = workspace_id
        _result = []

        # コネクションが切れた時に再接続してくれるよう設定
        self.conn.ping(reconnect=True)
        # DB操作用にカーソルを作成
        self.cur = self.conn.cursor(buffered=True)
        # hometokuデータベースを使用
        self.cur.execute('use `hometoku`')

        # ワークスペースIDが存在するか確認
        self.cur.execute('select exists (select * from users where workspace_id = %s)', (self.workspace_id,))

        if self.cur.fetchone()[0] == 1 : # 1:データが存在するとき, 0:データが存在しないとき
            # 内部結合したテーブルの中で引数のworkspace_idと一致するものを褒められた順で取得
            self.cur.execute('select u.workspace_id, c.channel_id, u.user_id, u.price from users u join channels c on u.workspace_id = c.workspace_id where u.workspace_id = %s order by u.price desc limit 3', (self.workspace_id,))
            print("褒められ度を降順で取得したよ!")
        else:
            print("ワークスペースIDがないから、褒められた度を取得できなかったよ(泣)")

        # 取得したデータをreslutに入れる
        _result = self.cur.fetchall()
        
        print("get_clap_numが完了したよ")

        # DB操作が終わったらカーソルとコネクションを閉じる
        self.cur.close()
        self.conn.close()

        return _result

    # チャンネルIDを削除する関数
    def delete_channel_id(self, workspace_id, channel_id) :
        self.workspace_id = workspace_id
        self.channel_id = channel_id

        # コネクションが切れた時に再接続してくれるよう設定
        self.conn.ping(reconnect=True)
        # DB操作用にカーソルを作成
        self.cur = self.conn.cursor(buffered=True)
        # hometokuデータベースを使用
        self.cur.execute('use `hometoku`')

        # ワークスペースIDとチャンネルIDが存在するか確認
        self.cur.execute('select exists (select * from channels where workspace_id = %s and channel_id = %s)', (self.workspace_id, self.channel_id))
        
        if self.cur.fetchone()[0] == 1 : # 1:データが存在するとき, 0:データが存在しないとき
            # channelsテーブルの中で、チャンネルIDをNULLに変更 #
            self.cur.execute('update channels set channel_id = NULL where channel_id = %s', (self.channel_id, ))
            # 変更をDB側にコミットする
            self.conn.commit()
            print("チャンネルIDを削除したよ。")
        else :
            print("変更するIDが見つかりませんでした。")

        # DB操作が終わったらカーソルとコネクションを閉じる
        self.cur.close()
        self.conn.close()


    # チャンネルIDを登録する関数
    def set_channel_id(self, workspace_id, channel_id) :
        self.workspace_id = workspace_id
        self.channel_id = channel_id

        # コネクションが切れた時に再接続してくれるよう設定
        self.conn.ping(reconnect=True)
        # DB操作用にカーソルを作成
        self.cur = self.conn.cursor(buffered=True)
        # hometokuデータベースを使用
        self.cur.execute('use `hometoku`')

        # ワークスペースIDが存在するか確認
        self.cur.execute('select exists (select workspace_id from channels where workspace_id = %s)', (self.workspace_id,))
        
        if self.cur.fetchone()[0] == 1 : # 1:データが存在するとき, 0:データが存在しないとき
            #ワークスペースIDがあるけど、チャンネルIDがない時、NULLのものを置き換える
            self.cur.execute('update channels set channel_id = %s where channel_id is NULL', (self.channel_id,))
            # 変更をDB側にコミットする
            self.conn.commit()
            print("チャンネルIDを設定したよ。")
        else :
            # 初回登録の際はワークスペースIDとチャンネルIDを登録する。
            # channelsテーブルの中で、ワークスペースIDと変える前のチャンネルID(prev_channel_id)が等しい行を変えた後のチャンネルID(next_channel_id)に変更する #
            self.cur.execute('insert into channels (workspace_id, channel_id) values (%s, %s)', (self.workspace_id, self.channel_id))
            # 変更をDB側にコミットする
            self.conn.commit()
            print("ワークスペースIDとチャンネルIDを新たに追加したよ。")

        # DB操作が終わったらカーソルとコネクションを閉じる
        self.cur.close()
        self.conn.close()



# テスト用 #
test_class = AccessDB()

test_class.set_channel_id("test","NM")

#引数：褒められた人(基本リスト)、ワークスペースID、チャンネルID、褒められ度
#返り値：なし
test_class.set_clap_num(["o","docmcm","onnnvn","q88"],"test", 5)

#引数：褒められた人()、ワークスペースID
#返り値：指定したワークスペースIDに所属する人の情報(ワークスペースID、チャンネルID、ユーザーID, 褒められ度)を返す。変える順番は、褒められた度をが大きい順
a = test_class.get_clap_num("test")
print(a)

#引数：ワークスペースID、チャンネルID
#返り値：なし
test_class.delete_channel_id("test", "NM")

test_class.set_channel_id("test","uotp")
