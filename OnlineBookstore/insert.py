# -*- coding: utf-8 -*-
import psycopg2
# 获得连接
conn = psycopg2.connect(database="OnlineBookstore", user="postgres", password="root", host="localhost", port="5432")
# 获得游标对象，一个游标对象可以对数据库进行执行操作
cur = conn.cursor()

sql = """INSERT INTO product_product (name, price)
         VALUES (%s, %s);"""

# 插入数据
data_to_insert = ('Book B',29.99)
cur.execute(sql, data_to_insert)

# 提交事务
conn.commit()

# 关闭游标和连接
cur.close()
conn.close()