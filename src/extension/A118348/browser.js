'use strict';
(function (){
    function loader() {
        var keys = 'value';
        chrome.storage.local.get(keys, (items) => {
            console.log(`${new Date().toISOString()} ${loader.name}:${items.value}`);
            const user_name = document.querySelector('#user_name');
            user_name.value = items.value || '';
        });
    }
    document.addEventListener('DOMContentLoaded', (event) => {
        loader();
    });
})();