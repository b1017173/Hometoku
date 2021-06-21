import mysql.connector

# コネクションの作成
conn = mysql.connector.connect(
    host='localhost',
    port='3306',
    user='hometoku',
    password='vPZrDNYjLfsV',
    database='hometoku'
)

# コネクションが切れた時に再接続してくれるよう設定
conn.ping(reconnect=True)

# 接続できているかどうか確認
print(conn.is_connected())

# DB操作用にカーソルを作成
cur = conn.cursor()

# id, name, priceを持つテーブルを（すでにあればいったん消してから）作成
cur.execute("DROP TABLE IF EXISTS `test_table`")
cur.execute("""CREATE TABLE IF NOT EXISTS `test_table` (
    `id` int(11) NOT NULL,
    `name` varchar(128) COLLATE utf8mb4_unicode_ci NOT NULL,
    `price` int(11) NOT NULL,
    PRIMARY KEY (id)
  ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci""")

cur.execute("INSERT INTO test_table VALUES (1, 'BTC', 10200)")


# プレースホルダを利用して挿入
cur.execute("INSERT INTO test_table VALUES (2, 'ETH', %s)", (5000, ))
cur.execute("INSERT INTO test_table VALUES (%s, %s, %s)", (3 ,'XEM', 2500))
cur.execute("INSERT INTO test_table VALUES (%(id)s, %(name)s, %(price)s)", {'id': 4, 'name': 'XRP', 'price': 1000})

# executemanyで複数データを一度に挿入
records = [
  (5, 'MONA', 3000),
  (6, 'XP', 1000),
]
cur.executemany("INSERT INTO test_table VALUES (%s, %s, %s)", records)
conn.commit()
cur.execute("SELECT * FROM test_table ORDER BY id ASC")

# 全てのデータを取得
rows = cur.fetchall()

for row in rows:
    print(row)

# 1件取得
cur.execute("SELECT * FROM test_table WHERE name=%s", ('BTC', ))
print(cur.rowcount)
print(cur.fetchone())


# DB操作が終わったらカーソルとコネクションを閉じる
cur.close()
conn.close()