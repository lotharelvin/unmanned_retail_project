import mysql.connector


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

	def Use_table(self,Table_name):
		self.__My_cursor.execute("ALTER TABLE "+Table_name)
		print(self.__My_cursor)

		


con1=Connection_customer()
con1.Connect_to_customer()
con1.Show_tables()
con1.Use_table("dx")



	

