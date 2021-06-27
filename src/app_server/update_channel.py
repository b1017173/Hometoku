# 参加に成功した際のメッセージプレビュー
def success_join_channel():
	return {
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

# 他に参加しているチャンネルがあるときのメッセージプレビュー
def failed_join_channel(_joined_channel_id):
	return {
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

# コマンドによってチャンネルに参加する(参加できるのは1つのチャンネルだけ)
def update_channel(say, _new_channel_id, _old_channel_id, client, db):
	exit_channel(_old_channel_id, client, db)
	setup_channel(say, _new_channel_id, client, db)

# チャンネルの参加
def setup_channel(say, _channel_id, client, db):
	_success_message = success_join_channel()

	try:
		# TODO: db.チャンネル情報の書き込み(_channel_id)
		client.conversations_join(channel = _channel_id)
		say(text = _success_message, channel = _channel_id)
	except Exception as e:
		print("Error: Failed to join the channel.\n{0}".format(e))

# チャンネルの退出
def exit_channel(_channel_id, client, db):
	try:
		client.conversations_leave(channel = _channel_id)
		# TODO: db.チャンネル情報の消去()
	except Exception as e:
		print("Error: Failed to join the channel.\n{0}".format(e))

def cant_setup_channel(say, _channel_id, _joined_channel_id, _user_id, client, db):
	_failed_message = failed_join_channel(_joined_channel_id)

	try:
		# TODO: 単純にsay()するのではなく，_user_idのユーザにのみ見えるメッセージで
		# 		他のチャンネルに参加していることを伝える
		pass
	except Exception as e:
		print("Error: Failed to join the channel.\n{0}".format(e))