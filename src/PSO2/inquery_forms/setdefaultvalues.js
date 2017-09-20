class HtmlUtils {
    static QS(key) {
        // セレクタ
        const node = document.querySelector(key);
        if (node == null) return null;
        // 問い合わせフォームの確認画面ではhiddenになるため。
        if (node.getAttribute('type') == 'hidden') return null;
        return node;
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
    setdefaultvalues() {
        // 問い合わせフォーム表示の初期設定値
        const now = new Date();
        //---------------------------------------------------------------
        // 【不具合のご報告】 フォーム
        //---------------------------------------------------------------
        // 年月日時
        const y = now.getFullYear();
        const m = String(now.getMonth() + 1).padStart(2, '0');
        const d = String(now.getDate()).padStart(2, '0');
        HtmlUtils.val('input[name="spt_hapdate"]', y + '-' + m + '-' + d + ' ');
    }
}

// call function 
var widgets = new Widgets();
widgets.setdefaultvalues();
