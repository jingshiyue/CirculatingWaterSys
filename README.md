## CirculatingWaterSys windows上docker环境搭建
    1、启动docker，导入两个镜像
        a. docker load < mysql_5.7_save.tar 导入mysql镜像；
        b. docker load < circulating_water_sys_save.tar，导入CirculatingWaterSys镜像；
        
    2、进入到项目路径下，生成2个容器
        a. docker-compose -f mysql.yml up 
        b. docker-compose -f web.yml up 
        
    3、用workbench登录mysql服务，修改数据库的编码格式为utf-8
    
    4、进入到导入CirculatingWaterSys容器，安装所需要的第三方包
        a. docker -it 容器ID bash            (进入容器)
        b. pip install -r requirements.txt   (安装所需要的第三方包，如果这部执行反复失败，可以c替代b)
        c. 复制requirements - 副本.txt内容，粘贴到控制窗口 
        d.替换needReplaceFile里的文件，替换步骤参照needReplaceFile里的“操作说明.txt”
        
    5、进入到导入CirculatingWaterSys容器，启动项目 
        a. docker -it 容器ID bash                         (进入容器)
        b. python manage.py makemigrations
        c. python manage.py migrate                       (生成数据库对应的数据)
        d. python manage.py createsuperuser               (创建管理员账户)
        e. python manage.py runserver 0.0.0.0:8000        (启动项目)
        f. 浏览器访问http://192.168.99.100:8000/index/index/login/  ，用"d"中创建的管理账号登录

http://192.168.99.100:8000/jwt_auth
http://192.168.99.100:8000/index/index.html/
http://192.168.99.100:8000/index/index/my.html/
http://192.168.99.100:8000/index/index/login/
http://localhost:8000/index/index/login/
http://203.176.75.1:8000/index/index/login/

config:
    https://www.cnblogs.com/xueweihan/p/11649630.html
   
drf demo：
	生鲜超市
	https://www.cnblogs.com/derek1184405959/p/8733194.html
   
   
http://ro.yueshuidz.com/index/index/login
http://ro.yueshuidz.com/Index/index/index.html
智跃测试 
12345678
173302591@qq.com

## 任务计划：
    10-19
        把django drf框架搭建起来，写几个路由，映射前端页面；
        docker搭建django应用；
        
## 最终目标：
    把项目部署到windows上
    用uwsgi？
    用nginx？
    前端 - 手机页面？
    
	pip freeze > requirements.txt
	pip install -r requirements.txt

    export COMPOSE_TLS_VERSION=TLSv1_2
    http://192.168.99.100:8000/

    调试时候不要用 【容器的日志】命令查看日志，不会更新，要重启容器，容器里的修改才会生效，而且有些日志，这里看不到
    调试进入到容器，用python manage.py runserver xxx,查看日志，修改会动态生效

    compose文件里的容器间通信，用172.18.0.2，用 docker network inspect xxx 查看容器“内网ip”
    容器与宿主机通讯用 192.168.99.100 通讯，用“外网ip”通讯

## 管理员用户
   root 
   123456

## 编译镜像文件
    docker-compose -f local.yml up --build
    docker-compose -f local.yml up  前台运行
    docker-compose -f local.yml -d up  后台运行

## 常用到的命令
    pip install -i http://mirrors.aliyun.com/pypi/simple/
    $ docker start $(docker ps -lq)
    save 和 export区别：
        1）save 保存镜像所有的信息-包含历史
        2）export 只导出当前的信息

    镜像导入和容器导入的区别：
    1）容器导入 是将当前容器 变成一个新的镜像 export-import
    2）镜像导入 是复制的过程 save-load

    
    docker save 9045 > tomcat8-apr.tar
    docker load < tomcat8-apr.tar
    
    docker export 7ec802bdcfe3> mysql.tar  #7ec802bdcfe3 容器id
    docker import tomcat80824.tar
    
    docker tag 9045 tomcat8-apr:3.0  #修改镜像名字， 9045是镜像id
    
## URL
    http://ro.yueshuidz.com/index/index.html  主页
                                                           主页->设备添加
        http://ro.yueshuidz.com/index/Equipment/index.html 主页->设备管理
            http://ro.yueshuidz.com/index/setting/sell/Id/f0311c1e-e289-ea11-b0df-87120c3b66e0.html  参数设置
                http://ro.yueshuidz.com/index/setting/recover.html  恢复出厂设置
            http://ro.yueshuidz.com/index/Equipment/statetu/Id/f0311c1e-e289-ea11-b0df-87120c3b66e0.html 设备运行状态(列表)
            http://ro.yueshuidz.com/index/Equipment/edit/Id/f0311c1e-e289-ea11-b0df-87120c3b66e0.html  修改

        http://ro.yueshuidz.com/index/repairs/index.html  报修
            http://ro.yueshuidz.com/index/repairs/add.html  一键报修
            http://ro.yueshuidz.com/index/repairs/addfeedback/id/24.html 报修回复
        
        http://ro.yueshuidz.com/index/remind/index.html  售后管理
        http://ro.yueshuidz.com/index/remind/add.html    
        http://ro.yueshuidz.com/index/fault/index.html  主页->设备故障列表
        http://ro.yueshuidz.com/index/index/index.html 更多

    http://ro.yueshuidz.com/index/Equipment/index.html 主页->设备
    
    http://ro.yueshuidz.com/index/index/my.html  主页->我的

### 已完成任务：
    token 实现管理员权限问题 done
    drf 接口区分管理员 done
    上一页，总共 done
    设备列表统计值 done
    嵌套更新和创建 done 
    查询界面 done
    增加add 页面 done
    设备查询框 后端接口对应 done
    主页-》我的-》修改密码  前端
    主页-》我的-》退出登录 前端
    主页-》报修管理 前端
    主页-》售后管理 前端
    主页-》故障管理 前端

### 明日任务-11.12
    设备列表下几个连接生成方式
    
    <button type="button" onclick="power(2,'f0311c1e-e289-ea11-b0df-87120c3b66e0','关机');" class="kgj">关机</button>
    <button type="button" onclick="power(2,'975efb4b-c689-ea11-b0df-87120c3b66e0','关机');" class="kgj">关机</button>


    <a href="/index/setting/sell/Id/f0311c1e-e289-ea11-b0df-87120c3b66e0.html">参数设置</a>
    <a href="/index/setting/sell/Id/975efb4b-c689-ea11-b0df-87120c3b66e0.html">参数设置</a>
    <a href="/index/setting/sell/Id/a706fc26-e289-ea11-b0df-87120c3b66e0.html">参数设置</a>
    <a href="/index/setting/sell/Id/24af3680-c486-ea11-b0df-87120c3b66e0.html">参数设置</a>

    <a href="/index/Equipment/statetu/Id/f0311c1e-e289-ea11-b0df-87120c3b66e0.html">设备运行状态</a>
    <a href="/index/Equipment/statetu/Id/975efb4b-c689-ea11-b0df-87120c3b66e0.html">设备运行状态</a>
    <a href="/index/Equipment/statetu/Id/a706fc26-e289-ea11-b0df-87120c3b66e0.html">设备运行状态</a>


    <a href="/index/Equipment/edit/Id/f0311c1e-e289-ea11-b0df-87120c3b66e0.html">修改</a>

    <a href="/index/Equipment/info/Id/f0311c1e-e289-ea11-b0df-87120c3b66e0.html">更多</a>

                            

### notes
     token储在客户端，例如存在local storage或cookie中
     headers: {'Authorization': 'JWT ' + token}