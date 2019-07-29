//获取窗口的高度
let windowHeight;
//获取窗口的宽度
let windowWidth;
//获取弹窗的宽度
let popWidth;
//获取弹窗高度
let popHeight;

// 从服务器端获得账本数据
// 注意参数 callback 函数为从服务器端成功取到数据后的回调函数
// 账本数据s模型
let bills = [{
    id: 3,                                         // 账单ID
    time: new Date('2019-05-15 19:27:38'),         // 记账时间
    amount: 80000,                                 // 金额, 单位:分
    memo: '老爸发生活费了'                          // 备注
}, {
    id: 2,
    time: new Date('2019-05-15 17:44:31'),
    amount: -1470,
    memo: '食堂打的饭, 味道还真是一般'
}, {
    id: 1,
    time: new Date('2019-05-15 17:27:12'),
    amount: -1890,
    memo: '买本《小王子》, 补个童年'
}, {
    id: 0,
    time: new Date('2019-05-14 18:19:34'),
    amount: -1200,
    memo: '今晚吃饺子'
}];
// let bills=[];
function getBillsFromServer(callback,url) {
    // 使用 jQuery 向服务器端发送 Ajax 请求
    $.ajax({
        url: url,          // 对应 Code-10.1 第 17 行, 注意多了 "/wl" 前缀
        method: 'GET',                 // 声明以 get 方式发送请求
        dataType: "json",             // 告诉 jQuery, 服务器端返回的数据是 JSON 格式
        // data:bills[0],s
        // headers:{"X-CSRFToken":$.cookie('csrftoken')}, //发起的是post请求所以要加csrftoken,目的就是声明下，可以通过django中间件的验证机制
        beforeSend: function () {     // 发送请求前的回调函数
            $("#progress").show();    // 发送请求前显示进度提示(左下角一个绕圈圈的动画)
        },
        success: function (resp) {    // 请求成功时的回调函数
            if (resp) {     // 若服务器端回应数据中状态码 code >= 0, 说明服务器端一切正
                callback(resp.data);// 回调 callback 函数, 并将服务器端返回的数据传入
            }
        },
        error: function () {          // 请求失败的回调函数
            $.fail("服务器出错啦!")
        },
        complete: function () {       // 请求完成时的回调函数
            $("#progress").hide();    // 隐藏进度提示
        }
    });
}
function saveToServer(callback,url,bill,action) {
    // 使用 jQuery 向服务器端发送 Ajax 请求
    console.log(JSON.stringify(bill));
    $.ajax({
        url: url,          // 对应 Code-10.1 第 17 行, 注意多了 "/wl" 前缀
        method: 'POST',                 // 声明以 get 方式发送请求
        dataType: "json",             // 告诉 jQuery, 服务器端返回的数据是 JSON 格式
        data: {
            action: action,               // 对应服务器端 Action 方法参数 (Code-10.1 第 30 行)
            bill: JSON.stringify(bill)    // 对应服务器端 Action 方法参数 (Code-10.1 第 31 行)
        },
        headers:{'Content-Type': "application/x-www-form-urlencoded"},
        // headers:{"X-CSRFToken":$.cookie("csrftoken")}, //发起的是post请求所以要加csrftoken,目的就是声明下，可以通过django中间件的验证机制
        beforeSend: function () {     // 发送请求前的回调函数
            $("#progress").show();    // 发送请求前显示进度提示(左下角一个绕圈圈的动画)
        },
        success: function (resp) {    // 请求成功时的回调函数
            if (resp) {     // 若服务器端回应数据中状态码 code >= 0, 说明服务器端一切正常
                callback(resp.data);// 回调 callback 函数, 并将服务器端返回的数据传入
            }
        },
        error: function () {          // 请求失败的回调函数
            $.fail("服务器出错啦!")
        },
        complete: function () {       // 请求完成时的回调函数
            $("#progress").hide();    // 隐藏进度提示
        }
    });
}


const url="http://127.0.0.1:8000/getBills/";

