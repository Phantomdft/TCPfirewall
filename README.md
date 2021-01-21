
好久好久以前写的练习用的小辣鸡项目，大佬们，基本上就是一点点端口扫描检查，大佬可以不用关注了。

# TCPfirewall

TCP入侵检测系统，检测端口扫描、Dos攻击、爬虫联动iptables进行防御

1.基于tcp的请求频率
2.tcp的flag标志位，SYN\FIN\NULL包的比例
3. 未开放端口的请求比例

需要安装的库python-iptables\MySQLdb\scapy

