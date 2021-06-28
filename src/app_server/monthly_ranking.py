from slack_sdk import WebClient

def post_monthlyranking(client): #褒められた回数を各ワークスペースtop3までを表彰
     """1.workspace_idとchannel_idのテーブルをみて，workspace_idで褒めたときにsubmitされたレコードを抽出
        2.褒められた回数でソート
        3.top3までjsonでworkspace_idのchannel_idのとこに送信(誰もいなかったら煽るか)
        123をworkspace_idテーブルの長さ分ぶんまわす"""
     #オーダーバイカラム名で褒められ度でソートしてリミット３とかでひっぱてこれるらしいぞ

     _workspaceList = [["workspece_id","C026DHW2A2G"]] #workspace_idとchannel_idのリスト
     for idList in _workspaceList: #[0]:workspace_id [1]: channel_id
         _rankingList = [["gszdtxtj","U024LNTCHR8","5"]] #ワークスペース毎の褒められランキングのリスト(1で抽出されたやつ)
         view = {#最終的にslackに表示されるもの
	     "blocks": [
		     {
			     "type": "header",
			     "text": {
				     "type": "plain_text",
				     "text": "月間ホメられたで賞",
				     "emoji": True
			     }
		     },
		     {
			     "type": "section",
			     "text": {
				     "type": "plain_text",
				     "text": "今月たくさんホメられたあなたを紹介します！ "
			     }
             },
             {
                 "type": "divider"
             },
         ]
     }

         for rank in range(0,len(_rankingList)):
            _clapCount = ":clap:"*(3-rank)
            _ranking =  {#viewに付け足されるランキング(最大1位2位3位の3回増やす)
                     "type": "section",
                     "text": {
                         "type": "mrkdwn",
                         "text": "*{0}位 <@{1}>*\n{2} 褒めた回数 {3}ホメ\n".format(str(rank+1),_rankingList[rank][1],_clapCount,_rankingList[rank][2])
                     }
                 },
            view["blocks"].append(_ranking)

         try :
            client.chat_postMessage(channel = idList[1],text = view)
         except Exception as e:
            print("Error: Failed to send a message the channel.\n{0}".format(e))

"""
     client.chat_postMessage(
         channel="C025BBH57LN",
         channel="C024ZBFDEU9",  #  testチャンネル:C025BBH57LN random:C024ZBFDEU9
         blocks=[
             {
 			"type": "header",
 			"text": {
 				"type": "plain_text",
 				"text": "ほめたい速報:thumbsup:",
 				"emoji": True
 			}
 		},
 		{
 			"type": "section",
 			"text": {
 				"type": "mrkdwn",
 				"text": mention(targets_id)
 			}
 		},
 		{
 			"type": "divider"
 		},
 		{
 			"type": "section",
 			"text": {
 				"type": "mrkdwn",
 				"text": praise_writing
 				"text": ph.random_positive(targets_id,praise_writing)
 			}
 		},
 		{
 @@ -59,12 +42,3 @@ def contents_to_slack(client, targets_id, praise_writing, *prise_quantity):
 		}
         ]
     )"""