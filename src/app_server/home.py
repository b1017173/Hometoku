# ホームタブに表示するヘルプのビュー
def view_help_message(client, event, logger):
    _channel_id = "未登録"
    # TODO: データベースにアクセスして登録チャンネルを取得する
    try:
        client.views_publish(
            user_id = event["user"],
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
                            "text": "*✅ チャンネルの登録*\n\nホメとくを使うためには，ホメとくが活躍できるチャンネルを登録する必要があります．以下の *変更/更新ボタン* をタップしてチャンネルの登録をしてみましょう．"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*現在の登録チャンネル：*{0}".format(_channel_id)
                        },
                        "accessory": {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "変更/更新",
                                "emoji": True
                            },
                            "value": "is_clicked",
                            "action_id": "update_channel"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*登録したいチャンネルで* 以下のコマンドを入力することで新規登録・更新することも可能です．"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*新規登録*\n`/hometoku_set_channel`"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*登録チャンネルの更新*\n`/hometoku_update_channel`"
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "*👏 ホメる！*\n\n*ホメる！* 機能を使うことで，匿名でチームメンバーに *ホメるメッセージ(ホメッセージ)* を伝えることができます．ホメる！機能はショートカットから使うことができます．"
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

def view_modal_from_help(body, client):
    client.views_open(
        trigger_id = body["trigger_id"],
        view = {
            "callback_id": "modal_update_channel",
            "type": "modal",
            "title": {
                "type": "plain_text",
                "text": "チャンネルの登録・更新",
                "emoji": True
            },
            "submit": {
                "type": "plain_text",
                "text": "更新",
                "emoji": True
            },
            "close": {
                "type": "plain_text",
                "text": "キャンセル",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "セレクターをタップしてホメとくの登録したいチャンネルを選択してください．\n※ プライベートチャンネルに設定することはできません\n※ 更新を行うと選択したチャンネルにホメとくが追加されます"
                    }
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "conversations_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "登録チャンネルを選択",
                                "emoji": True
                            },
                            "filter": {
                                "include": [
                                    "public"
                                ]
                            },
                            "action_id": "select_channel"
                        }
                    ]
                }
            ]
        }
    )