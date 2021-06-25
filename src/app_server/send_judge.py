def message_success_or_failure(client,channel_id:str,judge:bool):

    if judge == True:
        client.chat_postMessage(
            channel = channel_id,
            blocks = [
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
        )
    else:
        client.chat_postMessage(
            channel = channel_id,
            blocks = [
                {
			        "type": "section",
			        "fields": [
				        {
					        "type": "plain_text",
					        "text": "ごめんなさい....\nもう他のチャンネルにいるんだよね....\n#channelで呼んでもらってもいいかな....??",
					        "emoji": true
				        }
			        ]
		        },
		        {
			        "type": "image",
			        "image_url": "https://tenor.com/vIAq.gif",
			        "alt_text": "failure..."
		        }
            ]
        )