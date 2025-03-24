# 部署四部曲

> [!IMPORTANT]
> **前奏 (必读)** <br/>
> **建议使用 国外机器 / 容器平台 部署** *(因为需要与 Discord 服务器的稳定连接，但国内网络不进行一些特殊配置无法与 Discord 服务器通信，~~你懂的~~)*

## 1. 《下载》

有两种方式：

1. 如果你的机器安装了 Git

```shell
git clone https://github.com/siiway/JMComic-Discord-Bot.git
cd JMComic-Discord-Bot
```

2. 如果你的机器没有安装 Git

```shell
wget -O temp.zip https://github.com/siiway/JMComic-Discord-Bot/archive/refs/heads/main.zip # 如没有 wget 可使用 curl / 自行下载
unzip temp.zip # 如没有 unzip 自行解压
cd JMComic-Discord-Bot-main
```

## 2. 《依赖》

```shell
# Windows
python -m pip install -r requirements.txt
```

```shell
# Linux
python3 -m pip install -r requirements.txt
```

> 剩下的择日再写

<!-- ## 3. 《配置》 -->

<!-- ## 4. 《启动》 -->