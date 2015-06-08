#coding:utf-8
import MeCab
from cmath import *
sentence_list = ["Ruby は当初1993年2月24日に生まれ、1995年12月にfj上で発表された。名称の Ruby は、プログラミング言語 Perl が6月の誕生石である Pearl（真珠）と同じ発音をすることから、まつもとの同僚の誕生石（7月）のルビーを取って名付けられた。 機能として、クラス定義、ガベージコレクション、強力な正規表現処理、マルチスレッド、例外処理、イテレータ、クロージャ、Mixin、演算子オーバーロードなどがある。Perl を代替可能であることが初期の段階から重視されている。Perlと同様にグルー言語としての使い方が可能で、C言語プログラムやライブラリを呼び出す拡張モジュールを組み込むことができる。 Ruby 処理系は、主にインタプリタとして実装されている（詳しくは#実装を参照）。 可読性を重視した構文となっている。Ruby においては整数や文字列なども含めデータ型はすべてがオブジェクトであり、純粋なオブジェクト指向言語といえる。 長らく言語仕様が明文化されず、まつもとによる実装が言語仕様に準ずるものとして扱われて来たが、2010年6月現在、JRuby や Rubinius といった互換実装の作者を中心に機械実行可能な形で明文化する RubySpec という試みが行われている。公的規格としては2011年3月22日にJIS規格（JIS X 3017）が制定され、その後2012年4月1日に日本発のプログラム言語では初めてISO/IEC規格（ISO/IEC 30170）として承認された [3]。 フリーソフトウェアとしてバージョン1.9.2までは Ruby ライセンス（Ruby License や Ruby'sと表記されることもある。GPLかArtisticに似た独自ライセンスを選択するデュアルライセンス。）で配布されていたが、バージョン1.9.3以降は2-clause BSDLで配布されている。","Python（パイソン）は、広く使用されている汎用のプログラミング言語である。コードのリーダビリティが高くなるように言語が設計されていると主張され、その構文のおかげで、Cなどの言語に比べて、より少ないコード行数でプログラムを表現できる[13][14]と主張されている。小規模なプログラムから大規模なプログラムまで、さまざまなプログラムをクリアに書けるように、多くのコードが提供されている[15]。 Pythonは複数のプログラミングパラダイムをサポートしており、オブジェクト指向、命令型、手続き型、関数型などのスタイルでプログラムを書くことができる。Pythonは動的型付け言語であり、参照カウントベースの自動メモリ管理（ガベージコレクタ）を持つ。さまざまな領域をカバーする大規模な標準ライブラリを提供している[16]。 Pythonは、汎用のプログラミング言語として設計されており、標準ライブラリやサードパーティ製のライブラリも充実している。そのためPythonはWebアプリケーションやデスクトップアプリケーションなどの開発はもとより、システム用のスクリプトや、各種の自動処理、理工学や統計解析のためのツールとしてなど、幅広い領域で使用されている。 Pythonのリファレンス実装であるCPythonは、フリーかつオープンソースのソフトウェアであり、コミュニティベースの開発モデルを採用している。CPythonは、非営利団体であるPythonソフトウェア財団が管理している。その他の実装としては、PyPyやIronPythonなどが有名である。 Pythonは、オランダ人のグイド・ヴァンロッサムによって開発された。名前の由来は、イギリスのテレビ局 BBC が製作したコメディ番組『空飛ぶモンティ・パイソン』であるが、Pythonという英単語が意味する爬虫類のニシキヘビがPython言語のマスコットやアイコンとして使われることがある。","Java（ジャバ）は、狭義ではオブジェクト指向プログラミング言語Javaであり、広義ではプログラミング言語Javaのプログラムの実行環境および開発環境をいう。本稿ではプログラミング言語としての Java、および関連する技術や設計思想、およびJava言語の実行環境として見たJavaプラットフォームについて解説する。クラスライブラリなどを含めた、Javaバイトコードの実行環境と開発環境（広義のJava）については、Javaプラットフォームを参照。また、言語の文法に関してはJavaの文法を参照。"]

tagger = MeCab.Tagger()
tf_list = []
for sentence in sentence_list:
  result = tagger.parse(sentence)
  wordCount = {}
  wordTF = {}
  wordList = result.split()[:-1:2]
  allWordCount = 0
  for word in wordList:
    wordCount.setdefault(word, 0)
    wordCount[word]+= 1
    allWordCount += 1
  for word,count in wordCount.items():
    wordTF[word] = count*1.0/allWordCount
  tf_list.append(wordTF)
df_list = {}
for tf in tf_list:
  for word, tf_value in tf.items():
    df_list.setdefault(word, 0)
    df_list[word] += 1

tf_idf_value_list = []
count = 1
for tf in tf_list:
  tf_idf_value = {}
  for word, tf_value in tf.items():
    tf_idf_value[word] = tf_value * float(log(len(sentence_list)*1.0/df_list[word]).real)
  print '文書%dのキーワード' % (count)
  count += 1
  limit = 0
  for word, value in sorted(tf_idf_value.items(), key=lambda x:x[1],reverse=True):
    print '%-16s %f' % (word, value)
    limit += 1
    if limit == 10:
      break


