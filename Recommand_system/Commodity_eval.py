sys.path.append('/Users/ouyangyikang/unmanned_retail_project')
import mysql.connector
import sys
import Global_var
import pandas as pd
import numpy as np
# use first-time motecarlo

class Commodity_eval(threading.Thread,object):

	def __init__(self,ID,Rcmd_list,state_sample):
		threading.Thread.__init__(self)
		self.__My_con=None
		self.__My_cursor=None
		Connect_Value()

	def Connect_Value(self):
		try:
			self.__My_con=mysql.connector.connect(
				host="localhost",
				user="Value",
				passwd="123456"
				)
		except ConnectionError as e:
			print("Connection Error",e)

		self.__My_cursor=self.__My_con.cursor()

		try:
			self.__My_cursor.execute("USE Customer")

		except ConnectionError as e:
			print("Choose database Error",e)

class Mc_Thread(threading.Thread,object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(ClassName, self).__init__()
		self.arg = arg
		
'''
		self.ID=ID
		self.state_sample=state_sample
		#sort sample by shelf
		self.state_sample.insert(0,'Start')
		self.state_sample.append('End')
		# self.Rcmd_list=Rcmd_list
		#the recommand goods by zcr's alogrithoms
		self.state_list=Global_var.Commodity_list
		self.state_list.append('Start')
		self.state_list.append('End')

		self.Reward=pd.Series(-1,index=self.state_list)
		for item in state_sample:
			Reward[item]=state_sample[item]

'''