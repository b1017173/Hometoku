import app_server.message_contents as mc

#  modalに入力された内容をSlackで表示させる
def view_praise_message(say, workspace_id, targets_id, praise_writing, clap_num, db, logger):
	_channel_id = db.get_channel_id(workspace_id)  # botが参加しているチャンネルIDをDBから取得
	_result = mc.get_clap_contents(clap_num, targets_id) # 褒められ度によって変わるテキストとgifのURLを取得

	try:
		say(
			channel = _channel_id,
			blocks = [
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
						"text": ":confetti_ball::confetti_ball::confetti_ball:    *ホメられ速報*    :confetti_ball::confetti_ball::confetti_ball:"
					}
				},
				{
					"type": "divider"
				},
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
						"text": mc.random_positive(targets_id, praise_writing)
					}
				},
				{
					"type": "divider"
				},
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
						"text": "{0}\n\nみんなからのホメッセージも待ってるよ！！".format(_result[0])
					},
					"accessory": {
						"type": "image",
						"image_url": _result[1],
						"alt_text": "gif"
					}
				},
				{
					"type": "divider"
				}
			],
			text = "ホメられ速報" # 通知バナーの内容
		)
	except Exception as e:
		logger.error(f"Error posting praise message: {e}")
