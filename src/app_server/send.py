import app_server.positive_phrase as ph

#  modalに入力された内容をSlackで表示させる関数
def contents_to_slack(client, targets_id, praise_writing, *prise_quantity):

    client.chat_postMessage(
        channel="C025BBH57LN",  #  testチャンネル:C025BBH57LN random:C024ZBFDEU9
        blocks=[
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
				"text": ":clap:ほめクラップ:clap:"
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": ":clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap::clap:"
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
