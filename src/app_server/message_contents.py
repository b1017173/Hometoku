import random

#褒める文章を生成する関数
def random_positive(targets:list, praise_writing:str):
    _targets:str = get_targets_str(targets)
    _praise_writing = praise_writing
    _conversion_praise_writing = "*\n*".join(_praise_writing.splitlines()) # 改行があった場合 * を前後に追加(太文字にするため)
    _fix_praise_writing = _conversion_praise_writing.replace("**","") # 空行があった場合 ** を削除
  
    _positive_phrase_list = [
        "{0}さんへ\n「 *{1}* 」\n匿名さんより".format(_targets, _fix_praise_writing),
        "{0}の素晴らしい活躍の噂話を聞きました!\n「 *{1}* 」\nらしいですよ！".format(_targets, _fix_praise_writing),
        "{0}様．\n「 *{1}* 」\nという素晴らしい功績を残したため，チームメンバーよりここに賞する．".format(_targets, _fix_praise_writing),
        "シャイなチームメンバーから代わりに{0}をホメてって言われちゃった！\n「 *{1}* 」\nだって！凄いや！".format(_targets, _fix_praise_writing),
        "チームメンバーとタイムカプセルを掘りに行ったよ！\n{0}宛に\n「 *{1}* 」\nと書いてあったよ！".format(_targets, _fix_praise_writing),
        "伝書鳩が{0}宛にホメッセージを届けてきたよ！\n「 *{1}* 」\nと書いてあったよ！".format(_targets, _fix_praise_writing),
        "うちの犬が木の下で吠えててうるさい！もしかしてと思って掘ったら{0}宛の黄金のホメッセージが出てきたよ！\n「 *{1}* 」\nって書いてあったよ！".format(_targets, _fix_praise_writing),
        "ホメール文明の石碑に{0}宛のホメメッセージが記されている！どれどれ...\n「 *{1}* 」\nだって！文化遺産だね！".format(_targets, _fix_praise_writing),
        "ホメール神が{0}の\n「 *{1}* 」\nという善行に感動してたよ！".format(_targets, _fix_praise_writing),
        "{0}がいい子にしてたからサンタさんがプレゼント用意してたよ！\n「 *{1}* 」\nというのを見ていたんだって！".format(_targets, _fix_praise_writing),
        "チームメンバーがホメトークのホメたい芸人で{0}をホメていたよ！\n「 *{1}* 」\nというのを楽しそうに話していたよ！".format(_targets, _fix_praise_writing),
        "お出かけしていたら僕のところに非通知留守電が...怖いけど聞いてみよう...\n{0}へ\n「 *{1}* 」\n全然怖くないじゃん！".format(_targets, _fix_praise_writing),
        "{0}の\n「 *{1}* 」\nということをこっそりツイートしたら3万リツイートいっちゃったよ！\nバズったからホメとくを宣伝してきていいかな？".format(_targets, _fix_praise_writing),
        "始まりましたFMホメリアン！今日もホメッセージが届いております！\nラジオネーム : ホメラニアンさんから{0}さん宛に\n「 *{1}* 」\nと届いておりました！".format(_targets, _fix_praise_writing),
        "チームメンバーのパソコンに{0}宛に書きかけのホメッセージが残っていたよ！代わりに僕がホメちゃおう！\n「 *{1}* 」\n次は顔を見てホメられるといいね！".format(_targets, _fix_praise_writing),
        "近くの人が{0}宛にAirDropでホメッセージを送ってきたよ！\n「 *{1}* 」\n他の人も拾わないように早く切ってね！".format(_targets, _fix_praise_writing),
        "チームメンバーがwifiの名前を{0}にして，パスワードを\n「 *{1}* 」\nにしちゃったよ！気持ちが溢れすぎたね！".format(_targets, _fix_praise_writing),
        "こないだの土曜日，チームメンバーが\n「{0}さんへ， *{1}* ありがとう」\nって背中に書いてあるTシャツを着て外を歩いていたよ！\nもうそれ直接言った方が恥ずかしくないと思うよ！".format(_targets, _fix_praise_writing),
        "チームメンバーがブルーインパルスにお願いして\n「{0}さんへ， *{1}* 」\nって書いてもらってたよ！\nよく協力してもらえたね！".format(_targets, _fix_praise_writing),
        "花火大会で\n「{0}へ， *{1}* 」\nと書いた10寸玉が上がってたよ！".format(_targets, _fix_praise_writing)
    ]

    return _positive_phrase_list[random.randrange(0,len(_positive_phrase_list))]

# ホメられた人のIDをstrで返す関数
def get_targets_str(targets_id:str):
    _targets_str:str = ""
    
    for target in targets_id:
        _targets_str += "<@{0}>".format(target)

    return _targets_str

# ホメられ度によってテキストとgifを返す関数
def get_clap_contents(clap_num:int, targets_id:str):
	_targets_str = get_targets_str(targets_id)
	_last_text:str = ""
	_gif_url:str = ""

	if clap_num < 3:
		_last_text = "いいですね〜{0}\n\nその調子！！".format(_targets_str)
		_gif_url = "https://media.giphy.com/media/iziZJkVonHMMKElQTt/giphy.gif"
	elif clap_num < 5:
		_last_text = "さすがだなぁ〜\n\nそんな{0}にグッジョブ:+1::+1:".format(_targets_str)
		_gif_url = "https://media.giphy.com/media/xUSVThgS8BzMSE3ZjQ/giphy.gif"
	elif clap_num < 7:
		_last_text = "すごい！:hushed:\n\n{0}は絶好調だね:+1::+1:\n\nこのホメ合いがまた一つ団結力を強くしたね:muscle::muscle:".format(_targets_str)
		_gif_url = "https://media.giphy.com/media/fbonqRT3Bv53VfZVaH/giphy.gif"
	elif clap_num < 9:
		_last_text = "最高のチームメンバーだ！！:clap::clap:\n\nあふれるホメたい度にチームも大盛り上がり！！:arrow_heading_up::arrow_heading_up:"
		_gif_url = "https://media.giphy.com/media/VrBF7FxUC8ZVSeJPOH/giphy.gif"
	else:
		_last_text = "これはとんでもなく褒められてますよ:bangbang::bangbang:\n\n過去1のホメたい度かもしれません:bangbang::bangbang:\n\n{0}はみんなの誇りだね:bangbang:".format(_targets_str)
		_gif_url = "https://media.giphy.com/media/LADGQ3DIlxW0cSBg1R/giphy.gif"

	return _last_text, _gif_url