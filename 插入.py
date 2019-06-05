#coding = utf-8
'''
    python操作mysql数据库
    @name:数据库操作
    @function:执行SQL
    @author:Mr.Zheng
    @date:2018-11-01
'''
# 插入操作
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
# print(cur)
# 步骤三:执行sql语句
id = 3
name = "lisi"
import time
nowtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
# 处理异常
try:
    # res = cur.execute("insert into demo4 values('{0}')".format(name))
    # 占位符模式
    # res = cur.execute("insert into demo4 values('%s')" %(name))
    # 多占位符模式
    #本句重点,主要修改的内容
    res = cur.execute("insert into demo5 values('%d','%s','%s')" % (id,name,nowtime))
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