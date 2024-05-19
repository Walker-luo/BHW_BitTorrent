## P2P客户端设计 (language:`C`)
From [Article](https://evilpan.com/2015/10/31/p2p-over-middle-box/)
- 一般的网络编程，都是客户端比服务端要难，因为要处理与服务器的通信同时还要处理来自用户的事件；对于P2P客户端来说更是如此，因为P2P客户端不止作为客户端，同时也作为对等连接的服务器端。

- 这里的大体思路是，输入命令传输给服务器之后，接收来自服务器的反馈，并执行相应代码。例如A想要与B建立通信链路，先给服务器发送punch命令以及给B发送数据，服务器接到命令后给B发送punch_requst信息以及A的端点信息，B收到之后向A发送数据打通通路，然后A与B就可以进行P2P通信了。经测试，打通通路后即便把服务器关闭，A与B也能正常通信。

一个UDP打洞的例子见 https://github.com/pannzh/P2P-Over-MiddleBoxes-Demo


## mininet
https://blog.csdn.net/Rocky006/article/details/135910371

[tutorial](https://tonydeng.gitbooks.io/sdn/content/mininet/)

## BitTorrent
- [基于 Python 3.5 的 BitTorrent 客户端](https://docs.liangz.org/zh-cn/latest/Python/BitTorrent-client-in-Python3.5/A-BitTorrent-client-in-Python-3.5.html)

- [本文档是对 Bittorrent Protocol Specification v1.0 的翻译](https://github.com/fenying/bittorrent-specification-chinese-edition/tree/master)

