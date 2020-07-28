import mysql.connector


class Connection_sql(object):
	"""docstring for Connection_sql"""
	def __init__(self):
		super(Connection_sql, self).__init__()
		self.__My_con=None
		


	def Connect_to_sql(self):
		try:
			__My_con=mysql.connector.connect(
				host="localhost",
				user="root",
				passwd="123456aa"
				)
		except ConnectionError as e:
			print("Connection Error",e)

	def Choose_database(self):
		pass

	

