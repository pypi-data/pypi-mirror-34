## 度盘令

### 目的

用程序做百度盘 Web 界面可以做的所有（Almost）事情。模块化。

1. 读。列表、查看
2. 写。复制、移动、删除、分享。

### 方式

1. 抓取 iPhone 客户端的 HTTP 请求，录下 HAR
2. 用 Python 程序 仿制这些请求
3. 形成模块
4. 封装一个 Cli

### CLI 的假想模式

```

>>> dp = dupan(user="neoney", bduss="")
>>> dp.list('/')
>>> dp.stat('/manga')
>>> dp.cd('/manga')
>>> dp.mkdir('/manga/arakawa')
>>> dp.cp('/manga/hagaren.zip', '/manga/arakawa/hagaren.zip')
>>> dp.move('/manga/hagaren.zip', '/manga/arakawa/hagaren.zip')
>>> dp.delete('/manga/hagaren.zip')
>>> dp.share('/manga/arakawa/hagaren.zip')
>>> dp.sharings
>>>

```