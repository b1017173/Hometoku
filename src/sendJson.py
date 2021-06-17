import json


class SendJson:

    def __init__(self) -> None:
        pass
    
    #  modalに入力された内容の中身が記述されているJsonファイルを読み込む
    def make_json_file(self,json_path:str):
        with open(json_path, 'r') as catch_json_open:
            catch_json_read = json.load(catch_json_open)

        home_targets = catch_json_read["homePeople"]["multi_users_select-action"]["selected_users"] #  褒める相手を抽出
        home_contents = catch_json_read["homeMove"]["plain_text_input-action"]["value"]  #  褒め内容を抽出

        home_data = dict()  #  必要な要素だけを入れておくdict
        home_data["homePeople"] = home_targets  #  褒める相手の要素を入れる
        home_data["homeMove"] = home_contents  #  褒め内容を入れる

        with open('data/send_test.json','w') as send_json:
            json.dump(home_data, send_json, ensure_ascii=False, indent=2)

'''
    #  必要な要素（褒めたい相手，褒め内容，褒め尺度）を抽出
    def __element_extraction(self,json_data:dict):
        #home_people = json_box.homePeople.multi_users_select-action.selected_users
        #home_contents = json_box.homeMove.plain_text_input-action.value
        # 褒め尺度 home_scale = 

        #need_element = dict()
        #need_element.update(home_people,home_contents)

    #  SlackAppが表示する情報のみを抽出
    def __extract_data(self,catch_json_data):

        home_targets = catch_json_data["homePeople"]["multi_users_select-action"]["selected_users"]  #  褒める相手を抽出
        home_contents = catch_json_data["homeMove"]["plain_text_input-action"]["value"]  #  褒め内容を抽出
        # 褒め尺度 home_scale
        
        self.write_json(home_targets,home_contents)

    #  SlackAppが表示する情報をJsonとして変換
    def __write_json(self,):

        print(home_targets, home_contents)
'''