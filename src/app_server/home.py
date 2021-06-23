# ホームタブに表示するヘルプのビュー
def view_help_message(client, event, logger):
    try:
        client.views_publish(
            user_id=event["user"],
            view = {
                "type": "home",
                "blocks": [
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "ようこそ",
                            "emoji": True
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "チームメンバーを素直にホメることや感謝の気持ちを伝えるのが恥ずかしい時がありませんか？\n*ホメとく* はそんなあなたのメッセージを匿名で伝える役を引き受けます．"
                        }
                    },
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "使い方",
                            "emoji": True
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*チャンネルの登録*\n👉 タブの上部にあるアプリ名をタップし「+ チャンネルにこのアプリを追加する」から追加したいチャンネルを選択"
                        }
                    },
                    {
                        "type": "image",
                        "title": {
                            "type": "plain_text",
                            "text": "1. タブ上部をタップ",
                            "emoji": True
                        },
                        "image_url": "https://live.staticflickr.com/65535/51264777379_432e3274be_b.jpg",
                        "alt_text": "help1"
                    },
                    {
                        "type": "image",
                        "title": {
                            "type": "plain_text",
                            "text": "2. チャンネルを選択",
                            "emoji": True
                        },
                        "image_url": "https://live.staticflickr.com/65535/51263373722_e26b710262_b.jpg",
                        "alt_text": "help2"
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*ホメる！*\n👉 ワークスペース内でショートカットからホメる！を起動して，ホメたい人・ホメッセージ・ホメたい度を入力しよう！"
                        }
                    },
                    {
                        "type": "image",
                        "title": {
                            "type": "plain_text",
                            "text": "1. ショートカットの起動",
                            "emoji": True
                        },
                        "image_url": "https://live.staticflickr.com/65535/51264172256_77fd06c585_b.jpg",
                        "alt_text": "help3"
                    },
                    {
                        "type": "image",
                        "title": {
                            "type": "plain_text",
                            "text": "2. ホメる！を選択",
                            "emoji": True
                        },
                        "image_url": "https://live.staticflickr.com/65535/51265241465_406dfacbca_b.jpg",
                        "alt_text": "help4"
                    },
                    {
                        "type": "image",
                        "title": {
                            "type": "plain_text",
                            "text": "3. 各項目の入力",
                            "emoji": True
                        },
                        "image_url": "https://live.staticflickr.com/65535/51266196076_308df7bfe6_b.jpg",
                        "alt_text": "help4"
                    }
                ]
            }
        )
    except Exception as e:
        logger.error(f"Error publishing home tab: {e}")