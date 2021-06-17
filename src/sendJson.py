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
        # 褒め尺度 home_scale = 

        send_json_contents = dict()
        send_json_contents['homePeople'] = home_targets
        send_json_contents['homeMove'] = home_contents

        print(send_json_contents)

    def __object_json(self,json_data:dict):
        return a

'''
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