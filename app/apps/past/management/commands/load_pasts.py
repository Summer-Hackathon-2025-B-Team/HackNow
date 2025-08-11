from django.core.management.base import BaseCommand
from apps.past.models import Past

class Command(BaseCommand):
    help = '過去ハッカソンデータを一括投入します'

    def handle(self, *args, **options):
        # 過去ハッカソンデータ
        pasts_data = [
            Past(category="学習支援",name="IT 英単語",description="ITに関する英語をクイズ形式で学習するアプリ\n英単語の発音も確認できる",url="https://raretech.site/dashboard/lesson/archive/456",start_time="1:18:20～"),
            Past(category="学習支援",name="RareTECH Love",description="別ツールでやり取りしている質問・回答を一覧で参照できるアプリ\nキーワードや質問者での検索も可能",url="https://raretech.site/dashboard/lesson/archive/456",start_time="49:10～"),
            Past(category="学習支援",name="想起アプリ（仮）",description="RareTECHで学んだ内容を元に作問するアプリ\n問題に参考URLをつけることができ、知識拡充可能",url="https://raretech.site/dashboard/lesson/archive/456",start_time="20:20～"),
            Past(category="タスク管理",name="-",description="Flaskを利用したシンプルなTodo管理アプリ\nチームで参考記事を読み込み、不明点を整理",url="https://raretech.site/dashboard/lesson/archive/456",start_time="05:00～"),
            Past(category="その他",name="あんちてーぜ！",description="Todo管理/タイピングゲーム/ブックレビューができるアプリ\nメンバーが作りたいものを詰め込んだアプリ",url="https://raretech.site/dashboard/lesson/archive/474",start_time="1:28:00～"),
            Past(category="日記管理",name="守屋の秘訣日記",description="守屋さんの美の秘訣を紹介するブログアプリ\n簡単に記事投稿できる",url="https://raretech.site/dashboard/lesson/archive/474",start_time="1:11:20～"),
            Past(category="情報収集",name="REAL",description="RareTECH生のツイートだけを表示するアプリ\nTwitterのAPIを利用して情報取得",url="https://raretech.site/dashboard/lesson/archive/474",start_time="52:40～"),
            Past(category="学習支援",name="ITお絵描きゲーム",description="与えられたお題（IT用語）について画面上に図を書くアプリ\n複数人でゲーム参加し、何の絵か当てたらポイント",url="https://raretech.site/dashboard/lesson/archive/474",start_time="24:00～"),
            Past(category="学習支援",name="Niqiita",description="IT用語の解説投稿アプリ\nいい投稿には「いいね」をつけられるようにする想定",url="https://raretech.site/dashboard/lesson/archive/474",start_time="04:10～"),
            Past(category="学習支援",name="ITクロスワード",description="IT用語を使ったクロスワードアプリ\n難易度を選択可能（難易度が高いほど文字数が多くなる）",url="https://raretech.site/dashboard/lesson/archive/535",start_time="1:31:10～"),
            Past(category="学習支援",name="Rare Study Calendar",description="カレンダーにTodo機能を実装したアプリ\nRareTECH受講生の学習進捗を可視化",url="https://raretech.site/dashboard/lesson/archive/535",start_time="54:50～"),
            Past(category="学習支援",name="てっくらんど",description="キッズ向けIT学習アプリ\n学習用のクイズを出題し、正解するとポイント加算",url="https://raretech.site/dashboard/lesson/archive/535",start_time="27:30～"),
            Past(category="チャット",name="RareTECH掲示板",description="いつでもどこにいてもコアな話ができる掲示板アプリ\n簡単に掲示板作成やスレッド投稿ができる",url="https://raretech.site/dashboard/lesson/archive/535",start_time="03:20～"),
            Past(category="学習支援",name="TYPING EQ",description="正確性と速さが結果表示されるタイピングアプリ\nタイピング中はキーボード入力が可視化される",url="https://raretech.site/dashboard/lesson/archive/606",start_time="1:45:30～"),
            Past(category="チャット",name="ChaChat",description="気軽にテーマを決めてルーム作成できるチャットアプリ\nエンジニア同士のつながりを活性化させる",url="https://raretech.site/dashboard/lesson/archive/606",start_time="1:24:00～"),
            Past(category="趣味関係",name="Recommend Location",description="フォロワー間でおすすめの場所を紹介しあえるアプリ\nGoogleMapにピン刺しして場所を明示",url="https://raretech.site/dashboard/lesson/archive/606",start_time="57:40～"),
            Past(category="学習支援",name="Cタイピング",description="エンジニア用のタイピングアプリ\nコマンドをタイピング",url="https://raretech.site/dashboard/lesson/archive/606",start_time="46:20～"),
            Past(category="学習支援",name="Wordarium",description="言語化した内容の投稿・共有アプリ\n言語化すると星になって鑑賞できる",url="https://raretech.site/dashboard/lesson/archive/606",start_time="24:30～"),
            Past(category="開発支援",name="-",description="マウス操作なしでフローチャートを作成するアプリ\nキーボード操作でチャートを作成",url="https://raretech.site/dashboard/lesson/archive/606",start_time="06:30～"),
            Past(category="チャット",name="DocoIco",description="カレンダー付きチャットアプリ\nチャット画面からカレンダーを開ける",url="https://raretech.site/dashboard/lesson/archive/664",start_time="1:46:20～"),
            Past(category="学習支援",name="Blearn",description="文章から特定の単語を隠して勉強できるアプリ\nカテゴリを分けて作問可能",url="https://raretech.site/dashboard/lesson/archive/664",start_time="1:30:30～"),
            Past(category="チャット",name="MOSS Chat",description="ITエンジニア同士で気軽にやり取りできるチャットアプリ\n不適切な言葉を防ぐ仕組み（注意喚起・チェック）を構築",url="https://raretech.site/dashboard/lesson/archive/664",start_time="1:13:30～"),
            Past(category="チャット",name="Ring",description="人とのつながりをコンセプトにしたチャットアプリ\nお気に入り機能やリアクション機能を実装",url="https://raretech.site/dashboard/lesson/archive/664",start_time="58:10～"),
            Past(category="趣味関係",name="くらべてみなイカ？",description="スプラトゥーン用の装備比較アプリ\n検索時間の短縮を目的に作成",url="https://raretech.site/dashboard/lesson/archive/664",start_time="36:20～"),
            Past(category="チャット",name="E CHATT",description="情報の変更内容がわかるチャットアプリ\nRepost機能による過去投稿の引用・変更点の強調が可能",url="https://raretech.site/dashboard/lesson/archive/664",start_time="05:30～"),
            Past(category="関係構築支援",name="PairLeary",description="RareTECH生向けのコミュニケーション支援アプリ\nマッチング機能により他受講生とやり取りしやすくなる",url="https://raretech.site/dashboard/lesson/archive/697",start_time="1:40:30～"),
            Past(category="チャット",name="POP.",description="明るく親しみやすいをコンセプトにしたチャットアプリ\nリアクション機能や写真貼り付け機能の実装を想定",url="https://raretech.site/dashboard/lesson/archive/697",start_time="1:25:20～"),
            Past(category="チャット",name="Footchar",description="サッカー観戦を盛り上げるためのアプリ\nチャンネルに複数タグを紐づけ可能",url="https://raretech.site/dashboard/lesson/archive/697",start_time="1:12:40～"),
            Past(category="学習支援",name="-",description="かるたを通じてゲーム感覚でコマンドを覚えるアプリ\n表示される問題・札は毎回ランダムで変わる",url="https://raretech.site/dashboard/lesson/archive/697",start_time="59:30～"),
            Past(category="読書支援",name="LIFE",description="所有する本、購入代金を管理するアプリ\n本の登録はバーコード読み取り等で実現",url="https://raretech.site/dashboard/lesson/archive/697",start_time="39:40～"),
            Past(category="チャット",name="TabiComi",description="都道府県別にグループ作成できるチャットアプリ\nチャット名の編集・削除も可能",url="https://raretech.site/dashboard/lesson/archive/697",start_time="25:00～"),
            Past(category="チャット",name="LETAT",description="招待制のグループチャットアプリ\n人がスマホを触りだす時間帯（夕方）をコンセプトにデザイン",url="https://raretech.site/dashboard/lesson/archive/697",start_time="09:40～"),
            Past(category="チャット",name="Stlive",description="タスク管理もできるチャットアプリ\n下書きや定型文を挿入できる",url="https://raretech.site/dashboard/lesson/archive/697",start_time="00:00～"),
            Past(category="チャット",name="sou∞zou",description="夢やタスク登録もできるチャットアプリ\nシンプルで直感的なデザイン",url="https://raretech.site/dashboard/lesson/archive/718",start_time="1:26:00～"),
            Past(category="タスク管理",name="こつこつ",description="タスクの継続補助アプリ\n積み重ねた結果を可視化してモチベーション向上",url="https://raretech.site/dashboard/lesson/archive/718",start_time="1:07:30～"),
            Past(category="不動産管理",name="Real Estate360",description="不動産会社向け物件管理アプリ\nプルダウンで入力を簡素化",url="https://raretech.site/dashboard/lesson/archive/718",start_time="52:30～"),
            Past(category="チャット",name="WADACHI",description="勉強のモチベを高めるチャットアプリ\n他者の学習記録と目標を閲覧可能",url="https://raretech.site/dashboard/lesson/archive/718",start_time="37:30～"),
            Past(category="教育支援",name="Createst",description="テスト問題生成アプリ\n生成AIにキーワードを与え、自動で作問",url="https://raretech.site/dashboard/lesson/archive/718",start_time="23:50～"),
            Past(category="チャット",name="neeeeche処",description="ニッチな商品のレビューアプリ\nチャンネル名やメッセージ文言での検索が可能",url="https://raretech.site/dashboard/lesson/archive/718",start_time="12:00～"),
            Past(category="チャット",name="EarlyBird",description="Mattermost風のデザインのチャットアプリ\nレスポンシブ対応も具備",url="https://raretech.site/dashboard/lesson/archive/718",start_time="00:00～"),
            Past(category="チャット",name="NOTE.",description="チャット内で共有ノートを作るアプリ\n個人・グループ・パブリックのチャットを分割管理",url="https://raretech.site/dashboard/lesson/archive/746",start_time="1:25:50～"),
            Past(category="チャット",name="Tech Talk",description="RareTECH生が気軽にチャットできるアプリ\nパスワード再設定機能も具備",url="https://raretech.site/dashboard/lesson/archive/746",start_time="1:08:10～"),
            Past(category="生活支援",name="antoquino",description="料理レシピ備忘録アプリ\nレシピをコツコツ登録することで献立を決めやすくなる",url="https://raretech.site/dashboard/lesson/archive/746",start_time="52:50～"),
            Past(category="チャット",name="Bloom",description="メッセージのハードルを下げるチャットアプリ\nメッセージ送信すると花が育つなど工夫",url="https://raretech.site/dashboard/lesson/archive/746",start_time="28:30～"),
            Past(category="チャット",name="申請くん",description="備品や施設の利用申請に使うチャットアプリ\n利用申請フォームも具備",url="https://raretech.site/dashboard/lesson/archive/746",start_time="12:50～"),
            Past(category="チャット",name="CREW",description="社員同士で使うチャットアプリ\nTodo管理も可能",url="https://raretech.site/dashboard/lesson/archive/746",start_time="00:00～"),
            Past(category="開発支援",name="Basis",description="管理・設計に関するドキュメントを一元管理するアプリ\nテンプレートを用意し、円滑に設計書作成可能",url="https://raretech.site/dashboard/lesson/archive/782",start_time="1:26:10～"),
            Past(category="チャット",name="Petalk",description="ペットシッターとのチャットアプリ\n女性向けでデザインに特色あり",url="https://raretech.site/dashboard/lesson/archive/782",start_time="1:14:00～"),
            Past(category="チャット",name="DESIGN GREAT",description="教員と生徒で使うチャットアプリ\nコメントのピン留め機能やリアクション機能を実装",url="https://raretech.site/dashboard/lesson/archive/782",start_time="1:02:30～"),
            Past(category="チャット",name="Chat app",description="シンプルで使いやすいチャットアプリ\nAWS構成パターンを複数用意し、可用性やコストの観点で検討",url="https://raretech.site/dashboard/lesson/archive/782",start_time="41:10～"),
            Past(category="教育支援",name="チャプたん",description="RareTECH講義動画のチャプター自動生成アプリ\n文字起こし＋AIを使ってチャプター作成",url="https://raretech.site/dashboard/lesson/archive/782",start_time="26:50～"),
            Past(category="チャット",name="OASIS HUB",description="ハッカソン開発でチームメンバーと使えるチャットアプリ\n「集まれ」ボタンでメンバー招集（メール通知）",url="https://raretech.site/dashboard/lesson/archive/782",start_time="12:40～"),
            Past(category="タスク管理",name="What to do, to live me?",description="最低限の機能を持つTodo管理アプリ\n新技術を試す目的で実施",url="https://raretech.site/dashboard/lesson/archive/782",start_time="2:20～"),
            Past(category="生活支援",name="ツーガック",description="子どもの通学グループの欠席連絡・出欠席管理アプリ\n欠席連絡、欠席確認を簡易的に実施できる",url="https://raretech.site/dashboard/lesson/archive/786",start_time="1:34:10～"),
            Past(category="チャット",name="ぐーたらちゃっと",description="面倒くさがりな人でも気軽にチャットできるアプリ\n定型文登録により文字入力を簡略化",url="https://raretech.site/dashboard/lesson/archive/786",start_time="1:21:40～"),
            Past(category="タスク管理",name="Narra Belle",description="todo管理アプリ\ntodoをカードに見立て、直感的に配置可能",url="https://raretech.site/dashboard/lesson/archive/786",start_time="1:09:00～"),
            Past(category="チャット",name="CLUB CHAT",description="部活動をしているメンバー間で使うアプリ\n学年ごとのルームなど、複数ルームの作成が可能",url="https://raretech.site/dashboard/lesson/archive/786",start_time="45:30～"),
            Past(category="チャット",name="人の腹見て我が腹直せ。",description="インストラクターとチャットできるアプリ\n体重変化をグラフで可視化",url="https://raretech.site/dashboard/lesson/archive/786",start_time="28:30～"),
            Past(category="生活支援",name="Cook Keep",description="レシピ情報を一元管理できるアプリ\nキーワードやタグでレシピ検索可能",url="https://raretech.site/dashboard/lesson/archive/786",start_time="16:50～"),
            Past(category="学習支援",name="Linkey",description="問題作成・共有アプリ\n解説文を生成AIに作ってもらえる機能あり",url="https://raretech.site/dashboard/lesson/archive/786",start_time="2:50～"),
            Past(category="チャット",name="Our Language",description="話せる言語と学びたい言語が逆の人とチャットするアプリ\n学びたい言語で送信しないとエラーになる仕組み",url="https://raretech.site/dashboard/lesson/archive/836",start_time="1:21:40～"),
            Past(category="読書支援",name="Yomitai",description="読書習慣を身につけるためのアプリ\n読書記録を残したり表彰機能によるモチベ維持が可能",url="https://raretech.site/dashboard/lesson/archive/836",start_time="1:05:20～"),
            Past(category="健康支援",name="ちょこログ",description="ちょっとした運動の記録アプリ\n運動記録（スタンプ）を見返すことでモチベ維持が可能",url="https://raretech.site/dashboard/lesson/archive/836",start_time="48:20～"),
            Past(category="生活支援",name="買いもっと",description="買い物リスト作成アプリ\nLINEと連携し、LINEアカウントでのログインや買い忘れ通知が可能",url="https://raretech.site/dashboard/lesson/archive/836",start_time="19:00～"),
            Past(category="学習支援",name="TECH-LIBRA",description="本の貸し借りができるプラットフォームアプリ\n配送サービスとの連携を想定",url="https://raretech.site/dashboard/lesson/archive/836",start_time="00:00～"),
            Past(category="旅行関係",name="TRiP TRAIL",description="旅行先の経路などを一元管理するアプリ\nGoogleMapと連携して経路情報を取得",url="https://raretech.site/dashboard/lesson/archive/845",start_time="42:30～"),
            Past(category="学習支援",name="NICCA SAURUS",description="自己研鑽を日課にするためのサポートアプリ\n日課登録・進捗管理し、日課をこなすと恐竜が成長する",url="https://raretech.site/dashboard/lesson/archive/845",start_time="27:40～"),
            Past(category="関係構築支援",name="-",description="Good & New（直近あった良かったこと）の共有アプリ\nチャットツール（slack）と連携して入力・配信",url="https://raretech.site/dashboard/lesson/archive/845",start_time="14:40～"),
            Past(category="旅行関係",name="Travelers Album",description="旅行記録を残すアプリ\n写真の場所（座標）を管理し、GoogleMapにピン刺し可能",url="https://raretech.site/dashboard/lesson/archive/845",start_time="00:00～"),
            Past(category="学習支援",name="Wakarun",description="問題作成・共有ができるアプリ\n問題をお気に入り登録して繰り返し解くことができる",url="https://raretech.site/dashboard/lesson/archive/864",start_time="1:11:20～"),
            Past(category="健康支援",name="ほぐしーの",description="健康促進につながる動画を配信するアプリ\n過去動画も遡って見直し可能",url="https://raretech.site/dashboard/lesson/archive/864",start_time="51:30～"),
            Past(category="趣味関係",name="Fantre",description="グッズ情報の管理アプリ\nグッズの登録や検索ができる",url="https://raretech.site/dashboard/lesson/archive/864",start_time="35:00～"),
            Past(category="学習支援",name="Fucabo",description="生成AIを効率的に利用できるアプリ\n異なるAIの回答比較や回答の保存（マイ辞書機能）ができる",url="https://raretech.site/dashboard/lesson/archive/864",start_time="17:30～"),
            Past(category="学習支援",name="RareCHECK",description="選択問題の実施、作成（他者と共有可）ができるアプリ\n学習記録をグラフで可視化",url="https://raretech.site/dashboard/lesson/archive/864",start_time="00:00～"),
            Past(category="学習支援",name="Skill Typing",description="技術用語学習タイピングアプリ\n問題生成はAIを活用",url="https://raretech.site/dashboard/lesson/archive/877",start_time="1:51:20～"),
            Past(category="教育支援",name="作問くん",description="テスト作成アプリ\n直感的にわかりやすくテスト作成できる",url="https://raretech.site/dashboard/lesson/archive/877",start_time="1:32:20～"),
            Past(category="学習支援",name="efFEctive",description="基本情報技術者試験の学習支援アプリ\nユーザの理解度に合わせた問題提供",url="https://raretech.site/dashboard/lesson/archive/877",start_time="1:18:40～"),
            Past(category="学習支援",name="-",description="ポモドーロタイマーアプリ\n学習時間の計測・記録・グラフでの可視化",url="https://raretech.site/dashboard/lesson/archive/877",start_time="1:02:30～"),
            Past(category="情報収集",name="RareTicle",description="複数プラットフォーム（ZennやQuiita）から記事取得するアプリ\nお気に入り登録して読みたい記事を一元管理",url="https://raretech.site/dashboard/lesson/archive/877",start_time="52:20～"),
            Past(category="学習支援",name="StydyHub",description="学習場所検索(googlemapと連携)＋学習管理アプリ\nポモドーロタイマーの設定も可能",url="https://raretech.site/dashboard/lesson/archive/877",start_time="40:00～"),
            Past(category="生活支援",name="Wasurenu",description="日用品・調味料の買い忘れ防止アプリ\n賞味期限や次回購入日なども可視化",url="https://raretech.site/dashboard/lesson/archive/877",start_time="26:50～"),
            Past(category="情報収集",name="TechHub",description="RareTECHの投稿記事をまとめて参照できるアプリ\nメンバーごとの投稿記事一覧を参照することも可能",url="https://raretech.site/dashboard/lesson/archive/877",start_time="12:30～"),
            Past(category="タスク管理",name="FiniteDays",description="タスク管理と目標達成のサポートアプリ\n人生の残り時間を可視化し、モチベーションを向上させる",url="https://raretech.site/dashboard/lesson/archive/877",start_time="00:30～"),
            Past(category="日記管理",name="ハレの日日記",description="グループで写真付き日記を共有するアプリ\nカレンダーと紐づくので思い出を振り返りやすい",url="https://raretech.site/dashboard/lesson/archive/892",start_time="1:01:10～"),
            Past(category="学習支援",name="LinuQz",description="Linuxコマンド学習アプリ\nLinuxコマンドに関するクイズ（選択式・記述式）を実施",url="https://raretech.site/dashboard/lesson/archive/892",start_time="49:50～"),
            Past(category="生活支援",name="うちのごはん会議",description="グループで食べたいものを共有するアプリ\n食べたいレシピの登録や投票が可能",url="https://raretech.site/dashboard/lesson/archive/892",start_time="28:50～"),
            Past(category="生活支援",name="Kaji suke",description="家事のスケジュール管理アプリ\n繰り返し設定や残タスクの可視化が可能",url="https://raretech.site/dashboard/lesson/archive/892",start_time="14:30～"),
            Past(category="日記管理",name="さぶちゃん日記",description="日記投稿アプリ\n投稿するとキャラクターに応じたフィードバックをもらえる",url="https://raretech.site/dashboard/lesson/archive/892",start_time="00:00～"),
        ]

        try:
            # 既存データをクリア（必要に応じて）
            Past.objects.all().delete()

            # 一括投入実行
            Past.objects.bulk_create(pasts_data, ignore_conflicts=True)

            self.stdout.write(
                self.style.SUCCESS(f'{len(pasts_data)}件の過去ハッカソンデータを投入しました')
            )

        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'エラーが発生しました: {e}')
            )
