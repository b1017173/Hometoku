# ランキングデータを基にランキングメッセージの生成・送信
import datetime
import schedule
import time

def view_ranking_message(client, channel_id, ranking_list):
	_dt_now = datetime.datetime.now()
	_int_to_english = ["zero","one","two","three","four","five","six","seven","eight","nine"] # 添字の数字を英語に変える
	_view_blocks = [
		{
			"type": "image",
			"image_url": "https://cdn-ak.f.st-hatena.com/images/fotolife/s/sizimi0527/20210701/20210701201604.png",
			"alt_text": "home_award"
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "{0}月にたくさんホメられたあなたを表彰します！".format(_dt_now.month-1)
			}
		},
		{
			"type": "divider"
		}
	]

	# 感謝文作成
	_view_thanks = [
		{
			"type": "divider"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "ホメとくを使ってくれてありがとう！来月もガンガン褒めてくれよな:fire:"
			}
		}
		]

	for rank in range(len(ranking_list)):
		# viewに付け足されるランキング(最大1位2位3位の3回増やす)
		_clap_count = ":clap:" * (3 - rank)
		_score_simbol_list = list(str(ranking_list[rank][2]))#桁ごとに分離して配列に格納
		_score_simbol = ""
		for digit in _score_simbol_list:
			_score_simbol += ":{0}:".format(_int_to_english[int(digit)])
		_view_ranking =  {
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "{0}*{1}位 <@{2}>*{3}\nホメられた回数 {4} ホメ\n\n".format(_clap_count, rank+1, ranking_list[rank][1], _clap_count, _score_simbol)
				}
			}
		_view_blocks.append(_view_ranking)

	for map in _view_thanks :
		_view_blocks.append(map) # 最後に感謝文追加

	try:
		client.chat_postMessage(
			channel = channel_id,
			blocks = _view_blocks
		)
	except Exception as e:
		print("Error: sending ranking message is Failed, {0}".format(e))

def post_ranking(client, db, range):
	_team_info = client.team_info()
	_workspace_id = _team_info["team"]["id"]
	_channel_id = db.get_channel_id(_workspace_id)	# TODO: _channel_id = db.チャンネルIDの取得(_workspace_id)
	_ranking_list = db.read_score(_workspace_id,range)	# TODO: _ranking_list = db.ランキングリストの取得(_workspace_id, range = 3)

	# デバッグ用
	#_channel_id = "C026DHW2A2G"			# workspace_idとchannel_idのリスト
	#_ranking_list = [[_workspace_id, "U024LNTCHR8", "5"]] # ワークスペース毎の褒められランキングのリスト(1で抽出されたやつ)

	view_ranking_message(client, _channel_id, _ranking_list)

# 複数ワークスペースに送る場合の関数(未実装)
def all_ws_post_ranking(db):
	_workspaces = []	# TODO: _workspaces = db.ワークスペースリストの取得()

	for workspace in _workspaces:
		_client = ""
		post_ranking(_client, db)

# 毎月自動投稿する関数
def post_permonth_ranking(client, db, range):
	if datetime.datetime.now().day == 1:
		schedule.every(1).day.do(post_ranking, client, db, range) # scheduleに毎月1回実行が無かったのでif文で毎日実行を制限
		while True:
			schedule.run_pending()
			time.sleep(1)

	""" デバッグ用毎分投稿
	schedule.every(1).day.do(post_ranking, client, db, range) # scheduleに毎月1回実行が無かったのでif文で毎日実行を制限
	while True:
		schedule.run_pending()
		time.sleep(1)
		"""