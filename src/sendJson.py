import json
    
 #  modalに入力された内容の中身が記述されているJsonファイルを読み込む
def make_json_file(self,json_data:str):
    catch_json_read = json.load(json_data)

    home_targets = catch_json_read["homePeople"]["multi_users_select-action"]["selected_users"] #  褒める相手を抽出
    home_contents = catch_json_read["homeMove"]["plain_text_input-action"]["value"]  #  褒め内容を抽出

    home_data = dict()  #  必要な要素だけを入れておくdict
    home_data["homePeople"] = home_targets  #  褒める相手の要素を入れる
    home_data["homeMove"] = home_contents  #  褒め内容を入れる