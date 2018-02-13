javascript:(()=>{
[].forEach.call
document.querySelectorAll('.ProfileTweet-action--favorite').forEach.call
for(let l of document.querySelectorAll('.ProfileTweet-action--favorite')) {
    l.style.display='none';
}
alert('Hide');})();