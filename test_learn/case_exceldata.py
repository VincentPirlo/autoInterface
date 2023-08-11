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

column_data = sheet.range('A2:F2').value
print(column_data)

a = ApiRequest()
p = ParseIni()
url_prefix = p.geturl('../config/conf.ini', 'url', 'swagger_url')
url = url_prefix + column_data[2]
r = a.send_request(column_data[1], url)
print(json.dumps(r.json(), indent=2, ensure_ascii=False))
print(r.status_code)

A1 = sheet.range('A1').value
print(A1)
wb.close()
app.quit()


