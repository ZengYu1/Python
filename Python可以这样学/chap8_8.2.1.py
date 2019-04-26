# coding=gbk
# 建立数据库连接
import win32com.client
conn = win32com.client.Dispatch(r'ADODB.Connection')
DSN = 'PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = E:/DataBase/MyDB.mdb;'
conn.Open(DSN)

#打开记录集
rs = win32com.client.Dispatch(r'ADODB.Recordset')
rs_name = 'MyRecordset'
rs.Open('['+rs_name+']', conn, 1, 3)

#操作记录集
rs.AddNew()
rs.Fileds.Item(1).Value = 'data'
rs.Update()

#操作数据
conn = win32com.client.Dispatch(r'ADODB.Connection')
DSN = 'PROVIDER = Microsof.Jet.OLEDB.4.0;DATA SOURCE = E:/DataBase/MyDB.mdb;'
sql_statement = "INSERT INTO [Table_Name]([Field_1],[Field_2]) VALUES('data1', 'data2')"
conn.Open(DSN)
conn.Execute(sql_statement)
conn.Close()

# 遍历记录
rs.MoveFirst()
count = 0
while 1:
    if rs.EOF:
        break
    else:
        count = count +1
    rs.MoveNext()


