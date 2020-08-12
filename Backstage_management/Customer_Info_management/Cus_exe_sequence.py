import threading
import time
import Cus_sql
import sys
sys.path.append('/Users/ouyangyikang/unmanned_retail_project')
sys.path.append('/Users/ouyangyikang/unmanned_retail_project/Face_Recognition')
import Global_var
import defines 

Cus_con=Cus_sql.Connection_customer()
class Cus_exe_thd(threading.Thread,object):
	def __init__(self,FaceID,Thread_id):
		threading.Thread.__init__(self)
		self.__This_face=FaceID
		self.__This_id=None
		self.__This_Thread=Thread_id

	def Check_and_Cart():
		threadLock.acquire()
		flag=Cus_con.Has_cus()
		if flag== True:
			self.__This_id=Cus_con.Get_ID()
			Cus_con.Create_cart(__This_id)

		else:
			Cus_con.Insert_Cus_Info(__This_face)
			self.__This_id=Cus_con.Get_ID()
			Cus_con.Create_cart(__This_id)
			Cus_con.Create_Pur_His(__This_id)			
		threadLock.realease()

	def Shopping():
		pass
		#todo wait for shelf recognition
		#which should block here

	def Settlement():
		pass
		#wait for futher recognition


def main():
	People_inside=0;
	Thread_list=[]
	Face_list=[]
	while True:
		#keep listening here to acquire new people 
		FaceID=defines.get_cus_FaceID()
		if FaceID not in Face_list:
			Face_list.append(FaceID)
			Thread_temp=Cus_exe_thd(FaceID,People_inside)
			Thread_list.append(Thread_temp)
			People_inside+=1;
			
main()
	
		


