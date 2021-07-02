# ランキングデータを基にランキングメッセージの生成・送信
import datetime
import time

def view_ranking_message(client, channel_id, ranking_list):
	_view_blocks = "" # 最終的に出力されるjson
	_dt_now = datetime.datetime.now()
	_int_to_english = ["zero","one","two","three","four","five","six","seven","eight","nine"] # 添字の数字を英語に変える
	_twodiamond_symbol = ":diamond_shape_with_a_dot_inside:" * 2
	if(_dt_now.month != 1):
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
	else:
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
					"text": "12月にたくさんホメられたあなたを表彰します！"
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
					"text": "{0}*感謝状*{0}\n\n*<@{1}>殿* \nあなたは1ヶ月間で最もチームのメンバーから活躍を認められました．\nその栄誉を讃えつつ， *ホメとくを利用する機会をくれたこと* に感謝の意を表します．\n       　　　     　　　　   　　　　　{2}月{3}日　チームカタンより\n{4}"\
					.format(_twodiamond_symbol, ranking_list[0][1], _dt_now.month, _dt_now.day, _twodiamond_symbol * 3)
			},
			"accessory": {
				"type": "image",
				"image_url": "https://cdn-ak.f.st-hatena.com/images/fotolife/s/sizimi0527/20210702/20210702203617_120.jpg",
				"alt_text": "hometoku"
			}
		},
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
					"text": "{0}{1}*{2}位*{1}\n<@{3}> ホメられ度 {4} \n\n".format("　 " * rank, _clap_count, rank+1, ranking_list[rank][1], _score_symbol)
				}
			}
		_view_blocks.append(_view_ranking)

	for map in _view_thanks :
		_view_blocks.append(map) # 最後に感謝文追加

	try:
		client.chat_postMessage(
			channel = channel_id,
			blocks = _view_blocks,
			text = "月間ランキングが投稿されました！"
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


# TODO 複数ワークスペースに送る場合の関数
def all_ws_post_ranking(db):
	_workspaces = []	# TODO: _workspaces = db.ワークスペースリストの取得()

	for workspace in _workspaces:
		_client = ""
		post_ranking(_client, db)

# 毎月自動投稿する関数
def post_permonth_ranking(client, db, range):
	# デバッグするときは_dateを今月最終日の23:59分に設定する
	# _date = datetime.datetime(year, month, day, hour, minute)
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