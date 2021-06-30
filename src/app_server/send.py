import app_server.positive_phrase as ph
import database.connect_mysql as cm

#  modalに入力された内容をSlackで表示させる
def view_praise_message(client, workspace_id, targets_id, praise_writing, clup_num, logger):
	_claps:str = ""
	db = cm.Database()
	_channel_id = db.get_channel_id(workspace_id)  # botが参加しているチャンネルIDをDBから取得

	# 拍手数の数だけ:clap:を追加
	for i in range(clup_num):
		_claps += ":clap:"

	try:
		client.chat_postMessage(
			channel=_channel_id,
        	blocks=[
				{
					"type": "section",
					"text": {
						"type": "mrkdwn",
						"text": ph.random_positive(targets_id, praise_writing)
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