// 一条账单的 HTML 模板
// 对应 Code-3.3.2, 只是把其中类似 "05/13" 这样的信息删除了, 因为这些信息应是变量值, 而不是"硬编码"
// 注意, 变量 billItemTemplete 的值是一个字符串
const billItemTemplete = '<li class="record">' +
    '<div class="date-time">' +
    '<h2 class="date" data-field="date"></h2>' +
    '<p class="time" data-field="time"></p>' +
    '</div>' +
    '<div class="content">' +
    '<h4 class="media-heading io" data-field="amount"></h4>' +
    '<p class="memo" data-field="memo"></p>' +
    '</div>' +
    '</li>';

// 创建一条账单的 DOM
// 参数 bill 是一条账单的数据, 即 Code-3.3.1 所示的一坨数据
function createBillItemDom(bill) {
    // 借助 jQuery 直接使用账单模板形成 DOM
    // $item 为一条账单的 DOM
    const $item = $(billItemTemplete);

    // 将账单时间构建成 moment 对象, 以便后续格式化输出
    // moment() 来自第三方库 moment.js
    const dt = moment(bill.time);

    // 遍历所有含有 data-field 属性的元素
    // 并使用数据模型 (bill) 中的值替换此元素的内容(innerText)
    $item.find('[data-field]').each(function (i, ele) {
      	// 针对每一个含有"data-field"属性的元素, 此匿名函数将被执行一次
        // 其中参数 i 为顺序号, ele 为当前遍历到的元素

      	// 将 ele 这个普通的 DOM 元素封装成 jQuery 对象, 以便处理.
        const $ele = $(ele);

        // 读取当前元素的 data-field 属性值
        const field = $ele.attr('data-field');

        // 根据 data-field 属性值不同, 分别作不同的处理
        switch (field) {
            case 'date':    // 若 data-field = date, 填入使用 moment.js 格式化后的 "月/日"
                $ele.text(dt.format('MM/DD'));
                break;
            case 'time':    // 若 data-field = date, 填入使用 moment.js 格式化后的 "时:分:秒"
                $ele.text(dt.format('HH:mm:ss'));
                break;
            case 'amount':  // 金额字段
                $ele.text(bill.amount/100,true);
                // 若金额大于 0, 则给当前元素(金额字段)添加样式类 "in" (显示为绿色)
                if (bill.amount > 0) {
                    $ele.addClass('in');
                }
                break;
            default:        // 对于其余元素(如: memo), 直接使用 bill 中的相应属性值填充
                $ele.text(bill[field]);
        }
    });
    //增加时延迟
    let TimeFn=null;
    //双击进行删除数据
    $item.dblclick(function () {
        clearTimeout(TimeFn);
        removeBillItem($item, bill);
    });
    //单击进行数据的修改
    $item.click(function () {
        clearTimeout(TimeFn);
        TimeFn = setTimeout(function(){
            popCenterWindow($item,bill);
        },300);

    });

    // 返回构建好的 DOM
    return $item;
}
// 显示账本中所有账单
function showBillItems() {
    // 账单列表的容器, Code-2.1 中 41 行的那个 <ul>
    const $billItems = $('#bill-items');

    // 清空账单列表
    $billItems.empty();

    // 遍历整个 bills 数组, 构建每一个账单的 DOM 模型, 并将其"装入" 账单列表容器
    for (let i = 0; i < bills.length; i++) {
        $billItems.append(createBillItemDom(bills[i]));
    }
}

