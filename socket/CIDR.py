#_*_incoding:utf-8_*_
# CIDR（无类别域间路由，Classless Inter-Domain Routing）是一个在Internet上创建附加地址的方法，这些地址提供给服务提供商（ISP），再由ISP分配给客户。CIDR将路由集中起来，使一个IP地址代表主要骨干提供商服务的几千个IP地址，从而减轻Internet路由器的负担。

import  ipaddress  # ipaddress 模块有很多类可以表示IP地址、网络和接口。 当你需要操作网络地址（比如解析、打印、验证等）的时候会很有用。

# tip:ipaddress 模块跟其他一些和网络相关的模块比如 socket 库交集很少。 所以，你不能使用 IPv4Address 的实例来代替一个地址字符串，你首先得显式的使用 str() 转换它。
net = ipaddress.ip_network('123.45.67.64/27')
print(net)
for x in net:
	print(x)