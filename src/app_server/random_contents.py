import random

#褒める文章を生成する関数
def random_positive(targets:list, prise_writing:str):
    _targets_str:str = ""
    for target in targets:
        _targets_str += "<@{0}>".format(target)
  
    _positive_phrase_list = [
        "{0}さんへ\n「 *{1}* 」\n匿名さんより".format(_targets_str, prise_writing),
        "{0}の素晴らしい活躍の噂話を聞きました!\n「 *{1}* 」らしいですよ！".format(_targets_str, prise_writing),
        "{0}様．\n *{1}* という素晴らしい功績を残したため，チームメンバーよりここに賞する．".format(_targets_str, prise_writing),
        "シャイなチームメンバーから代わりに{0}をホメてって言われちゃった！\n「 *{1}* 」だって！凄いや！".format(_targets_str, prise_writing),
        "チームメンバーとタイムカプセルを掘りに行ったよ！\n{0}宛に「 *{1}* 」と書いてあったよ！".format(_targets_str, prise_writing),
        "伝書鳩が{0}宛にホメッセージを届けてきたよ！\n「 *{1}* 」と書いてあったよ！".format(_targets_str, prise_writing),
        "うちの犬が木の下で吠えててうるさい！もしかしてと思って掘ったら{0}宛の黄金のホメッセージが出てきたよ！\n「 *{1}* 」って書いてあったよ！".format(_targets_str, prise_writing),
        "ホメール文明の石碑に{0}宛の褒メッセージが記されている！\nどれどれ...「 *{1}* 」だって！文化遺産だね！".format(_targets_str, prise_writing),
        "ホメール神が{0}の「 *{1}* 」という善行に感動してたよ！".format(_targets_str, prise_writing),
        "{0}がいい子にしてたからサンタさんがプレゼント用意してたよ！\n「 *{1}* 」というのを見ていたんだって！".format(_targets_str, prise_writing),
        "チームメンバーがホメトークのホメたい芸人で{0}をホメていたよ！\n「 *{1}* 」というのを楽しそうに話していたよ！".format(_targets_str, prise_writing),
        "お出かけしていたら僕のところに非通知留守電が...怖いけど聞いてみよう...\n{0}へ「 *{1}* 」\n全然怖くないじゃん！".format(_targets_str, prise_writing),
        "{0}の「 *{1}* 」ということをこっそりツイートしたら3万リツイートいっちゃったよ！\nバズったからホメとく宣伝してきていいかな？".format(_targets_str, prise_writing),
        "始まりましたFMホメリアン！今日もホメッセージが届いております！\nラジオネーム : ホメラニアンさんから{0}さん宛に「 *{1}* 」と届いておりました！".format(_targets_str, prise_writing),
        "チームメンバーのパソコンに{0}宛に書きかけのホメッセージが残っていたよ！代わりに僕がホメちゃおう！\n「 *{1}* 」\n次は顔を見てホメられるといいね！".format(_targets_str, prise_writing),
        "近くの人が{0}宛にAirDropでホメッセージを送ってきたよ！\n「 *{1}* 」\n他の人も拾わないように早く切ってね！".format(_targets_str, prise_writing),
        "チームメンバーがwifiの名前を{0}にして，パスワードを「 *{1}* 」にしちゃったよ！\n気持ちが溢れすぎたね！".format(_targets_str, prise_writing),
        "こないだの土曜日，チームメンバーが「{0}さんへ， *{1}* ．ありがとう」って背中に書いてあるTシャツを着て外を歩いていたよ！\nもうそれ直接言った方が恥ずかしくないと思うよ！".format(_targets_str, prise_writing),
        "チームメンバーがブルーインパルスにお願いして「{0}さんへ， *{1}* 」って書いてもらってたよ！\nよく協力してもらえたね！".format(_targets_str, prise_writing),
        "花火大会で「{0}へ， *{1}* 」と書いた10寸玉が上がってたよ！".format(_targets_str, prise_writing)
    ]

    return _positive_phrase_list[random.randrange(0,len(_positive_phrase_list))] 

# gifのURLをランダムで1つ返す
def random_gif_url():
    _gif_url_list = [
        "https://tenor.com/view/omg-simon-cowell-americas-got-talent-oh-my-wide-eyes-gif-22145587",
        "https://tenor.com/view/nanon-nanon-korapat-%e0%b8%99%e0%b8%99%e0%b8%99-%e0%b8%99%e0%b8%99%e0%b8%99%e0%b8%81%e0%b8%a3%e0%b8%a0%e0%b8%b1%e0%b8%97%e0%b8%a3%e0%b9%8c-hearts-gif-22124241",
        "https://tenor.com/view/screaming-cat-staring-ahh-whaa-gif-18345319",
        "https://tenor.com/view/kitty-highkitten-mdmacat-cat-happykitty-gif-6198981",
        "https://tenor.com/view/hug-love-dog-dogs-bestfriend-gif-5746206",
        "https://tenor.com/view/dogs-cute-adorable-gif-13995631",
        "https://tenor.com/view/spongebob-squarepants-dance-happydance-gif-5027512",
        "https://tenor.com/view/my-happpy-dance-cute-shade-gif-15567340",
        "https://tenor.com/view/dancing-dance-twerk-jump-street-gif-5840882",
        "https://tenor.com/view/happy-mochi-gif-20079211",
    ]

    return _gif_url_list[random.randrange(0, len(_gif_url_list))]