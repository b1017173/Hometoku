# コマンドによってチャンネルに参加する
def set_channel(say, command, client):
    _channel_id = command["channel_id"]
    try:
        ## TODO: データベースにアクセスしてすでに参加しているチャンネルがないかを調べる
        # if 参加している:
        #   TODO: すでに参加している系のメッセージを送る
        #   say("別の場所に参加してるよ")
        # else:
        #   TODO: 参加させる(実装済)+参加したよのメッセージ送る
        client.conversations_join(channel = _channel_id)
        # say("参加したお")

    except Exception as e:
        print("Error: Failed to join the channel.\n{0}".format(e))