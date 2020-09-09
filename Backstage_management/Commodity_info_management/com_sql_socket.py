import pymysql
import mysql.connector
def create_table():
    # 创建连接
    conn = pymysql.connect(host='localhost',user='root',password='428016',charset='utf8mb4')
    # 创建游标
    cursor = conn.cursor()
    # 创建数据库的sql(如果数据库存在就不创建，防止异常)
    sql = "CREATE DATABASE IF NOT EXISTS commodity" 

    # 执行创建数据库的sql
    cursor.execute(sql)
    #连接本地数据库
    db = pymysql.connect("localhost","root","428016","commodity")

    #创建游标
    cursor = db.cursor()
    #如果存在comm表，则删除
    cursor.execute("DROP TABLE IF EXISTS comm")

    #创建comm表
    sql = """
        CREATE TABLE comm (
		ID int(255),
		Name varchar(255),
		Price float(10),
                Inventory int(255),
		Shelf int(255),
                Type  varchar(255)
		);
    """

    try:
        # 执行SQL语句
        cursor.execute(sql)
        print("创建数据库成功")
    except Exception as e:
        print("创建数据库失败：case%s"%e)
    finally:
        #关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()
def insert_into(ID,Name,Price,Inventory,Shelf,Type):
    print("插入数据库操作！")
    db = pymysql.connect("localhost","root","428016","commodity")
    cursor = db.cursor()
    
    #批量插入数据
    sql = """INSERT INTO comm VALUES(%s,%s,%s,%s,%s,%s)"""
    params = [
        (ID,Name,Price,Inventory,Shelf,Type),
    ]

    try:
        # 执行SQL语句
        cursor.executemany(sql,params)
        # 提交到数据库执行
        db.commit()
        print("插入数据成功")
    except Exception as e:
        print("插入数据失败：case%s"%e)
        # 如果发生错误则回滚
        db.rollback()
    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()
        
def select_form(ID):
    print("查询数据库操作！")
    # 打开数据库连接
    db = pymysql.connect("localhost","root","428016","commodity")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    n=ID
    # SQL 查询语句
    sql = """SELECT * FROM comm WHERE ID = %s"""%(n)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        print("开始查询：")
        # 获取所有记录列表
        results = cursor.fetchall()
        if(not len(results)):
            print("暂无此ID")
        for row in results:
            ID = row[0]
            Name = row[1]
            Pice = row[2]
            Inventory = row[3]
            Shelf = row[4]
            Type= row[5]
            print("ID=%s,Name=%s,Pice=%s,Inventory=%s,Shelf=%s,Type=%s"%\
                  (ID,Name,Pice,Inventory,Shelf,Type))

    except Exception as e:
        print("查询出错：case%s"%e)

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()

def Update_Set_Name(ID,New_Name):         # 更改商品名
    #打开数据库链接
    print("更新数据库操作 更改商品名称！")
    db = pymysql.connect("localhost","root","428016","commodity")
    id=ID
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    #SQL语句更新数据
    sql = """UPDATE comm SET Name = '%s' WHERE ID = %s"""%(New_Name,id)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("更新数据成功")

    except Exception as e:
        print("数据更新出错：case %s"%e)
        #发生错误是回滚
        db.rollback()

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()

def Update_Set_Price(ID,New_Price):      #更改商品价格
    #打开数据库链接
    print("更新数据库操作 更改商品价格！")
    db = pymysql.connect("localhost","root","428016","commodity")
    id=ID
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    #SQL语句更新数据
    sql = """UPDATE comm SET Price = %s WHERE ID = %s"""%(New_Price,id)
   
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("更新数据成功")

    except Exception as e:
        print("数据更新出错：case %s"%e)
        #发生错误是回滚
        db.rollback()

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()

def Update_Set_Inventory(ID,New_Inventory):      #更改商品库存
    #打开数据库链接
    print("更新数据库操作 更改商品库存！")
    db = pymysql.connect("localhost","root","428016","commodity")
    id=ID
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    #SQL语句更新数据
    sql = """UPDATE comm SET Inventory = %s WHERE ID = %s"""%(New_Inventory,id)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("更新数据成功")

    except Exception as e:
        print("数据更新出错：case %s"%e)
        #发生错误是回滚
        db.rollback()

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()

def Update_Set_Shelf(ID,New_Inventory):      #更改商品货架号
    #打开数据库链接
    print("更新数据库操作 更改商品库存！")
    db = pymysql.connect("localhost","root","428016","commodity")
    id=ID
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    #SQL语句更新数据
    sql = """UPDATE comm SET Shelf = %s WHERE ID = %s"""%(New_Inventory,id)
    #else:
     #   sql = """UPDATE comm SET Type = %s WHERE ID = %s"""%(value,id)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("更新数据成功")

    except Exception as e:
        print("数据更新出错：case %s"%e)
        #发生错误是回滚
        db.rollback()

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()

def Update_Set_Type(ID,New_Type):         # 更改商品类型
    #打开数据库链接
    print("更新数据库操作 更改商品类型！")
    db = pymysql.connect("localhost","root","428016","commodity")
    id=ID
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    #SQL语句更新数据
    sql = """UPDATE comm SET Type = '%s' WHERE ID = %s"""%(New_Type,id)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("更新数据成功")

    except Exception as e:
        print("数据更新出错：case %s"%e)
        #发生错误是回滚
        db.rollback()

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()

def Delete_From(ID):
    #打开数据库链接
    db = pymysql.connect("localhost","root","428016","commodity")
    print("删除数据库操作！")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL语句更新数据
    sql = """DELETE FROM comm WHERE ID = %s"""%(ID)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
        print("删除数据成功")

    except Exception as e:
        print("删除数据失败：case%s"%e)
        #发生错误时回滚
        db.rollback()

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()
#def main():                 用于测试各个函数是否正常
    #create_table()                          #建表
    #insert_into(1,'yagao',15,100,1,'per')    #输入商品信息
    #select_form(1)                           #查询信息
    #Update_Set_Name(1,'nige')                #更改商品名称
    #Update_Set_Price(1,10)                   #更改商品价格
    #Update_Set_Inventory(1,99)               #更改商品库存
    #Update_Set_Shelf(1,2)                    #更改商品货架号
    #Update_Set_Type(1,'personal_care')       #更改商品类行
    #Delete_From(1)                          #从库中删除商品

#if __name__ == "__main__":
    #main()