// 显示结余
function refreshBalance() {
    // 计算 "结余"
    let balance = 0;
    for (let i = 0; i < bills.length; i++) {
        balance += parseInt(bills[i].amount);
    }
    balance =balance/100;
    // 刷新界面
    const $balance = $("#balance");
    $balance.css('color', (balance > 0) ? 'green' : '#ce4844');
    $balance.find('span').text(balance,false);
}
// 新增一条账单的数据到账本数据模型
// 参数说明:
// bill - 新账单的数据, 一个对象, 形如 Code-3.3.1 中展示的那样一坨
// callback - 数据模型更新成功后的回调函数
function addBillItemData(bill, callback) {
    // 将新账单数据插入账本数据模型(账单数组)的开头
    // array.push() 是在数组尾部新增元素, array.unshift() 则是在开头插入新元素
     // 保存数据到服务器端
    saveToServer( function (newBill) {
        // 更新前端账本数据, 以保持和服务器端一致
        bills.unshift(newBill[0]);
        console.log(bills);
        // 回调刷新界面
        callback(newBill[0]);
    },url,bill,'append');
}
function addBillItem() {
    // 找到金额和备注输入框
    const $fAmount = $('#nb-amount');
    const $fMemo = $('#nb-memo');

    // 取得用户输入的金额值, 并做验证
    const amount = parseFloat($fAmount.val());
    if (!amount) {
      	// $.fail() 将弹出一个漂亮的消息框, 作用和 alert('金额不对哦~') 相同, 只是更漂亮
        // $.fail() 借助了 jquery-confirm.3.3.min.js 提供的功能
        // 并在 jquery-confirm-bailey.js 做了扩展, 可参看附件中的代码
        $.fail('金额不对哦~');
        return;
    }

    // 新增账单的数据
    const bill = {
        time: new Date(),                   // 取客户端当前系统时间
        amount: Math.round(amount * 100),   // 用户输入的金额乘以100后取整. 由"元"换算成"分"
        memo: $fMemo.val()
    };

    // 数据模型更新成功后的回调函数, 实现界面刷新
    const callback = function (bill) {
        // 创建新账单项的DOM
        const $billItemDom = createBillItemDom(bill);
        // 插入到账单列表(#bill-items) 的第 1 项之前
        $('#bill-items').prepend($billItemDom);
        // getBillsPostServer()
        // 清空账单编辑面板中的"金额"和"备注"输入框
        $fAmount.val('');
        $fMemo.val('');

        // 刷新结余显示
        refreshBalance();
    };

    // 添加账单数据模型, 成功后回调, 刷新界面
    addBillItemData(bill, callback);
}
// 从账本中删除账单数据 (更新账本数据模型), 成功后回调刷新界面
// 参数说明:
// bill - 待删除的账单数据
// callback - 删除成功(账本数据模型更新成功)后的回调函数
function removeBillData(bill, callback) {
    // 保存数据到服务器端, 调用的仍然是 Code-11.2.1 中的 saveToServer 函数, 只是参数变了
    saveToServer(function () {
        // 删除前端账本数据模型中对应的记录, 与服务器端保存一致
        for (let i = 0; i < bills.length; i++) {
            if (bills[i].id === bill.id) {
                bills.splice(i, 1);
                break;
            }
        }
        // 回调刷新界面
        callback();
    },url,bill,'remove');
}

// 删除一条账单
// 此函数所需的两个参数 $item 和 bill 在 Code-5.1.1 第 7 行传入
// $item 为用户双击的账单项的DOM
// bill 双击的那个账单项对应的数据对象
function removeBillItem($billItemDom, bill) {
// $.question() 将弹出一个漂亮的提示框
    // $.question() 借助了 jquery-confirm.3.3.min.js 提供的功能
    // 并在 jquery-confirm-bailey.js 做了扩展, 可参看附件中的代码
    $.question('确定要删除此账单?', function () {
        // 删除数据模型中的账单, 成功后回调刷新界面
        removeBillData(bill, function () {
            // 从 DOM 中移除当前账单项, 即从界面上移除当前账单
            $billItemDom.remove();
            // 刷新"结余"显示
            refreshBalance();
        });
    });


}


$(document).ready(function () {
    // 从服务器端获取账本数据
    // 此处调用的是 Code-11.1.1 中定义的那个 getBillsFromServer 函数
    // 你找到 Code-11.1.1 中 getBillsFromServer 函数所需要的 callback 回调函数了吗?
    getBillsFromServer(function (result) {
        // 将获取到的数据赋值给 bills 数组
        console.log(result);
        bills = result;
        // 显示账单列表
        showBillItems();
        // 显示结余
        refreshBalance();
    },url);
    // 注册 打开/关闭"账单编辑面板"按钮 的点击事件监听
    $('#btn-add-bill').click(toggleBillEditor);
     // 注册 "记一笔" 按钮点击事件监听
    $('#btn-confirm-add').click(addBillItem);


});

