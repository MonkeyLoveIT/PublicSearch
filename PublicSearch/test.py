import psycopg2

# 连接到 PostgreSQL 数据库
conn = psycopg2.connect(
    host="localhost",
    port="5432",
    dbname="postgres",
    user="eddy",
    password="19970109"
)

# 创建一个游标对象
cursor = conn.cursor()

# 执行查询语句
query = "SELECT * FROM firstapp_book"
cursor.execute(query)

# 获取查询结果
result = cursor.fetchall()

# 打印查询结果
for row in result:
    print(row)

# 关闭游标和连接
cursor.close()
conn.close()
