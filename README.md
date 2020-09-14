
## 【准备工作】

### 1. 安装Gunicorn
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