// 打开/关闭账单编辑面板
function toggleBillEditor() {
    // 显示/隐藏"账单编辑面板"
    $("#panel-bill-editor").toggle('fast');

    // 切换展开(>) 和 关闭(<) 图标
    const $btnIcon = $(this).find('i');
    $btnIcon.toggleClass('glyphicon-menu-left');
    $btnIcon.toggleClass('glyphicon-menu-right');
}



function init() {
      windowHeight = $(window).height();
      windowWidth = $(window).width();
      popHeight = $(".window").height();
      popWidth = $(".window").width();
    }
//关闭窗口的方法,
function closeWindow(btn2,showMsg) {
    $(".cancel").click(function () {
    $('.window').hide("slow");
    $('.mask').css('display', 'none');
    btn2.removeEventListener('click', showMsg, false); //去除绑定
  });
}

//定义弹出居中窗口的方法
//实现修改，查看详细信息
function popCenterWindow($item,bill) {
  init();
  $('.mask').css('display', 'block');
  $('.mask').css('width', $(window).width());
  $('.mask').css('height', $(document).height());
  //计算弹出窗口的左上角X的偏移量
    const popX = (windowWidth - popWidth) / 2;
    // 计算弹出窗口的左上角Y的偏移量为窗口的高度 - 弹窗高度 / 2 + 被卷去的页面的top
    const popY = (windowHeight - popHeight) / 2 + $(document).scrollTop();
    //设定窗口的位置
    $("#center").css("top", popY).css("left", popX).slideToggle("fast");

    const $fAmount = $('#b-amount');
    const $fMemo = $('#b-memo');
    //把获取到的数据放到输入框里
    $fAmount.val(bill.amount/100);
    $fMemo.val(bill.memo);
    const btn2 = document.getElementById('change');
    btn2.addEventListener('click', showMsg, false); //鼠标单击的时候调用showMes这个函数
    function showMsg() {
        // 取得用户输入的金额值, 并做验证
        const amount = parseFloat($fAmount.val());
        // 修改账单的数据
        bill.amount = $fAmount.val()*100;
        bill.memo =$fMemo.val();
        // bill.time = new Date();
        console.log(bill);
       // 找到金额和备注输入框
        if (!amount) {
            // $.fail() 将弹出一个漂亮的消息框, 作用和 alert('金额不对哦~') 相同, 只是更漂亮
            // $.fail() 借助了 jquery-confirm.3.3.min.js 提供的功能
            // 并在 jquery-confirm-bailey.js 做了扩展, 可参看附件中的代码
            $.fail('金额不对哦~');
            return;
        }else {
            $('.window').hide("slow");
            $('.mask').css('display', 'none') ;
            saveToServer(function (newBill) {
                // 删除前端账本数据模型中对应的记录, 与服务器端保存一致
                for (let i = 0; i < bills.length; i++) {
                    if (bills[i].id === newBill.id) {
                        bills.splice(i, 1);
                        break;
                    }
                }
                console.log(bills);
                // 更新前端账本数据, 以保持和服务器端一致
                bills.unshift(newBill);
                //去除绑定
                btn2.removeEventListener('click', showMsg, false);
                //刷新界面
                showBillItems();
                // 刷新"结余"显示
                refreshBalance();
            },url,bill,'revamp');

        }
    }
    closeWindow(btn2,showMsg);
}

//实现对input实时监听
function search(e){
    const Bills = document.getElementById('input_search').value;
    //实现模糊搜索功能
    saveToServer(function (newBill) {
                console.log(newBill);
                //更新前端账本数据, 以保持和服务器端一致
                if (newBill!=null){
                    bills=newBill;
                    //刷新界面
                    showBillItems();
                    // 刷新"结余"显示
                    refreshBalance();
                }

            },url,Bills,'search');
}