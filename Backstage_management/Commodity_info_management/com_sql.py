import pymysql
import mysql.connector
def create_table():
    # 创建连接
    conn = pymysql.connect(host='localhost',user='root',password='001015',charset='utf8mb4')
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
def insert_into():
    print("插入数据库操作！")
    db = pymysql.connect("localhost","root","001015","commodity")
    cursor = db.cursor()
    
    #批量插入数据
    sql = """INSERT INTO comm VALUES(%s,%s,%s,%s,%s)"""
    ID=input("请输入 id号： ")
    Price=input("请输入 price： ")
    Inventory=input("请输入 Inventory： ")
    Shelf=input("请输入 Shelf：" )
    Type=input("请输入 Type:")
    params = [
        (ID,Price,Inventory,Shelf,Type),
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
        
def select_form():
    print("查询数据库操作！")
    # 打开数据库连接
    db = pymysql.connect("localhost","root","001015","commodity")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    n=input("请输入查询的ID：")
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
            Pice = row[1]
            Inventory = row[2]
            Shelf = row[3]
            Type= row[4]
            print("ID=%s,Pice=%s,Inventory=%s,Shelf=%s,Type=%s"%\
                  (ID,Pice,Inventory,Shelf,Type))

    except Exception as e:
        print("查询出错：case%s"%e)

    finally:
        # 关闭游标连接
        cursor.close()
        # 关闭数据库连接
        db.close()

def Update_Set():
    #打开数据库链接
    print("更新数据库操作！")
    db = pymysql.connect("localhost","root","001015","commodity")

    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    id=input("请输入ID: ")
    print("1代表Price，2代表Inventory，3代表Shelf，4代表Type")
    n=int(input("请输入你要更新的选项："))  

    if(n==1):
    #SQL语句更新数据
        price=input("请输入 price： ")
        sql = """UPDATE comm SET Price = %s WHERE ID = %s"""%(price,id)
    elif(n==2):
        inventory=input("请输入 Inventory： ")
        sql = """UPDATE comm SET Inventory = %s WHERE ID = %s"""%(inventory,id)
    elif(n==3):
        shelf=input("请输入 Shelf： ")
        sql = """UPDATE comm SET Shelf = %s WHERE ID = %s"""%(shelf,id)
    else:
        type=input("请输入 Type:")
        sql = """UPDATE comm SET Type = %s WHERE ID = %s"""%(type,id)

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
def Delete_From():
    #打开数据库链接
    db = pymysql.connect("localhost","root","001015","commodity")
    print("删除数据库操作！")
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    ID=input("请输入ID: ")
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
def main():
    create_table()
    print("请输入你要进行的操作：\n1:代表插入数据，\n2:代表查询数据，\n3:代表更新数据，\n4:代表删除数据。\n0:代表退出数据库操作")
    n=int(input("请输入："))
    
    while(n!=0):
        
        while(n==1 and n!=5):
            insert_into()
            print("请输入你要进行的操作：\n1:代表插入数据，\n2:代表查询数据，\n3:代表更新数据，\n4:代表删除数据。\n5:代表退出当前操作")
            n=int(input("请输入："))
        while(n==2 and n!=5):
            select_form()
            print("请输入你要进行的操作：\n1:代表插入数据，\n2:代表查询数据，\n3:代表更新数据，\n4:代表删除数据。\n5:代表退出当前操作")
            n=int(input("请输入："))
        while(n==3 and n!=5):
            Update_Set()
            print("请输入你要进行的操作：\n1:代表插入数据，\n2:代表查询数据，\n3:代表更新数据，\n4:代表删除数据。\n5:代表退出当前操作")
            n=int(input("请输入："))
        while(n==4 and n!=5):
            Delete_From()
            print("请输入你要进行的操作：\n1:代表插入数据，\n2:代表查询数据，\n3:代表更新数据，\n4:代表删除数据。\n5:代表退出当前操作")
            n=int(input("请输入："))
        print("请输入你要进行的操作：\n1:代表插入数据，\n2:代表查询数据，\n3:代表更新数据，\n4:代表删除数据。\n0:代表退出数据库操作")
        n=int(input("请输入："))
if __name__ == "__main__":
    main()
