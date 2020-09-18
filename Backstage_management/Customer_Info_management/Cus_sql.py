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


	def Has_cus(self,FaceID):
		
		self.__My_cursor.execute("SELECT ID FROM Customer_Info WHERE FACEID = %s "% (FaceID))
		
		Mycheck=self.__My_cursor.fetchall();
		#print(Mycheck)
		if len(Mycheck) == 0:
			return False
		else:
			return True

	def Insert_Cus_Info(self,FaceID):
		self.__My_cursor.execute("ALTER TABLE Customer_Info")
		self.__My_cursor.execute("SELECT * FROM Customer_Info WHERE FACEID = %s " % (FaceID))
		x=self.__My_cursor.fetchone()
		if type(x)!=None:
			sql=("INSERT INTO Customer_Info (FACEID) VALUES ( %s)")
			val=([FaceID])
			self.__My_cursor.execute(sql , val)
			self.__My_con.commit()
		else:
			print("This person already in record")

	def Del_Cus_Info_Face(self,FaceID):
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

	def Get_Id(self,FaceID):
		ID=-1
		self.__My_cursor.execute("ALTER TABLE Customer_Info")
		self.__My_cursor.execute("SELECT ID FROM Customer_Info WHERE FACEID = %s " % FaceID)
		x=self.__My_cursor.fetchall()
		ID=x[0]
		ID=ID[0]
		return ID
		


	def Renew_Cart(self,New_list:list):
		#New_List is Global_var.Pur_History_List
		self.__My_cursor=self.__My_con.cursor()
		self.__My_cursor.execute("select COLUMN_NAME from information_schema.COLUMNS where table_name = 'Cart'")
		Old_List=[]
		for x in self.__My_cursor:
			y=list(x)
			print(y)
			Old_List.append(y[0])

		for x in Old_List:
			if x not in New_list:
				self.__My_cursor.execute("ALTER TABLE Cart DROP COLUMN %s" % (x))
				self.__My_con.commit()

		for New_item in New_list:
			if New_item not in Old_List:
				print(New_item)
				sql="ALTER TABLE Cart add COLUMN  %s INT UNSIGNED DEFAULT 0"
				val=(New_item)
				self.__My_cursor.execute(sql % val)
				self.__My_con.commit()


	# def CLear_Cart(self,Del_list:list):
	# 	self.__My_cursor=self.__My_con.cursor()

	# 	for Del_item in Del_list:
	# 		sql="ALTER TABLE Cart DROP COLUMN %s"
	# 		val=(Del_item)
	# 		self.__My_cursor.execute(sql % val)
	# 		self.__My_con.commit()

	def Create_cart(self,ID):
		self.__My_cursor=self.__My_con.cursor()
		self.__My_cursor.execute("INSERT INTO Cart (ID) VALUES (%s)" % (ID))
		self.__My_con.commit()


	def Add_to_cart(self,ID,Pur_dict:dict):
		self.__My_cursor=self.__My_con.cursor()
		#check if this customer has a row in cart
		self.__My_cursor.execute("SELECT * FROM Cart WHERE ID = %s",([ID]))
		Mycheck=self.__My_cursor.fetchall()
		if len(Mycheck) == 0:
			print("Invalid ID: "+str(ID))
			return

		for item in Pur_dict:
			# print(item)
			self.__My_cursor.execute("SELECT %s FROM Cart WHERE ID = %s" % (item,ID))
			Origin_val=self.__My_cursor.fetchall()
			Origin_val=list(Origin_val[0])
			# print(Origin_val)
			New_val=Origin_val[0]+Pur_dict[item]
			# print(New_val)
			self.__My_cursor.execute("UPDATE Cart SET %s = %s WHERE ID = %s" % (item,New_val,ID))
			self.__My_con.commit()

	def Drop_cus_cart(self,ID):
		self.__My_cursor=self.__My_con.cursor()
		self.__My_cursor.execute("DELETE FROM Cart WHERE ID = %s" % (ID))
		self.__My_con.commit()

	def Renew_Pur_History(self,New_list):
		#New_List is Global_var.Pur_History_List
		self.__My_cursor=self.__My_con.cursor()
		self.__My_cursor.execute("select COLUMN_NAME from information_schema.COLUMNS where table_name = 'Pur_History'")
		Old_List=[]
		for x in self.__My_cursor:
			y=list(x)
			print(y)
			Old_List.append(y[0])

		for x in Old_List:
			if x not in New_list:
				self.__My_cursor.execute("ALTER TABLE Pur_History DROP COLUMN %s" % (x))
				self.__My_con.commit()
				#for table value
				self.__My_cursor.execute("ALTER TABLE Value DROP COLUMN %s" % (x))
				self.__My_con.commit()
		for New_item in New_list:
			if New_item not in Old_List:
				#print(New_item)
				sql="ALTER TABLE Pur_History add COLUMN  %s INT UNSIGNED DEFAULT 0"
				val=(New_item)
				self.__My_cursor.execute(sql % val)
				self.__My_con.commit()
				#for table value
				sql="ALTER TABLE Value add COLUMN  %s INT UNSIGNED DEFAULT 0"
				val=(New_item)
				self.__My_cursor.execute(sql % val)
				self.__My_con.commit()


	def Create_Pur_His(self,ID):
		self.__My_cursor=self.__My_con.cursor()
		self.__My_cursor.execute("INSERT INTO Pur_History (ID) VALUES (%s)" % (ID))
		self.__My_con.commit()
		self.__My_cursor.execute("INSERT INTO Value (ID) VALUES (%s)" % (ID))
		self.__My_con.commit()

	def Add_to_Pur_His(self,ID,Pur_dict):
		self.__My_cursor=self.__My_con.cursor()
		#check if this customer has a row in cart
		self.__My_cursor.execute("SELECT * FROM Pur_History WHERE ID = %s",([ID]))
		Mycheck=self.__My_cursor.fetchall()
		if len(Mycheck) == 0:
			print("Invalid ID: "+str(ID))
			return

		for item in Pur_dict:
			self.__My_cursor.execute("SELECT %s FROM Pur_History WHERE ID = %s" % (item,ID))
			Origin_val=self.__My_cursor.fetchall()
			Origin_val=list(Origin_val[0])
			New_val=Origin_val[0]+Pur_dict[item]
			self.__My_cursor.execute("UPDATE Pur_History SET %s = %s WHERE ID = %s" % (item,New_val,ID))
			self.__My_con.commit()

			self.__My_cursor.execute("UPDATE Value SET %s = %s WHERE ID = %s" % (item,New_val,ID))
			self.__My_con.commit()
		
		self.__My_cursor.execute("UPDATE Pur_History SET Last_Time = %s WHERE ID = %s" % (datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),ID))
		self.__My_con.commit()

	def Settlement(self,ID,Cart):
		# This function is useless now 
		self.__My_cursor=self.__My_con.cursor()
		for x in Global_var.Commodity_list:
			# print(x)
			self.__My_cursor.execute("SELECT %s FROM Cart WHERE ID = %s  " % (x,ID))
			This_Cart=self.__My_cursor.fetchall()
			This_Cart=list(This_Cart[0])
			

			
			self.__My_cursor.execute("SELECT %s FROM Pur_History WHERE ID = %s" % (x,ID))
			Origin_val=self.__My_cursor.fetchall()
			Origin_val=list(Origin_val[0])

			Now_val=This_Cart[0]+Origin_val[0]
			
			self.__My_cursor.execute("UPDATE Pur_History SET %s = %s WHERE ID =%s" % (x,Now_val,ID))
			self.__My_con.commit()

		# self.__My_cursor.execute("DELETE FROM Cart WHERE ID = %s ",([ID]))
		self.__My_con.commit()

