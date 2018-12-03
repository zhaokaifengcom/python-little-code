import xlrd
import requests
a = xlrd.open_workbook('1.xlsx','r') #打开.xlsx文件
sht = a.sheets()[0] #打开表格中第一个sheet
row1 = sht.row_values(0)

#设置要下载的图片的范围，对应于 Excel 中的行数
start = 0
end = 100

for i in range(start,end):
    url = sht.cell(i,2).value #依次读取每行第三列的数据，也就是 URL
    f = requests.get(url)

    ii = str(i) #按照下载顺序（行号）构造文件名

    url2 = url[-3:] #根据链接地址获取文件后缀，后缀有.jpg 和 .gif 两种

    dir = ii + "." + url2 #构造完整文件名称
    
    with open(dir,"wb") as code:
        code.write(f.content) #保存文件
    print(url) #打印当前的 URL

    jindu = (i - start) / (end - start) * 100 #计算下载进度
    print("下载进度：",jindu,"%") #显示下载进度
