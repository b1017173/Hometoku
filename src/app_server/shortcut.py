def view_modal_from_shortcut(client, shortcut):
    # モーダル表示のリクエスト
    client.views_open(
        trigger_id = shortcut["trigger_id"],
        view = {
            "title": {
                "type": "plain_text",
                "text": "Hometoku",
            },
            "submit": {
                "type": "plain_text",
                "text": "Submit",
            },
            "type": "modal",
            "close": {
                "type": "plain_text",
                "text": "Cancel",
            },
            "blocks": [
                {
                    "type": "divider"
                },
                {
                    "block_id": "homePeople",
                    "type": "input",
                    "element": {
                        "type": "multi_users_select",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Select users",
                        },
                        "action_id": "multi_users_select-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "褒めたい人",
                    }
                },
                {
                    "block_id": "homeMove",
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "plain_text_input-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "褒めたいこと",
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
                            }
                        }
                    ]
                }
            ]
        }
    )