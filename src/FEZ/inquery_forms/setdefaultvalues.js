const COUNTRIES = [
	{ text:'', value:'' },
    { text:'ネツァワル', value:'ネツァワル' },
    { text:'カセドリア', value:'カセドリア' },
    { text:'エルソード', value:'エルソード' },
	{ text:'ホルデイン', value:'ホルデイン' },
	{ text:'ゲブランド', value:'ゲブランド' },
];
// セレクトボックスを作成
function createSelectBox(element, options){
    element.length = options.length;
    for (var i = 0; i < options.length; i++){
		var item = options[i];
        element.options[i].text = item.text;
        element.options[i].value = item.value;
    }
};
// 値を設定
function setValue(key, value) {
	const element = document.querySelector(key);
	if (element == null) return;
	element.value = value;
};
// 国家名のセレクトボックスを作成
// セレクトボックスを選択時に、input項目に反映
function createCountries(key) {
	const element = document.querySelector(key);
	if (element == null) return;
	const select = document.createElement('select');
	createSelectBox(select, COUNTRIES);
	// セレクトボックス => input項目への反映
	select.onchange = (event) => {
		const target = event.target;
		element.value = target.options[target.selectedIndex].value;
	};
	element.parentNode.insertBefore(select, element.nextSibling);
};

function setdefaultvalues() {
	const now = new Date();
	//---------------------------------------------------------------
	// 【不具合のご報告】 フォーム
	//---------------------------------------------------------------
	setValue('select[name="trouble_date1"]', now.getFullYear());
	setValue('select[name="trouble_date2"]', now.getMonth() + 1);
	setValue('select[name="trouble_date3"]', now.getDate());
	setValue('select[name="trouble_date4"]', now.getHours());
	setValue('select[name="webbrowser_name"]', 'Google Chrome');
	//---------------------------------------------------------------
	// 【迷惑行為のご報告】 フォーム
	//---------------------------------------------------------------
	setValue('select[name="lova_report_datetime1"]', now.getFullYear());
	setValue('select[name="lova_report_datetime2"]', now.getMonth() + 1);
	setValue('select[name="lova_report_datetime3"]', now.getDate());
	setValue('select[name="lova_report_datetime4"]', now.getHours());
	createCountries('input[name="fez_reporter_region"]'); //通報者の国家名
	createCountries('input[name="fez_report_region"]'); //違反者の国家名
	//---------------------------------------------------------------
	// 【不具合のご報告】、 【迷惑行為のご報告】フォームの両方にある項目
	//---------------------------------------------------------------
	setValue('select[name="fez_world"]', 'ワールド統合後');
};
// call function 
setdefaultvalues();