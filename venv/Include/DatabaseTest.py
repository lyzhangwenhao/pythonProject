import pymysql.cursors

# 连接数据库
connect = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    db='zzqa_manager',
    charset='utf8'
)

# 获取游标
cursor = connect.cursor()


# 查询数据
sql = "SELECT * FROM user"
cursor.execute(sql)
result = cursor.fetchall()
for x in result:
    print(x)

# 关闭连接
cursor.close()
connect.close()