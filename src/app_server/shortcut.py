def view_modal_from_shortcut(client, shortcut):
    # モーダル表示のリクエスト
    client.views_open(
        trigger_id = shortcut["trigger_id"],
        view = {
        "callback_id": "modal_homeru",
        "title": {
            "type": "plain_text",
            "text": "Hometoku",
            "emoji": True
        },
        "submit": {
            "type": "plain_text",
            "text": "Submit",
            "emoji": True
        },
        "type": "modal",
        "close": {
            "type": "plain_text",
            "text": "Cancel",
            "emoji": True
        },
        "blocks": [
            {
                "type": "divider"
            },
            {
                "block_id": "homepeople",
                "type": "input",
                "element": {
                    "type": "multi_users_select",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Select users",
                        "emoji": True
                    },
                    "action_id": "select_homepeople"
                },
                "label": {
                    "type": "plain_text",
                    "text": "褒めたい人",
                    "emoji": True
                }
            },
            {
                "block_id": "homemove",
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "multiline": True,
                    "action_id": "input_homemove"
                },
                "label": {
                    "type": "plain_text",
                    "text": "褒めたいこと",
                    "emoji": True
                }
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "褒めたい度",
                            "emoji": True
                        }
                    }
                ]
            },
            {
                "type": "context",
			    "block_id": "prize_counter",
			    "elements": [
				    {
                        "type": "mrkdwn",
                        "text": ":clap: :clap::clap::clap::clap::clap::clap::clap: "
                    }
                ]
            }
        ]
        }
    )
