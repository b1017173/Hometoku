import app_server.positive_phrase as ph

#  modalに入力された内容をSlackで表示させる
def view_praise_message(client, targets_id, praise_writing, clup_num, logger):
	_targets_id = targets_id
	_praise_writing = praise_writing
	_clup_num = clup_num
	_claps:str = ""
	_channel_id = "C026DHW2A2G" #Botが参加しているチャンネルID testチャンネル:C025BBH57LN random:C024ZBFDEU9 test_kai：C026DHW2A2G

	# 拍手数の数だけ:clap:を追加
	for i in range(_clup_num):
		_claps += ":clap:"

	# TODO: DBからBotが参加しているチャンネルIDを持ってきて変数_channel_idを変更する

	try:
		client.chat_postMessage(
			channel=_channel_id,
        	blocks=[
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
						"text": ph.random_positive(_targets_id, _praise_writing)
					}
				},
				{
					"type": "divider"
				},
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
						"text": ":clap:ほめクラップ:clap:"
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
					"type": "image",
					"title": {
						"type": "plain_text",
						"text": "homehome",
						"emoji": True
					},
					"image_url": "https://tenor.com/bfiRs.gif",
					"alt_text": "marg"
				}
			]
		)	
	except Exception as e:
		logger.error(f"Error posting praise message: {e}")
