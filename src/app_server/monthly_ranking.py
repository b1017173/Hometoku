# ランキングデータを基にランキングメッセージの生成・送信
def view_ranking_message(client, channel_id, ranking_list):
	"""
	ranking_list: [
		[workspace_id:str, user_id:str, prise_count:int],
		...
	]
	"""
	_view_blocks = [
		{
			"type": "header",
			"text": {
				"type": "plain_text",
				"text": "月間ホメられたで賞",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": "今月たくさんホメられたあなたを紹介します！ "
			}
		},
		{
			"type": "divider"
		}
	]

	for rank in range(len(ranking_list)):
		# viewに付け足されるランキング(最大1位2位3位の3回増やす)
		_clap_count = ":clap:" * (3 - rank)
		_view_ranking =  {
				"type": "section",
				"text": {
					"type": "mrkdwn",
					"text": "*{0}位 <@{1}>*\n{2} 褒めた回数 {3}ホメ\n".format(rank+1, ranking_list[rank][1], _clap_count, ranking_list[rank][2])
				}
			}
		_view_blocks.append(_view_ranking)

	try:
		client.chat_postMessage(
			channel = channel_id,
			blocks = _view_blocks
		)
	except Exception as e:
		print("Error: sending ranking message is Failed, {0}".format(e))

def post_ranking(client, db):
	_team_info = client.team_info()
	_workspace_id = _team_info["team"]["id"]
	_channel_id = ""	# TODO: _channel_id = db.チャンネルIDの取得(_workspace_id)
	_ranking_list = []	# TODO: _ranking_list = db.ランキングリストの取得(_workspace_id, range = 3)

	# デバッグ用
	_channel_id = "C026DHW2A2G"			# workspace_idとchannel_idのリスト
	_ranking_list = [[_workspace_id, "U024LNTCHR8", "5"]] # ワークスペース毎の褒められランキングのリスト(1で抽出されたやつ)

	view_ranking_message(client, _channel_id, _ranking_list)

def all_ws_post_ranking(db):
	_workspaces = []	# TODO: _workspaces = db.ワークスペースリストの取得()

	for workspace in _workspaces:
		_client = ""
		post_ranking(_client, db)