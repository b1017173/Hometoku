import random

#褒める文章を生成する関数
def random_positive(targets:list, prise_writing:str):
    _targets:str = get_targets_str(targets)
  
    _positive_phrase_list = [
        "{0}さんへ\n「 *{1}* 」\n匿名さんより".format(_targets, prise_writing),
        "{0}の素晴らしい活躍の噂話を聞きました!\n「 *{1}* 」\nらしいですよ！".format(_targets, prise_writing),
        "{0}様．\n「 *{1}* 」\nという素晴らしい功績を残したため，チームメンバーよりここに賞する．".format(_targets, prise_writing),
        "シャイなチームメンバーから代わりに{0}をホメてって言われちゃった！\n「 *{1}* 」\nだって！凄いや！".format(_targets, prise_writing),
        "チームメンバーとタイムカプセルを掘りに行ったよ！\n{0}宛に\n「 *{1}* 」\nと書いてあったよ！".format(_targets, prise_writing),
        "伝書鳩が{0}宛にホメッセージを届けてきたよ！\n「 *{1}* 」\nと書いてあったよ！".format(_targets, prise_writing),
        "うちの犬が木の下で吠えててうるさい！もしかしてと思って掘ったら{0}宛の黄金のホメッセージが出てきたよ！\n「 *{1}* 」\nって書いてあったよ！".format(_targets, prise_writing),
        "ホメール文明の石碑に{0}宛のホメメッセージが記されている！どれどれ...\n「 *{1}* 」\nだって！文化遺産だね！".format(_targets, prise_writing),
        "ホメール神が{0}の\n「 *{1}* 」\nという善行に感動してたよ！".format(_targets, prise_writing),
        "{0}がいい子にしてたからサンタさんがプレゼント用意してたよ！\n「 *{1}* 」\nというのを見ていたんだって！".format(_targets, prise_writing),
        "チームメンバーがホメトークのホメたい芸人で{0}をホメていたよ！\n「 *{1}* 」\nというのを楽しそうに話していたよ！".format(_targets, prise_writing),
        "お出かけしていたら僕のところに非通知留守電が...怖いけど聞いてみよう...\n{0}へ\n「 *{1}* 」\n全然怖くないじゃん！".format(_targets, prise_writing),
        "{0}の\n「 *{1}* 」\nということをこっそりツイートしたら3万リツイートいっちゃったよ！\nバズったからホメとくを宣伝してきていいかな？".format(_targets, prise_writing),
        "始まりましたFMホメリアン！今日もホメッセージが届いております！\nラジオネーム : ホメラニアンさんから{0}さん宛に\n「 *{1}* 」\nと届いておりました！".format(_targets, prise_writing),
        "チームメンバーのパソコンに{0}宛に書きかけのホメッセージが残っていたよ！代わりに僕がホメちゃおう！\n「 *{1}* 」\n次は顔を見てホメられるといいね！".format(_targets, prise_writing),
        "近くの人が{0}宛にAirDropでホメッセージを送ってきたよ！\n「 *{1}* 」\n他の人も拾わないように早く切ってね！".format(_targets, prise_writing),
        "チームメンバーがwifiの名前を{0}にして，パスワードを\n「 *{1}* 」\nにしちゃったよ！気持ちが溢れすぎたね！".format(_targets, prise_writing),
        "こないだの土曜日，チームメンバーが\n「{0}さんへ， *{1}* ．ありがとう」\nって背中に書いてあるTシャツを着て外を歩いていたよ！\nもうそれ直接言った方が恥ずかしくないと思うよ！".format(_targets, prise_writing),
        "チームメンバーがブルーインパルスにお願いして\n「{0}さんへ， *{1}* 」\nって書いてもらってたよ！\nよく協力してもらえたね！".format(_targets, prise_writing),
        "花火大会で\n「{0}へ， *{1}* 」\nと書いた10寸玉が上がってたよ！".format(_targets, prise_writing)
    ]

    return _positive_phrase_list[random.randrange(0,len(_positive_phrase_list))]

# gifのURLをランダムで1つ返す
def random_gif_url():
    _gif_url_list = [
        "https://tenor.com/view/shiba-shiny-shiba-doggo-good-doggo-shiny-doggo-gif-16082089",
        "https://tenor.com/view/nanon-nanon-korapat-%e0%b8%99%e0%b8%99%e0%b8%99-%e0%b8%99%e0%b8%99%e0%b8%99%e0%b8%81%e0%b8%a3%e0%b8%a0%e0%b8%b1%e0%b8%97%e0%b8%a3%e0%b9%8c-hearts-gif-22124241",
        "https://tenor.com/view/shinegifs-gif-8555546",
        "https://tenor.com/view/kitty-highkitten-mdmacat-cat-happykitty-gif-6198981",
        "https://tenor.com/view/shaq-buffalo-wings-hot-ones-shaquille-oneal-shocked-gif-13728541",
        "https://tenor.com/view/dogs-cute-adorable-gif-13995631",
        "https://tenor.com/view/spongebob-squarepants-dance-happydance-gif-5027512",
        "https://tenor.com/view/my-happpy-dance-cute-shade-gif-15567340",
        "https://tenor.com/view/dancing-dance-twerk-jump-street-gif-5840882",
        "https://tenor.com/view/happy-mochi-gif-20079211",
    ]

    return _gif_url_list[random.randrange(0, len(_gif_url_list))]

# ホメられた人のIDをstrで返す関数
def get_targets_str(targets_id:str):
    _targets_str:str = ""
    
    for target in targets_id:
        _targets_str += "<@{0}>".format(target)

    return _targets_str

# ホメられ度によってテキストとgifを返す関数
def get_last_text(clap_num:int, targets_id:str):
	_targets_str = get_targets_str(targets_id)
	_clap_num = clap_num
	_last_text:str = ""
	_gif_url:str = ""

	if _clap_num < 2:
		_last_text = "いいですね〜{0}\n\nその調子！！".format(_targets_str)
		_gif_url = "https://tenor.com/view/shaq-buffalo-wings-hot-ones-shaquille-oneal-shocked-gif-13728541"
	elif _clap_num < 5:
		_last_text = "素敵！:sparkles::sparkles:\n\n{0}は今日も輝いてる:sparkles::sparkles:\n\n眩しすぎて目が開けられないよ！:dizzy_face:".format(_targets_str)
		_gif_url = "https://tenor.com/view/aplauso-superholly-buen-hecho-muy-bien-celebrar-gif-22174395"
	elif _clap_num < 7:
		_last_text = "すごい！:hushed:\n\n{0}は絶好調だね:+1::+1:\n\nこの調子でどんどん進めていこう:muscle::muscle:".format(_targets_str)
		_gif_url = "https://tenor.com/view/two-thumbs-up-bravo-nice-happy-smile-gif-8782543"
	elif _clap_num < 9:
		_last_text = "最高のチームメンバーだ！！:clap::clap:\n\nこれは表彰ものだね！:clap::clap:"
		_gif_url = "https://tenor.com/view/standing-ovation-applause-yes-gif-4982332"
	else:
		_last_text = "これはとんでもなく褒められてますよ:bangbang::bangbang:\n\n過去1かもしれません:bangbang::bangbang:\n\n{0}はみんなの誇りだね:bangbang:".format(_targets_str)
		_gif_url = "https://tenor.com/view/surprise-chris-pratt-parks-and-recreation-parks-and-rec-shocked-gif-5571450"

	return _last_text, _gif_url