import os
# Use the package we installed
from slack_bolt import App
import app_server.shortcut as sc

# Initializes your app with your bot token and signing secret
app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

# 'shortcut_homeru' という callback_id のショートカットをリッスン
@app.shortcut("shortcut_homeru")
def open_modal(ack, shortcut, client):
    # リクエストを受け付け
    ack()
    sc.view_modal_from_shortcut(client, shortcut)

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))