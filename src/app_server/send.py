import app_server.positive_phrase as ph

#  modalに入力された内容をSlackで表示させる
def view_praise_message(say, workspace_id, targets_id, praise_writing, clup_num, db, logger):
	_claps:str = ":clap:" * clup_num
	_channel_id = db.get_channel_id(workspace_id)  # botが参加しているチャンネルIDをDBから取得

	try:
		say(
			channel = _channel_id,
			blocks = [
				{
                	"type": "section",
                	"text": {
                    	"type": "plain_text",
                    	"text": "========================================"
                	}
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ":confetti_ball::confetti_ball::confetti_ball::confetti_ball:    *ホメられ速報*    :confetti_ball::confetti_ball::confetti_ball::confetti_ball:"
                    }
                },
				{
                	"type": "section",
                	"text": {
                        "type": "plain_text",
                        "text": "☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…"
                	}
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": ph.random_positive(targets_id,praise_writing)
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": "☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…☆…"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "今回のホメたい度は...."
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": "＼／＼／＼／＼／＼／＼／＼／＼／＼／＼／＼／"
                    },
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
                        "type": "plain_text",
                        "text": "／＼／＼／＼／＼／＼／＼／＼／＼／＼／＼／＼"
                    },
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "すごいや！！！ :tada:"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "これは僕からのプレゼントだよ！"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "これからも頑張ってね！ :wave:"
                	}
                },
                {
                    "type": "section",
                    "text": {
                        "type": "plain_text",
                        "text": "========================================"
                    }
                }
			],
			text = f":confetti_ball: :confetti_ball: :confetti_ball: :confetti_ball:  ホメられ速報 :confetti_ball: :confetti_ball: :confetti_ball: :confetti_ball: " # 通知バナーの内容
		)
	except Exception as e:
		logger.error(f"Error posting praise message: {e}")
