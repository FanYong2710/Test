#coding = utf-8
'''
    python操作mysql数据库
    @name:数据库操作
    @function:执行SQL
    @author:Mr.Zheng
    @date:2018-11-01
'''
# 查询操作
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
    res = cur.execute("select dname,e.sal from dept,(select deptno,avg(sal) sal from emp group by deptno having sal > 1600)e where dept.deptno = e.deptno")
    print(res)
    # 显示第一条记录
    # res = cur.fetchone()
    # 显示所有记录（元组）
    res = cur.fetchall()
    # 遍历数据
    for i in res:
        for j in range(len(i)):
            print(i[j],end="\t")
        print()
except:
    # 回退事务
    con.rollback()
    print(">>事务回退成功")

# 步骤四:关闭数据库连接
cur.close()
con.close()
