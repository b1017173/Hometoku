import random

#褒める文章を生成する関数
def random_positive(targets:list, prise_writing:str):
  _targets_str:str = ""
  for target in targets:
    _targets_str += "<@{0}>".format(target)
  
  _positiveList=[_targets_str+'さんへ\n「'+prise_writing+'」\n匿名さんより',
    _targets_str+'の素晴らしい活躍の噂話を聞きました!\n「'+prise_writing+'」らしいですよ！',
    _targets_str+'様．\n'+prise_writing+'という素晴らしい功績を残したため，チームメンバーよりここに賞する．',
    'シャイなチームメンバーから代わりに'+_targets_str+'をホメてって言われちゃった！\n「'+prise_writing+'」だって！凄いや！',
    'チームメンバーとタイムカプセルを掘りに行ったよ！\n'+_targets_str+'宛に「'+prise_writing+'」と書いてあったよ！',
    '伝書鳩が'+_targets_str+'宛にホメッセージを届けてきたよ！\n「'+prise_writing+'」と書いてあったよ！',
    'うちの犬が木の下で吠えててうるさい！もしかしてと思って掘ったら'+_targets_str+'宛の黄金のホメッセージが出てきたよ！\n「'+prise_writing+'」って書いてあったよ！',
    'ホメール文明の石碑に'+_targets_str+'宛の褒メッセージが記されている！\nどれどれ...「'+prise_writing+'」だって！文化遺産だね！',
    'ホメール神が'+_targets_str+'の「'+prise_writing+'」という善行に感動してたよ！',
    _targets_str+'がいい子にしてたからサンタさんがプレゼント用意してたよ！\n「'+prise_writing+'」というのを見ていたんだって！',
    'チームメンバーがホメトークのホメたい芸人で'+_targets_str+'をホメていたよ！\n「'+prise_writing+'」というのを楽しそうに話していたよ！',
    'お出かけしていたら僕のところに非通知留守電が...怖いけど聞いてみよう...\n'+_targets_str+'へ「'+prise_writing+'」\n全然怖くないじゃん！',
    _targets_str+'の「'+prise_writing+'」ということをこっそりツイートしたら3万リツイートいっちゃったよ！\nバズったからホメとく宣伝してきていいかな？'
    '始まりましたFMホメリアン！今日もホメッセージが届いております！\nラジオネーム : ホメラニアンさんから'+_targets_str+'さん宛に「'+prise_writing+'」と届いておりました！',
    'チームメンバーのパソコンに'+_targets_str+'宛に書きかけのホメッセージが残っていたよ！代わりに僕がホメちゃおう！\n「'+prise_writing+'」\n次は顔を見てホメられるといいね！',
    '近くの人が'+_targets_str+'宛にAirDropでホメッセージを送ってきたよ！\n「'+prise_writing+'」\n他の人も拾わないように早く切ってね！',
    'チームメンバーがwifiの名前を'+_targets_str+'にして，パスワードを「'+prise_writing+'」にしちゃったよ！\n気持ちが溢れすぎたね！',
    'こないだの土曜日，チームメンバーが「'+_targets_str+'さんへ，'+prise_writing+'．ありがとう」って背中に書いてあるTシャツを着て外を歩いていたよ！\nもうそれ直接言った方が恥ずかしくないと思うよ！',
    'チームメンバーがブルーインパルスにお願いして「'+_targets_str+'さんへ，'+prise_writing+'」って書いてもらってたよ！\nよく協力してもらえたね！',
    '花火大会で「'+_targets_str+'へ，'+prise_writing+'」と書いた10寸玉が上がってたよ！']

  return _positiveList[random.randrange(0,len(_positiveList))] 