(function () {
	'use strict';
	chrome.alarms.create('Tasks', {
    	periodInMinutes: 1
	});
	chrome.alarms.onAlarm.addListener(function(alarm) {
		console.log(alarm);
	});
})();