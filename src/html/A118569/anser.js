$(function (){
    var searchParams = new URLSearchParams(location.search);
    // target _blankで開くリンクはrel="noopener"を付けると安全になります。
    if (!searchParams.has('param')) {
        $('.link').append('<a href="https://Example.com/" target="_blank" rel="noopener"><img src="images/link_off.png" alt=""></a>');
        return;
    }
    sub_dir = searchParams.get("param");
    $('.link').append('<a href="https://Example.com/' + sub_dir + '/" target="_blank" rel="noopener">' + sub_dir + '<img src="images/link_off.png" alt=""></a>');
});