# ショートカットが押された時に表示するモーダルを生成する関数
def view_modal_from_shortcut(client, shortcut):
    # モーダル表示のリクエスト
    client.views_open(
        trigger_id = shortcut["trigger_id"],
        view = {
            "type": "modal",
            "title": {"type": "plain_text", "text":"My App"},
            "close": {"type": "plain_text", "text":"Close"},
            "blocks": [
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text":"About the simplest modal you could conceive of :smile:\n\nMaybe <https://api.slack.com/reference/block-kit/interactive-components|*make the modal interactive*> or <https://api.slack.com/surfaces/modals/using#modifying|*learn more advanced modal use cases*>."
                    }
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "mrkdwn",
                            "text":"Psssst this modal was designed using <https://api.slack.com/tools/block-kit-builder|*Block Kit Builder*>"
                        }
                    ]
                }
            ]
        }
    )

# 褒めたい度が上がった時にモーダルを更新する関数
def update_modal_from_countup(body, client):
    client.views_update(
        view_id = body["view"]["id"],
        hash = body["view"]["hash"],
        view={
            "type": "modal",
            # ビューの識別子
            "callback_id": "view_1",
            "title": {"type": "plain_text", "text":"Updated modal"},
            "blocks": [
                {
                    "type": "section",
                    "text": {"type": "plain_text", "text":"You updated the modal!"}
                },
                {
                    "type": "image",
                    "image_url": "https://media.giphy.com/media/SVZGEcYt7brkFUyU90/giphy.gif",
                    "alt_text":"Yay!The modal was updated"
                }
            ]
        }
    )