import threading
import mysql.connector
import time
import Cus_sql
import sys
sys.path.append('/Users/ouyangyikang/unmanned_retail_project')
sys.path.append('/Users/ouyangyikang/unmanned_retail_project/Face_Recognition')
import Global_var
import defines 
import socket
import json


class Cus_exe_thd(threading.Thread,object):
	def __init__(self,FaceID,Thread_id,SQL_con):
		threading.Thread.__init__(self)
		self.__This_face=FaceID
		self.__This_id=None
		self.__This_Thread=Thread_id
		self.lock=threading.Lock()
		self.SQL_con=SQL_con
		self.stop_flag=False
	def Check_and_Cart(self):
		self.lock.acquire()
		flag=self.SQL_con.Has_cus(self.__This_face)
		print(flag)
		if flag== True:
			#old customer
			self.__This_id=self.SQL_con.Get_Id(self.__This_face)
		else:
			#new customer
			self.SQL_con.Insert_Cus_Info(self.__This_face)
			self.__This_id=self.SQL_con.Get_Id(self.__This_face)
			if self.__This_id!=-1:
				self.SQL_con.Create_cart(self.__This_id)
				self.SQL_con.Create_Pur_His(self.__This_id)	
				print("Add and Create done")	
			else:
				print("Invalid ID")	
		self.lock.release()
	def Shopping(self):
		pass
		#todo wait for shelf recognition
		#which should block here

	def Settlement(self,cart):
		self.SQL_con.Add_to_Pur_His(self.__This_id,cart)
		self.stop_flag=True
		#wait for futher recognition
		# make sure delete this people in cart and add timestamp to pur_history
	def run(self):
		self.Check_and_Cart()
		while self.stop_flag==False:
			pass
		print("Thread")
		print(self.Thread_id)
		print("exit")



class Main_thread(threading.Thread,object):
	"""docstring for Main_thread"""
	def __init__(self):
		threading.Thread.__init__(self)
		self._Cus_con=Cus_sql.Connection_customer()
		self._Cus_con.Connect_to_customer()
		self._People_in=0
		self._Thread_list=[]
		self._Face_list=[]
		self.Creation_thd=self.Create_cus_thread(self)
		self.Closure_thd=self.Close_cus_thread(self)
		self.Shopping_thd=self.Shopping_thread(self)
	class Create_cus_thread(threading.Thread,object):
		"""docstring for Create_thread"""
		def __init__(self, Main_thread):
			self.Main_thread=Main_thread
			threading.Thread.__init__(self)
			
		def Create(self):
			while True:
				print('detecting')
				FaceID=defines.get_capcus_FaceID()
				print(FaceID)
				if FaceID not in self.Main_thread._Face_list:
					if FaceID==0:
						continue
					self.Main_thread._Face_list.append(FaceID)
					Thread_temp=Cus_exe_thd(FaceID,self.Main_thread._People_in,self.Main_thread._Cus_con)
					self.Main_thread._Thread_list.append(Thread_temp)
					# Thread_temp.setDaemon(True)   
					Thread_temp.start()
					# Thread_temp.join()
					self.Main_thread._People_in+=1;
				else:
					print("This customer exists")
		def run(self):
			self.Create()


	class Shopping_thread(threading.Thread,object):
		def __init__(self,Main_thread):
			threading.Thread.__init__(self)
			self.Main_thread=Main_thread

		def Listen(self):
			s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.bind(('127.0.0.1',4396))
			s.listen(1)

			while True:
				try:
					c,c_addr=s.accept()
					while True:
						print("recv data")
						data=c.recv(1024).decode('utf-8')
						#print(data)
						try:
							cart_info=json.loads(data)
							#print(cart_info)
							#loads successfully
						except json.decoder.JSONDecodeError:
							break
						FaceID=cart_info['Face_ID']
						if FaceID==0:
							break

						cart={}
						for good in cart_info["Cart"]:
							if good in cart:
								cart[good]+=1
							else:
							 	cart[good]=1
						Face_idx=self.Main_thread._Face_list.index(FaceID)
						This_cus_thd=self.Main_thread._Thread_list[Face_idx]
						This_cus_thd.Settlement(cart)
						
						#print(cart)
						# close this thd
						This_cus_thd.stop_flag=True
						self.Main_thread._Face_list.remove(Face_idx)
						self.Main_thread._Thread_list.remove(This_cus_thd)
				except KeyboardInterrupt:
					print("Quit")


		def run(self):
			self.Listen()
					
			
	class Close_cus_thread(threading.Thread,object):
		"""docstring for Create_thread"""
		def __init__(self, Main_thread):
			threading.Thread.__init__(self)
			self.Main_thread=Main_thread
		#todo :wait for settlement signal to close a thread



	def run(self):
		self._Cus_con.Renew_Pur_History(Global_var.Pur_History_List)
		self.Creation_thd.start()
		self.Shopping_thd.start()






def main():
	Main_thd=Main_thread()
	Main_thd.start()


if __name__ == '__main__':			
	main()
	
		


