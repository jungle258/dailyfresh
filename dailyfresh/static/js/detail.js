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
    });
    num.keyup(function () {
        t.html(parseFloat(p)*parseFloat(num.val()));
    })


    $('#add_cart').click(function () {

        let goods_id = $('.goods_detail_con').attr('id');
        let num = $('.num_show').val();
        $.getJSON('/cart/add'+ goods_id + '_' + num, function (data) {

            $('#show_count').text(data.count);
        })
        $('#cart_animate').animate(
            {top:70,left:1270},
            300,'swing',
            function () {
                $(this).css({'top': '560px','left': '750px'});
            }
            );
    });



    

});