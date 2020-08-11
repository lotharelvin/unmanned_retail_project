class Commodity(object):
	"""docstring for Commodity"""
	def __init__(self, ID: int, Price: float, Inventory: int,Shelf: int,Type: str):
		super(Commodity, self).__init__()
		self.ID=ID
		self.Price=Price
		self.Inventory=Inventory
		self.Shelf=Shelf
		self.Type=Type

	def myprint(self):
				print("ID is",self.ID)
				print("Price is",self.Price)
				print("Inventory is",self.Inventory)
				print("Shelf is",self.Shelf)
				print("Type is",self.Type)

	def Change_ID(self,New_ID):
		self.ID=New_ID

	def Change_Price(self,New_Price):
		self.Price=New_Price

	def Add_Inventory(self,Incre):
		self.Inventory+=Incre

	def Dec_Inventory(self,Decre):
		self.Inventory-=Decre

	def Change_Shelf(self,New_Shelf):
		self.Shelf=New_Shelf

	def Change_Type(self,New_Type):
		self.Type=New_Type

	def Reset(self):
		self.ID=-1
		self.Price=-1
		self.Inventory=-1
		self.Shelf=-1
		self.Type=""