if __name__=="__main__":

	con1=Connection_customer()
	con1.Connect_to_customer()
# # #con1.Show_tables()
# # #con1.Use_table("Cart")
	
# con1.Del_Cus_Info_Id(999)
# Del=['Apple']
# #print(Global_var.Commodity_list)
# #con1.Renew_Cart(Global_var.Cart_list)
# #con1.Del_Cart(Del)
	a=con1.Get_Id(1597824723)
	print(a)
# # con1.Create_Pur_His(1)
# # con1.Creat_cart(1)
# # con1.Add_to_cart(1,{'Apple':1,'Cola':2})
# #con1.Drop_cus_cart(1)
# #con1.Renew_Cart(Global_var.Cart_list)
# #con1.Renew_Pur_History(Global_var.Pur_History_List)
# #con1.Add_to_Pur_His(1,{'Apple':1,'Cola':2})

# con1.Insert_Cus_Info(23)
# con1.Creat_cart(1)
# con1.Add_to_cart(1,{'Chips':1,'Moutai':2})
# #con1.Drop_cus_cart(1)
# #con1.Renew_Cart(Global_var.Cart_list)
# #con1.Renew_Pur_History(Global_var.Pur_History_List)
# #con1.Add_to_Pur_His(1,{'Apple':1,'Cola':2})

# con1.Settlement(1)
