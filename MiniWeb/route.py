# 用来存储所有视图的映射关系
URL_FUNC = dict()


def route(url):
    def set_url_func(func):
        # 向字典添加数据
        URL_FUNC[url] = func

        def call_func():
            func()

        return call_func

    return set_url_func


print("---这是 MiniWeb/route.py---")
