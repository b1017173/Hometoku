# カスタマイズされたモーダルを返す
def view_modal(clap:str):
    return {
        "callback_id": "modal_homeru",
        "title": {
            "type": "plain_text",
            "text": "Hometoku",
            "emoji": True
        },
        "submit": {
            "type": "plain_text",
            "text": "送信",
            "emoji": True
        },
        "type": "modal",
        "close": {
            "type": "plain_text",
            "text": "キャンセル",
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
                        "action_id": "prise_countup",
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
			    "block_id": "prise_counter",
			    "elements": [
				    {
                        "type": "mrkdwn",
                        "text": clap
                    }
                ]
            }
        ]
        }

# ショートカットが押された時に表示するモーダルを生成する関数
def view_modal_from_shortcut(client, shortcut):
    # モーダル表示のリクエスト
    _clap = ":clap:"
    client.views_open(
        trigger_id = shortcut["trigger_id"],
        view = view_modal(_clap)
    )

# 褒めたい度が上がった時にモーダルを更新する関数
def update_modal_from_countup(body, client):
    # _clap = view["state"]["values"]["prise_counter"]
    # _clap = body["view"]["state"]["values"]["prise_counter"]
    _clap = body["view"]["blocks"][4]["elements"][0]["text"]
    _clap += ":clap:"
    client.views_update(
        view_id = body["view"]["id"],
        hash = body["view"]["hash"],
        view = view_modal(_clap)
    )

# チャンネルの登録がされていない状態で，ホメる！が押された時のモーダル
def view_modal_not_set_channel(client, shortcut):
    client.views_open(
        trigger_id = shortcut["trigger_id"],
        view = {
            "callback_id": "modal_not_set_channel",
            "type": "modal",
            "title": {
                "type": "plain_text",
                "text": "チャンネルの登録がされていません",
                "emoji": True
            },
            "close": {
                "type": "plain_text",
                "text": "確認",
                "emoji": True
            },
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "*ホメる！* を使うためにはホメとくをチャンネルに登録する必要があります．"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": "チャンネルの登録は，登録したいチャンネルで `/hometoku_set_channel` と入力することで行えます．\nチャンネルの登録の詳細はホメとくとのDMのホームタブから確認できます．"
                    }
                }
            ]
        }
    )