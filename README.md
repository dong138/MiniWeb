
## 【说明】

> MiniWeb框架是一个基于Python3实现的轻量入门级web框架，其目的不是拥有臃肿的功能，而是通过简洁优雅的方式，实现易于让学生快速掌握原理的入门级web框架

> 主要面向的对象：web框架刚刚接触的用户，想要研究框架原理的用户

## 【准备工作】

### 安装Gunicorn
想要用Gunicorn需要安装，命令如下
pip install gunicorn -i https://pypi.tuna.tsinghua.edu.cn/simple



##【使用】

### 1. 终端中，运行命令

```
gunicorn -w 1 -b 127.0.0.1:8080 MiniWeb:application
```

简单说明：

* `-w 1` 表示同意同时处理的请求只有1个，可以改的大一点
* `-b 127.0.0.1:8080` 表示绑定的ip以及端口
* `MiniWeb:application` 表示哪个`.py`下的哪个函数作为WSGI协议调用的入口

### 2. 浏览器访问

```
http://127.0.0.1:8080
```
