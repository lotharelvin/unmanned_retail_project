import mysql.connector
import sys
sys.path.append('/Users/ouyangyikang/unmanned_retail_project')
import Global_var

class Connection_customer(object):
	"""docstring for Connection_sql"""
	def __init__(self):
		super(Connection_customer, self).__init__()
		self.__My_con=None
		self.__My_cursor=None
		


	def Connect_to_customer(self):
		try:
			self.__My_con=mysql.connector.connect(
				host="localhost",
				user="root",
				passwd="123456aa"
				)
		except ConnectionError as e:
			print("Connection Error",e)

		self.__My_cursor=self.__My_con.cursor()

		try:
			self.__My_cursor.execute("USE Customer")

		except ConnectionError as e:
			print("Choose database Error",e)

	def Show_tables(self):
		if self.__My_con is None:
			print("Connection unestablished")
			return 
		else:
			self.__My_cursor.execute("SHOW TABLES")
			for x in self.__My_cursor:
				print(x)

	def Use_table(self,Table_name:str):
		if Table_name not in Global_var.Customer_table_type:
			print("Wrong Table Name")
			return
		else:
			self.__My_cursor.execute("ALTER TABLE "+Table_name)
			print(self.__My_cursor)


	def Insert_Cus_Info(self,FaceID:str):
		self.__My_cursor.execute("ALTER TABLE Customer_Info")
		sql=("INSERT INTO Customer_Info (FACEID) VALUES ( %s )")
		val=([FaceID])
		self.__My_cursor.execute(sql , val)
		self.__My_con.commit()

	def Del_Cus_Info_Face(self,FaceID:str):
		self.__My_cursor.execute("ALTER TABLE Customer_Info")
		sql=("DELETE FROM Customer_Info WHERE FACEID = %s")
		val=([FaceID])
		self.__My_cursor.execute(sql,val)
		self.__My_con.commit()

	def Del_Cus_Info_Id(self,ID):
		self.__My_cursor.execute("ALTER TABLE Customer_Info")
		sql=("DELETE FROM Customer_Info WHERE ID = %s")
		val=([ID])
		self.__My_cursor.execute(sql , val)
		self.__My_con.commit()

	def Renew_Cart(self,New_list:list):
		self.__My_cursor=self.__My_con.cursor()
		self.__My_cursor.execute("select COLUMN_NAME from information_schema.COLUMNS where table_name = 'Cart'")
		Old_List=[]
		for x in self.__My_cursor:
			y=list(x)
			print(y)
			Old_List.append(y[0])

		for New_item in New_list:
			if New_item not in Old_List:
				sql="ALTER TABLE Cart add COLUMN  %s INT UNSIGNED DEFAULT 0"
				val=(New_item)
				self.__My_cursor.execute(sql % val)
				self.__My_con.commit()


	def Del_Cart(self,Del_list:list):
		self.__My_cursor=self.__My_con.cursor()

		for Del_item in Del_list:
			sql="ALTER TABLE Cart DROP COLUMN %s"
			val=(Del_item)
			self.__My_cursor.execute(sql % val)
			self.__My_con.commit()
		


con1=Connection_customer()
con1.Connect_to_customer()
#con1.Show_tables()
#con1.Use_table("Cart")
#con1.Insert_Cus_Info("22")
#con1.Del_Cus_Info_Id(999)
Del=['Apple']
#print(Global_var.Commodity_list)
con1.Renew_Cart(Global_var.Commodity_list)
con1.Del_Cart(Del)




	

