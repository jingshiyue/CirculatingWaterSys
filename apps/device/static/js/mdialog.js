/**
 * 
 * @authors Your Name (you@example.org)
 * @date    2017-09-04 15:17:12
 * @version $Id$
 */
var dialog = {
    //普通信息提示
    msg:function (msg){
        layer.open({
            title: [
              '错误提示',
              'background-color: #E71F19; color:#fff;'
            ]
            ,content: msg
            ,time: 3
          });
    },
    error:function(msg,url){
        layer.closeAll('loading');
        if (url) {
            layer.open({
                type: 0,
                time: 1,
                content: msg,
                skin: 'msg',
                end: function() {
                    window.location.href = url;
                    layer.closeAll();
                }
            });
        }else{
            layer.open({
                type: 0,
                time: 3,
                content: msg,
                skin: 'msg',
            });
        }
    },
    success:function(msg,url){
        layer.closeAll('loading');
        layer.open({
          content: msg,
          btn: '确定',
          shadeClose: false,
          yes: function(){
            if (url == 'reload') {
                location.reload();
            }else{
                if (url) {
                    window.location.href=url;
                    //history.back(-1);
                }else{
                    history.back(-1);
                }
            }
            
            //window.location.href=url;
            layer.closeAll();
          }
        });
    },
    loading:function(){
        layer.open({
            type: 2
            ,content: '处理中...'
        });
    }

}

