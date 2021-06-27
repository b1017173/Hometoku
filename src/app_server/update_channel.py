# コマンドによってチャンネルに参加する(参加できるのは1つのチャンネルだけ)
def update_channel(say, command, client):
    _channel_id = command["channel_id"] # コマンドが呼ばれたチャンネルID用の変数
    _user_id = command["user_id"] # コマンドを呼び出した人のユーザーID用の変数
    _joined_channel_id:str = ""  # 既に参加しているチャンネルID用の変数

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
					        "text": "ごめんなさい....\nもう他のチャンネルにいるんだよね....\n<#{0}>で呼んでもらってもいいかな....??".format(_joined_channel_id)
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
        # TODO: DBにアクセスしてすでに参加しているチャンネルがないかを調べる
        # if 参加している:
		# TODO:すでに参加しているチャンネルIDをDBから取得して _joined_channel_idに保存
		# コマンドを呼び出した人だけに見えるメッセージを送信
        # client.chat_postEphemeral(text = _failure_message, channel = _channel_id, user = _user_id)  
        # else:
        client.conversations_join(channel = _channel_id)  #  コマンドが入力されたチャンネルに参加する
        say(text = _success_message, channel = _channel_id)  #  コマンドが入力されたチャンネルに参加したよのメッセージ送信
		# TODO: DBにBotが参加したワークスペースID，チャンネルIDを追加する

    except Exception as e:
        print("Error: Failed to join the channel.\n{0}".format(e))