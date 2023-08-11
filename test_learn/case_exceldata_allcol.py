import requests
import xlwings as xw
import json
from common.method import ApiRequest
from config.parse_ini import ParseIni

# 打开excel文件——方法1
app = xw.App(visible=False, add_book=False)
wb = app.books.open('../test_data/data_excel.xlsx')

# 打开excel文件——方法2
# wb = xw.Book('../test_data/data_excel.xlsx')

sheet = wb.sheets[0]
# 或sheet = wb.sheets['Sheet1']
info = sheet.used_range
# 行数
nrows = info.last_cell.row
# 列数
ncloumns = info.last_cell.column
print(nrows, ncloumns)


a = ApiRequest()
p = ParseIni()
url_prefix = p.geturl('../config/conf.ini', 'url', 'swagger_url')


# colum = sheet.range('A3:F3').value
# urlp = url_prefix + colum[2]
# print(type(colum[4]), colum[4], json.loads(colum[4]), type(json.loads(colum[4])))
# rp = requests.request(colum[1], urlp, data=json.loads(colum[4]))
# print(rp.status_code)

for i in range(2, nrows+1):
    # 根据params，确定请求url
    column_datat = sheet.range('A%s:F%s' % (i, i)).value
    if column_datat[3] is not None:
        url = url_prefix + column_datat[2] + str(int(column_datat[3]))
    else:
        url = url_prefix + column_datat[2]

    # 根据有无body，执行请求
    if column_datat[4] is not None:
        r = a.send_request(column_datat[1], url, json.loads(column_datat[4]))
    else:
        r = a.send_request(column_datat[1], url)

    # 响应状态码为200时，在最后一列写入结果标识“PASSED"，否则写入”Failed“
    if r.status_code == 200:
        sheet.range('F%s' % i).value = 'PASSED'
    else:
        sheet.range('F%s' % i).value = 'Failed'

wb.save()

wb.close()
app.quit()
print("It's all over!!!")
