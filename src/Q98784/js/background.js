(function () {
    'use strict';
    chrome.downloads.onDeterminingFilename.addListener(function(item, suggest) {
       if(item.mime === 'application/pdf'){
           console.log(item.url);
           localStorage.setItem(item.startTime, item.url);
       }
    });

})();