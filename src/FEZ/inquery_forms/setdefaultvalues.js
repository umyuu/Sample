class HtmlUtils {
    QS(key) {
        // セレクタ
        const element = document.querySelector(key);
        if (element == null) return null;
        // 問い合わせフォームの確認画面では非表示項目になるため。
        if (element.getAttribute('type') == 'hidden') return null;
        return element;
    }
    createSelectBox(element, options) {
        // セレクトボックスを作成
        element.length = options.length;
        for (var i = 0; i < options.length; i++){
            const item = options[i];
            element.options[i].text = item.text;
            element.options[i].value = item.value;
        }
    }
    setValue(key, value) {
        // 値を設定
        // key:Selector
        // value:value
        const element = this.QS(key);
        if (element == null) return;
        element.value = value;
    }
}

class Widgets {
    createCountries(key) {
        // 国家名のセレクトボックスを作成
        // セレクトボックスを選択時に、input項目に反映
	   const element = utils.QS(key);
	   if (element == null) return;
	
	   const select = document.createElement('select');
	   utils.createSelectBox(select, COUNTRIES);
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
	   utils.setValue('select[name="trouble_date1"]', now.getFullYear());
	   utils.setValue('select[name="trouble_date2"]', now.getMonth() + 1);
	   utils.setValue('select[name="trouble_date3"]', now.getDate());
	   utils.setValue('select[name="trouble_date4"]', now.getHours());
	   utils.setValue('select[name="webbrowser_name"]', 'Google Chrome');
	   //---------------------------------------------------------------
	   // 【迷惑行為のご報告】 フォーム
	   //---------------------------------------------------------------
	   utils.setValue('select[name="lova_report_datetime1"]', now.getFullYear());
	   utils.setValue('select[name="lova_report_datetime2"]', now.getMonth() + 1);
	   utils.setValue('select[name="lova_report_datetime3"]', now.getDate());
	   utils.setValue('select[name="lova_report_datetime4"]', now.getHours());
	   this.createCountries('input[name="fez_reporter_region"]'); //通報者の国家名
	   this.createCountries('input[name="fez_report_region"]'); //違反者の国家名
	   //---------------------------------------------------------------
	   // 【不具合のご報告】、 【迷惑行為のご報告】フォームの両方にある項目
	   //---------------------------------------------------------------
	   utils.setValue('select[name="fez_world"]', 'ワールド統合後');
    }
}
const COUNTRIES = [
    { text:'', value:'' },
    { text:'ネツァワル', value:'ネツァワル' },
    { text:'エルソード', value:'エルソード' },
    { text:'ホルデイン', value:'ホルデイン' },
    { text:'ゲブランド', value:'ゲブランド' },
    { text:'カセドリア', value:'カセドリア' },
];
var utils = new HtmlUtils();
// call function 
var widgets = new Widgets();
widgets.setdefaultvalues();
