#  アプリが追加されているチャンネルIDを取得
def channel_id(client):

    _hometoku_id:str = ""
    _channel_member_id = {}
    _members_list = client.users_list()  #  ワークスペース内の全てのユーザー情報を取得（APP，Botも含む）
    _members = _members_list.data['members']
    for _member in _members:
        if _member['name'] == "hometoku":
            _hometoku_id = _member['id']  # hometokuのID取得

    _channels_list = client.conversations_members
    print(_channels_list)

    # _user_info = client.users_info(
    #     user=_hometoku_id
    #     )