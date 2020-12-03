
/**
 * 提交form表单操作
 */

$("#h-submit").click(function(){
    $("#h-submit").attr("disabled",true);
    // 提示
    //dialog.loading();
    //return false;
    var data = $("#h-form").serializeArray();
    console.log(data)
    postData = {};
    $(data).each(function(i){
       postData[this.name] = this.value;
       console.log(this.name)
       console.log(this.value)
    });
    // 将获取到的数据post给服务器
    url = SCOPE.post_url;
    console.log(data)

    $.post(url,postData,function(result){
        alert(11111);
        console.log(result);
        // if(result.status == 1) {
        dialog.success(result.message);
        // }else if(result.status == 0) {
        //     // 失败
        //     dialog.error(result.message,result.url);
        //     $("#h-submit").attr("disabled",false);
        //     return false;
        // }
    },"JSON");
});

//弹窗表单提交
$("#n-submit").click(function(){
    $("#n-submit").val("正在处理..");
    $("#n-submit").attr("disabled",true);
    $("#n-submit").css("background-color", "#fe7100 ");
    var data = $("#h-form").serializeArray();
    postData = {};
    $(data).each(function(i){
       postData[this.name] = this.value;
    });
    // 将获取到的数据post给服务器
    url = SCOPE.save_url;
    $.post(url,postData,function(result){
        if(result.status == 1) {
            dialog.successre(result.message);
        }else if(result.status == 0) {
            // 失败
            dialog.errorChange(result.message);
            $("#n-submit").attr("disabled",false);
            $("#n-submit").css("background-color", "#E71F19");
            $("#n-submit").val("确认提交");
            return false;
        }
    },"JSON");
});

