import defines 
import threading
import time
import Cus_sql
import sys
sys.path.append('/Users/ouyangyikang/unmanned_retail_project')
import Global_var

Cus_con=Cus_sql.Connection_customer()
class Cus_exe_thd(threading.Thread,object):
	def __init__(self,FaceID):
		self.__This_face=FaceID
		

	def Check_cus():
		flag=cus_con.Has_cus()
		if flag== True:
			cus_con.Insert_Cus_Info

	
		


