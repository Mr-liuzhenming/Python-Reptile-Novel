# Python-Reptile-Novel

看小说要钱？免费的有广告？下载txt找不到？

今天分享的程序可以解决以上困扰，，习Python爬虫知识同时还可以得到你当前想看的小说，调试好代码，只需按一下回车即可完成。

代码我已调试过了，下面是操作步骤：

 1. 将代码复制到你的Python文件中，存放在本地C盘根目录下，名为：`downnovel.py`；
 2. 安装所需要的Python模块：
`pip3 install requests`
`pip3 install Ixml`
 3. 在代码中最下面相应位置，修改你要下载的小说名称，不要写错字哦；
 4. 指定一个保存小说txt文件的目录路径；
 5. `Win+R` 运行 `cmd`，在命令行中输入：`python C:/downnovel.py` 回车查看结果；
 6. 可以看到命令行中输出的章节名称与下载进度，等待下载完成就可以打开阅读了
 
 至此，我们就完成了Python爬取任意一本小说并保存txt到本地的程序执行，大家喜欢的记得支持一下，有遇到问题的随时在评论区里找我沟通。
 
可能会遇到的问题：
 1. 爬取太多小说，可能会导致IP被封，此时需换个网络或第二天在爬取;
 2. 程序如果报错，大半原因是小说名称写错了，此时检查小说名称是否正确;
 3. 还有一种情况就是我设定的源没有你要的小说，这个就需要修改代码的源地址和相关解析代码了。
