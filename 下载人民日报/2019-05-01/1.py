import datetime
import requests
import string

for a in range(1, 21):
	if a < 10:
		b = str(a)
		b = '0'+b
	else:
		b = str(a)
	url = datetime.datetime.now().strftime('http://paper.people.com.cn/rmrb/page/%Y-%m/%d/'+b+'/rmrb%Y%m%d'+b+'.pdf')
	f = requests.get(url)
	c = b+'.pdf'
	with open(c, "wb") as code:
		code.write(f.content)


#检查网络连接
#创建文件夹
