from slack_bolt import App
#  必要な要素を取得してSlackに送信して表示
def contents_to_slack(client, targets_id, praise_writing, *prise_quantity):
    #  (client, logger, user_id, targets_id, praise_writing, *prise_quantity)
    
    '''
    #  褒めたい相手のUserIDを変換
    for user_id in targets_id:
        return "i"
    '''

    #  メッセージ表示のリクエスト
    print(targets_id,praise_writing)
    client.chat_postMessage(
        channel="C025BBH57LN",
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": targets_id
                }
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": praise_writing 
                }
            }
        ]
    )