$(function () {
    total();
    $('#carts ul').each(function () {

        let $num_show = $(this).find('.num_show');
        let price = $(this).find('.col05 em').html();
        let $money = $(this).find('.col07');
        let goods_id = $(this).attr('id');
        let $ul = $(this);
        $money.html(parseFloat(price)*parseInt($num_show.val()) + '元');
        $num_show.blur(function () {

            let n = $(this).val();

            if (/^[1-9]\d*$/.test(n)){
                let money = parseInt(n) * parseFloat(price);
                $money.html( money+ '元')

            }else {
                alert('数量填写错误');
                n = 1;
                $money.html( price + '元')
            }
            $(this).val(n);
            total();
        });

        $(this).find('.add').click(function () {
            let temp = parseFloat($num_show.val())+1;
            $.get('/cart/edit'+ goods_id + '_' + temp, function (data) {
                if (data.ok == 0){
                    $num_show.val(temp);
                    $money.html(parseFloat(price)*temp + '元');
                }
            });

            total();
        });
        $(this).find('.minus').click(function () {
            if ($num_show.val() == '1'){
                return
            }
            let temp = parseFloat($num_show.val())-1;
            $.get('/cart/edit'+ goods_id + '_' + temp, function (data) {
                if (data.ok == 0){
                    $num_show.val(temp);
                    $money.html(parseFloat(price)*temp + '元');
                }
            });
            total();
        });

        $(this).find('.col08').click(function () {

            $.getJSON('/cart/delete'+ goods_id, function (data) {

                if (data.ok == 0){
                    alert('删除失败')
                }else {
                    $ul.remove();
                    if ($('#carts ul').length == 0){
                        window.location.reload()
                    }
                }
            })

        })

    });

    $('#select_all').click(function () {

        let sta = $(this).prop('checked');
        $(':checkbox:not(#select_all)').prop('checked', sta)
        total();
    });

    $(':checkbox:not(#select_all)').click(function () {

        if ($(this).prop('checked')){
            if ($(':checked').length+1 == $(':checkbox').length){
                $('#select_all').prop('checked', true)
            }
        } else {
            $('#select_all').prop('checked', false)
        }
        total();
    });

    function total() {
        let total_count = 0;
        let total_money = 0;

        $(':checked:not(#select_all)').each(function () {
            total_count += 1
            total_money += parseFloat($(this).parent().siblings('.col07').text())

        })

        $('.settlements .col03 b').text(total_count);
        $('#total_money').text(total_money);

    }


});