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
	return [
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text": "ごめんなさい....\nもうすでに<#{0}>に登録されているんだ....\nもしチャンネルを更新したい場合は\n`/hometoku_update_channel`\nを登録したいチャンネルで入力してね！！".format(_joined_channel_id)
				}
			]
		},
		{
			"type": "image",
			"image_url": "https://tenor.com/vIAq.gif",
			"alt_text": "failure..."
		}
	]

# 既に参加しているチャンネル内でコマンドが呼ばれたときのメッセージプレビュー
def aleady_exist_channel(_user_id):
	return [
		{
			"type": "section",
			"fields": [
				{
					"type": "mrkdwn",
					"text":"もうすでにこのチャンネルにいるよ！！ \n <@{0}>さんからのホメッセージ，待ってるよ！！".format(_user_id)
				}
			]
		}
	]
# 参加チャンネルを更新
def update_channel(say, _workspace_id, _new_channel_id, _old_channel_id, client, db):
	exit_channel(_old_channel_id, client)
	setup_channel(say, _workspace_id,  _new_channel_id, client, db)

# チャンネルの参加(参加できるのは1つだけ)
def setup_channel(say, _workspace_id, _channel_id, client, db):
	_success_message = success_join_channel()
	try:
		db.set_channel_id(_workspace_id, _channel_id)
		client.conversations_join(channel = _channel_id)
		say(text = _success_message, channel = _channel_id)
	except Exception as e:
		print("Error: Failed to join the channel.\n{0}".format(e))

# チャンネルの退出
def exit_channel(_channel_id, client):
	try:
		client.conversations_leave(channel = _channel_id)
	except Exception as e:
		print("Error: Failed to leave the channel.\n{0}".format(e))

# 別のチャンネルに参加中
def cant_setup_channel(_joined_channel_id, _user_id, client):
	_failed_message = failed_join_channel(_joined_channel_id)

	try:
		# コマンドを読んだ人にしか見えないメッセージを送信
		client.chat_postEphemeral(channel = _joined_channel_id, user = _user_id, blocks = _failed_message)
	except Exception as e:
		print("Error: Failed to join the channel.\n{0}".format(e))

# 参加中のチャンネル内でコマンドがよばれた場合
def send_aleady_exist_message(_channel_id, _user_id, client):
	_exist_message = aleady_exist_channel(_user_id)

	try:
		# コマンドを読んだ人にしか見えないメッセージを送信
		client.chat_postEphemeral(channel = _channel_id, user = _user_id, blocks = _exist_message)
	except Exception as e:
		print("Error: Failed to send the exist message.\n{0}".format(e))