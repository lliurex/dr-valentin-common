import os
import shutil
import pwd

class DrValentinCommon:
	
	
	def __init__(self):
		
		pass
		
	#init
	
	def get_var_log(self,dst,user=None):
		
		try:
			shutil.copytree("/var/log",dst)
		
			if user!=None:
				
				cmd="chown -R %s:%s '%s'"%(user,user,dst)
				os.system(cmd)				

			return True
				
		except Exception as e:
			print e
			return False
		
	#def get_var_log



