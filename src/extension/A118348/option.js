'use strict';
(function (){
    function loadfun(){
        chrome.storage.local.get('value', (items) => {
            console.log(`${new Date().toISOString()} ${loadfun.name}:${items.value}`);
            const user_name = document.querySelector('#user_name');
            user_name.value = items.value || '';
        });
    }
    function savefun(){
        const user_name = document.querySelector('#user_name');
        const getter = user_name.value;
        chrome.storage.local.set({'value': getter}, () => {
            console.log(`${new Date().toISOString()} ${savefun.name}:${getter}`);
        });
    }
    document.addEventListener('DOMContentLoaded', (event) => {
        const load = document.querySelector('#load');
        load.addEventListener('click', (e) => {
            loadfun();
        }, false);
        const save = document.querySelector('#save');
        save.addEventListener('click', (e) => {
            savefun();
        }, false);
        // ページ表示時
        loadfun();
    });
})();