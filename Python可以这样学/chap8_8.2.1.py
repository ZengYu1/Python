# coding=gbk
# �������ݿ�����
import win32com.client
conn = win32com.client.Dispatch(r'ADODB.Connection')
DSN = 'PROVIDER = Microsoft.Jet.OLEDB.4.0;DATA SOURCE = E:/DataBase/MyDB.mdb;'
conn.Open(DSN)

#�򿪼�¼��
rs = win32com.client.Dispatch(r'ADODB.Recordset')
rs_name = 'MyRecordset'
rs.Open('['+rs_name+']', conn, 1, 3)

#������¼��
rs.AddNew()
rs.Fileds.Item(1).Value = 'data'
rs.Update()

#��������
conn = win32com.client.Dispatch(r'ADODB.Connection')
DSN = 'PROVIDER = Microsof.Jet.OLEDB.4.0;DATA SOURCE = E:/DataBase/MyDB.mdb;'
sql_statement = "INSERT INTO [Table_Name]([Field_1],[Field_2]) VALUES('data1', 'data2')"
conn.Open(DSN)
conn.Execute(sql_statement)
conn.Close()

# ������¼
rs.MoveFirst()
count = 0
while 1:
    if rs.EOF:
        break
    else:
        count = count +1
    rs.MoveNext()


