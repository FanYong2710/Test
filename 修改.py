#coding = utf-8
'''
    python操作mysql数据库
    @name:数据库操作
    @function:执行SQL
    @author:Mr.Zheng
    @date:2018-11-01
'''
# 修改操作
import pymysql
# 步骤一:建立连接
con = pymysql.connect(host="localhost",port=3306,user="root",passwd="root",db="db_test")
#判断连接状态
if con:
    print(">>数据库连接成功！")
else:
    print(">>数据库连接失败！")
# 步骤二:获取游标对象
cur = con.cursor()
try:
    # 步骤三:执行SQL语句
    res = cur.execute("update emp set sal=3000 where ename='zs'")
    print(res)
    # 提交事务
    con.commit()
    print(">>事务提交成功")
except:
    # 回退事务
    con.rollback()
    print(">>事务回退成功")

# 步骤四:关闭数据库连接
cur.close()
con.close()
