class HtmlUtils {
    static QS(key) {
        // セレクタ
        const node = document.querySelector(key);
        if (node == null) return null;
        // 問い合わせフォームの確認画面ではhiddenになるため。
        if (node.getAttribute('type') == 'hidden') return null;
        return node;
    }
    static createSelectBox(node, options) {
        // セレクトボックスを作成
        const element = node.ownerDocument.createElement('select');
        element.length = options.length;
        for (var i = 0; i < options.length; i++){
            const item = options[i];
            element.options[i].text = item.text || item.value;
            element.options[i].value = item.value || item.text;
        }
        return element;
    }
    static val(key, value) {
        // 値を設定
        // key:Selector
        // value:value
        const node = HtmlUtils.QS(key);
        if (node == null) return;
        node.value = value;
    }
}

class Widgets {
    constructor() {
        this.createSelectBox('input[name="fez_place"]', AREA); // エリア名
        this.createSelectBox('input[name="fez_reporter_region"]', COUNTRIES); //通報者の国家名
        this.createSelectBox('input[name="fez_report_region"]', COUNTRIES); //違反者の国家名
    }
    createSelectBox(key, options) {
        // セレクトボックスを作成
        // key:Selector セレクトボックスを追加するための位置ヒントとして利用
        // option:Array optionタグ用
        // セレクトボックスを選択時に、input項目に反映
        const node = HtmlUtils.QS(key);
        if (node == null) return;
        
        const select = HtmlUtils.createSelectBox(node, options);
        // セレクトボックス => input項目への反映
        select.addEventListener('change', (event) => {
            node.value = event.currentTarget.value;
        }, false);
        node.parentNode.insertBefore(select, node.nextSibling);
    }
    setdefaultvalues() {
        // 問い合わせフォーム表示の初期設定値
        const now = new Date();
        //---------------------------------------------------------------
        // 【不具合のご報告】 フォーム
        //---------------------------------------------------------------
        // 年月日時
        HtmlUtils.val('select[name="trouble_date1"]', now.getFullYear());
        HtmlUtils.val('select[name="trouble_date2"]', now.getMonth() + 1);
        HtmlUtils.val('select[name="trouble_date3"]', now.getDate());
        HtmlUtils.val('select[name="trouble_date4"]', now.getHours());
        HtmlUtils.val('select[name="webbrowser_name"]', 'Google Chrome');
        //---------------------------------------------------------------
        // 【迷惑行為のご報告】 フォーム
        //---------------------------------------------------------------
        HtmlUtils.val('select[name="lova_report_datetime1"]', now.getFullYear());
        HtmlUtils.val('select[name="lova_report_datetime2"]', now.getMonth() + 1);
        HtmlUtils.val('select[name="lova_report_datetime3"]', now.getDate());
        HtmlUtils.val('select[name="lova_report_datetime4"]', now.getHours());
        //---------------------------------------------------------------
        // 【不具合のご報告】、 【迷惑行為のご報告】フォームの両方にある項目
        //---------------------------------------------------------------
        HtmlUtils.val('select[name="fez_world"]', 'ワールド統合後');
    }
}
const COUNTRIES = [
    { text:'', value:''},//セレクトボックスの値がundefinedになるため。
    { text:'ネツァワル'},
    { text:'エルソード'},
    { text:'ホルデイン'},
    { text:'ゲブランド'},
    { text:'カセドリア'},
];
const AREA = [
    { text:'', value:''},//セレクトボックスの値がundefinedになるため。
    { text:'ルダン雪原'}, { text:'ブリザール湿原'}, { text:'グランフォーク河口'}, { text:'ウィネッシュ渓谷'}, { text:'アベル渓谷'},
    { text:'アンバーステップ平原'}, { text:'クダン丘陵'}, { text:'シバーグ遺跡'}, { text:'シュア島古戦場跡'}, { text:'ネフタル雪原'},
    { text:'クノーラ雪原'}, { text:'セルベーン高地'}, { text:'シャーマイン砦'}, { text:'ルード雪原'}, { text:'ロッシ雪原'},
    { text:'ノイム草原'}, { text:'フェブェ雪原'}, { text:'エルギル高地'}, { text:'ドランゴラ荒地'}, { text:'インベイ高地'},
    { text:'アークトゥルス隕石跡'}, { text:'ホークウィンド高地'}, { text:'クラウス山脈'}, { text:'ダガー島'}, { text:'ベルタ平原'},
    { text:'ラナス城跡'}, { text:'ワーグノスの地'}, { text:'ザーク古戦場跡'}, { text:'ソーン平原'}, { text:'ワードノール平原'},
    { text:'アシロマ山麓'}, { text:'クローディア水源'}, { text:'スピカ隕石跡'}, { text:'始まりの大地'}, { text:'カペラ隕石跡'},
    { text:'マスクス水源'}, { text:'セノビア荒地'}, { text:'タマライア水源'}, { text:'デスパイア山麓'}, { text:'キンカッシュ古戦場跡'},
    { text:'オリオン廃街'}, { text:'ゴブリンフォーク'}, { text:'ニコナ街道'}, { text:'ログマール古戦場跡'}, { text:'レイクパス荒地'},
    { text:'ラインレイ渓谷'}, { text:'シディット水域'}, { text:'ウェンズデイ古戦場跡'}, { text:'ジャコル丘陵'}, { text:'ブローデン古戦場跡'},
    { text:'オブシディアン荒地'},
];
// call function 
var widgets = new Widgets();
widgets.setdefaultvalues();
