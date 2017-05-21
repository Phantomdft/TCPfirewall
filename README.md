# TCPfirewall

TCP入侵检测系统，检测端口扫描、Dos攻击、爬虫联动iptables进行防御

1.基于tcp的请求频率
2.tcp的flag标志位，SYN\FIN\NULL包的比例
3. 未开放端口的请求比例

需要安装的库python-iptables\MySQLdb\scapy
