import builtwith
import whois  #ouwer 也可以通过urlib.request.urlopen()来看

print(builtwith.parse("http://baidu.com"))
print(whois.whois("souhu.com"))
