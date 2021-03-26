import os
import shutil
import pwd
import n4d.responses

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

			return n4d.responses.build_successful_call_response()
				
		except Exception as e:
			print(str(e))
			return n4d.responses.build_failed_call_response()
		
	#def get_var_log



