$(function () {
    $('.detail_tab').delegate('li', 'click', function () {
        $(this).addClass('active').siblings().removeClass('active')
    });
    let num = $('.num_show');
    let p = $('.show_pirze em').html();
    let t = $('.total em');
    t.html(parseFloat(p)*parseFloat(num.val()));
    $('.add').click(function () {
        let temp = parseFloat(num.val())+1
        num.val(temp)
        t.html(parseFloat(p)*temp);
    })
    $('.minus').click(function () {
        if (num.val() == '0'){
            t.html('0')
            return
        }
        let temp = parseFloat(num.val())-1
        num.val( temp)
        t.html(parseFloat(p)*temp);
    })
    num.keyup(function () {
        t.html(parseFloat(p)*parseFloat(num.val()));
    })

    

});