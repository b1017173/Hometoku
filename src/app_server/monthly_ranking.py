# ランキングデータを基にランキングメッセージの生成・送信
import datetime
from os import register_at_fork
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
		_score_symbol_list = list(str(ranking_list[rank][2]))#桁ごとに分離して配列に格納
		_score_symbol = ""
		for digit in _score_symbol_list:
			_score_symbol += ":{0}:".format(_int_to_english[int(digit)])
		_view_ranking =  {
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "{0}*{1}位 <@{2}>*{3}\nホメられた回数 {4} ホメ\n\n".format(_clap_count, rank+1, ranking_list[rank][1], _clap_count, _score_symbol)
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
	_channel_id = ""

	_team_info = client.team_info()
	_workspace_id = _team_info["team"]["id"]
	_channel_id = db.get_channel_id(_workspace_id)	# TODO: _channel_id = db.チャンネルIDの取得(_workspace_id)
	_ranking_list = db.read_score(_workspace_id,range)	# TODO: _ranking_list = db.ランキングリストの取得(_workspace_id, range = 3)

	if(_channel_id != ""):
		view_ranking_message(client, _channel_id, _ranking_list)
		db.reset_score()
	else:
		print("channel is not setting")


# 複数ワークスペースに送る場合の関数(未実装)
def all_ws_post_ranking(db):
	_workspaces = []	# TODO: _workspaces = db.ワークスペースリストの取得()

	for workspace in _workspaces:
		_client = ""
		post_ranking(_client, db)

# 毎月自動投稿する関数
def post_permonth_ranking(client, db, range):
	_date = datetime.datetime.now()				# 今の時間を格納
	_expected_date = datetime.datetime.now()	# 来月の予定日を格納
	while True:
		# 来月のついたちの時間型を取得
		if _date.month != 12:
			_expected_date = datetime.datetime(
				year = _date.year,
				month = _date.month + 1,
				day = 1
			)
		else:
			_expected_date = datetime.datetime(
				year = _date + 1,
				month = 1,
				day = 1
			)
		
		# 来月までの時間を算出し，sleepする
		_timedelta = _expected_date - _date
		time.sleep(_timedelta.total_seconds()+1)
		post_ranking(client, db, range)
		_date = _expected_date	# 今月の時間型を更新