class HtmlUtils {
    static QS(key) {
        // セレクタ
        const element = document.querySelector(key);
        if (element == null) return null;
        // 問い合わせフォームの確認画面ではhiddenになるため。
        if (element.getAttribute('type') == 'hidden') return null;
        return element;
    }
    static createSelectBox(options) {
        const element = document.createElement('select');
        // セレクトボックスを作成
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
        const element = HtmlUtils.QS(key);
        if (element == null) return;
        element.value = value;
    }
}

class Widgets {
    constructor() {
        this.createCountries('input[name="fez_reporter_region"]'); //通報者の国家名
        this.createCountries('input[name="fez_report_region"]'); //違反者の国家名
    }
    createCountries(key) {
        // 国家名のセレクトボックスを作成
        // key:Selector セレクトボックスを追加するための位置ヒントとして利用
        // セレクトボックスを選択時に、input項目に反映
        const element = HtmlUtils.QS(key);
        if (element == null) return;
        const select = HtmlUtils.createSelectBox(COUNTRIES);
        // セレクトボックス => input項目への反映
        select.onchange = (event) => {
           const target = event.target;
           element.value = target.options[target.selectedIndex].value;
        }
        element.parentNode.insertBefore(select, element.nextSibling);
    }
    setdefaultvalues() {
	   const now = new Date();
	   //---------------------------------------------------------------
	   // 【不具合のご報告】 フォーム
	   //---------------------------------------------------------------
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
    { text:'', value:''},
    { text:'ネツァワル'},
    { text:'エルソード'},
    { text:'ホルデイン'},
    { text:'ゲブランド'},
    { text:'カセドリア'},
];
// call function 
var widgets = new Widgets();
widgets.setdefaultvalues();
