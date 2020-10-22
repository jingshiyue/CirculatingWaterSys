# CirculatingWaterSys

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

    