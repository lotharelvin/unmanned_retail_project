sys.path.append('/Users/ouyangyikang/unmanned_retail_project')
import Global_var
import pandas as pd
import numpy as np


class Commodity_eval(object):
	"""docstring for Commodity_eval"""
	def __init__(self,Rcmd_list,state_sample):
		self.state_sample=state_sample
		self.state_sample.insert(0,'Start')
		self.state_sample.append('End')

		self.Rcmd_list=Rcmd_list
		#the recommand goods by zcr's alogrithoms
		self.state_list=Global_var.Commodity_list
		self.state_list.append('Start')
		self.state_list.append('End')

		self.Value=pd.Series(0,index=self.state_list)
		self.Reward=pd.Series(-1,index=self.state_list)
		for x in Rcmd_list:
			Reward[x]=1


