# コマンドによってチャンネルに参加する
def set_channel(say, command, client):
    _channel_id = command["channel_id"]
    #  参加した時に表示させるMessagePreview
    _success_message = {
	        "blocks": [
		            {
			            "type": "section",
			            "text": {
				            "type": "mrkdwn",
				            "text": "招待ありがとう！！\nこれからはこのチャンネルでホメッセージを発信していくよ！！"
			         }
		            },
		            {
			            "type": "image",
			            "image_url": "https://media.giphy.com/media/cnuS67F8IoVTYRvJXE/giphy.gif",
			            "alt_text": "success!!!"
		            }
	            ]
            }

    #  すでに参加している時に表示させるMessagePreview
    _failure_message = {
	        "blocks": [
		        {
			        "type": "section",
			        "fields": [
				        {
					        "type": "mrkdwn",
					        "text": "ごめんなさい....\nもう他のチャンネルにいるんだよね....\n#channelで呼んでもらってもいいかな....??"
				        }
			        ]
		        },
		        {
			        "type": "image",
			        "image_url": "https://tenor.com/vIAq.gif",
			        "alt_text": "failure..."
		        }
	        ]
        }

    try:
        ## TODO: データベースにアクセスしてすでに参加しているチャンネルがないかを調べる
        # if 参加している:
        #   TODO: すでに参加している系のメッセージを送る
        # say(text = _failure_message, channel = _channel_id)  #  コマンドが入力されたチャンネルにすでに参加してるメッセージを送信
        # else:
        #   TODO: 参加させる(実装済)+参加したよのメッセージ送る
        client.conversations_join(channel = _channel_id)
        say(text = _success_message, channel = _channel_id)  #  コマンドが入力されたチャンネルに参加したよのメッセージ送信

    except Exception as e:
        print("Error: Failed to join the channel.\n{0}".format(e))