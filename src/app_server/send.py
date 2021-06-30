import app_server.positive_phrase as ph

#  modalに入力された内容をSlackで表示させる
def view_praise_message(say, workspace_id, targets_id, praise_writing, clup_num, db, logger):
	_claps:str = ""
	_channel_id = db.get_channel_id(workspace_id)  # botが参加しているチャンネルIDをDBから取得

	# 拍手数の数だけ:clap:を追加
	for i in range(clup_num):
		_claps += ":clap:"

	try:
		say(
			channel = _channel_id,
			blocks = [
				{
					"type": "header",
					"text": {
						"type": "plain_text",
						"text": ":confetti_ball: :confetti_ball: :confetti_ball: :confetti_ball:  ホメられ速報 :confetti_ball: :confetti_ball: :confetti_ball: :confetti_ball: ",
						"emoji": True
					}
				},
				{
					"type": "divider"
				},
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
						"text": ph.random_positive(targets_id,praise_writing)
					}
				},
				{
					"type": "divider"
				},
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
						"text": "*今回のホメたい度は....*"
					}
				},
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
						"text": _claps
					}
				},
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
						"text": "すごいや！！！ :tada:"
					}
				},
				{
					"type": "divider"
				},
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
						"text": "これは僕からのプレゼントだよ！"
					}
				},
				{
					"type": "image",
					"title": {
						"type": "plain_text",
						"text": "homehome",
						"emoji": True
					},
					"image_url": "https://tenor.com/view/nanon-nanon-korapat-%e0%b8%99%e0%b8%99%e0%b8%99-%e0%b8%99%e0%b8%99%e0%b8%99%e0%b8%81%e0%b8%a3%e0%b8%a0%e0%b8%b1%e0%b8%97%e0%b8%a3%e0%b9%8c-hearts-gif-22124241",
					"alt_text": "marg"
				},
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
						"text": "これからも頑張ってね！ :wave:"
					}
				}			
			],
			text = f":confetti_ball: :confetti_ball: :confetti_ball: :confetti_ball:  ホメられ速報 :confetti_ball: :confetti_ball: :confetti_ball: :confetti_ball: " # 通知バナーの内容
		)
	except Exception as e:
		logger.error(f"Error posting praise message: {e}")
