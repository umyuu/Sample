function setValue(key, value) {
	const element = document.querySelector(key);
	if (element == null) return;
	element.value = value;
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
	//---------------------------------------------------------------
	// 【不具合のご報告】、 【迷惑行為のご報告】フォームの両方にある項目
	//---------------------------------------------------------------
	setValue('select[name="fez_world"]', 'ワールド統合後');
};
// call function 
setdefaultvalues();