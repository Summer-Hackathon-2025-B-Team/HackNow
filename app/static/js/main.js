
// ハックマンの一言モーダル（base.html）
document.addEventListener("DOMContentLoaded", function() {
    const quotes = [
        "学べば学ぶほど、自分がどれだけ無知であるか思い知らされる。自分の無知に気づけば気づくほど、より一層学びたくなる。（by アインシュタイン）",
        "人間はやり通す力があるかないかによってのみ、称賛または非難に値する。（by レオナルド・ダ・ヴィンチ）",
        "最も高い目標を達成するには、一歩一歩進むしかないという事実を、頭に入れておかなければならない。（by アンドリュー・カーネギー）",
        "天才なんかあるものか。僕は他人がコーヒーを飲んでいる時間に仕事をしただけだ。（by 魯迅）",
        "早い時間に始めて遅くまで残っていた。来る日も来る日も、来る年も来る年も。一夜にして成功するのに17年と114日もかかったよ。（by リオネル・メッシ）",
        "未来は今日何をするかによって決まる。（by ガンジー）",
        "「Stay hungry, stay foolish（貪欲であれ、愚か者であれ）」（by スティーブ・ジョブズ）",
        "常に新しいことを学び、謙虚であれ（by ウォーレン・バフェット）",
    ];

    const img = document.getElementById("motivation-img");
    const modalText = document.getElementById("modal-text");
    const motivationModal = new bootstrap.Modal(document.getElementById('motivationModal'));

    img.addEventListener("click", function() {
        const randomQuote = quotes[Math.floor(Math.random() * quotes.length)];
        modalText.textContent = randomQuote;
        motivationModal.show();
    });
});


// 日報提出トレースモーダル（base.html）
document.addEventListener('DOMContentLoaded', function() {

    // モーダルを表示する時間（24時間表記）
    const targetHour = 12;
    const targetMinute = 40;

    // 今日の日付 (例: "2025-08-22")
    const today = new Date().toISOString().split("T")[0];

    // localStorageに保存された「最後に日報提出トレースモーダルを表示した日」を取得
    const lastShownDate = localStorage.getItem("modalShownDate");

    // 今日、表示していなければ監視を開始（表示していれば監視しない=当日中は表示されない）
    // if (lastShownDate !== today) {
    const timer = setInterval(() => {
        const now = new Date();
        if (now.getHours() === targetHour && now.getMinutes() === targetMinute) {
            showDailyReportTraceModal();

            // 今日表示したことを記録
            localStorage.setItem("modalShownDate", today);

            // 一度表示したら監視停止
            clearInterval(timer);
        }
    }, 1000);
    // }

    function showDailyReportTraceModal() {

        // モーダルに表示するテキスト
        const quote = "夜遅くまでおつかれさまです！\nハッカソンを頑張りつつ、日報の提出も忘れずにお願いします！\n（ハッカソンでの学びをぜひアウトプットしましょう！）";

        // モーダルにテキストを表示する箇所を取得
        const modalText = document.getElementById("daily-report-trace-modal-text");

        // Bootstrapのモーダル機能をJSから使うためにインスタンス化
        const dailyReportTraceModal = new bootstrap.Modal(document.getElementById('daily-report-trace-modal'));

        modalText.innerHTML = quote.replace(/\n/g, "<br>");
        dailyReportTraceModal.show();

    }
});


// 削除ボタン押下時の処理（各種メニュー）

let deleteUrl = null;

// 削除確認モーダルの表示
function confirmDelete(itemId, url, name) {
    deleteUrl = url;
    document.getElementById('confirm-message').innerText = `「${name}」を削除しますか？`;
    document.getElementById('confirm-dialog').style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
}

// 削除確認モーダルで「No」を押下したときの処理（モーダルを非表示に）
function cancelDelete() {
    deleteUrl = null;
    document.getElementById('confirm-dialog').style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
}

// 削除確認モーダルで「Yes」を押下したときの処理（削除処理にルーティング）
function proceedDelete() {
    if (deleteUrl) {
        window.location.href = deleteUrl;
    }
}
