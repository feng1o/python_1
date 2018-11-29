#coding:utf-8
'''reboot_mysqld.py'''
import requests
import json
import time
from .query_reboot_mysqld import *
from base import *

def reboot_mysqld(instance_id="", reboot_role="ALL",operator="autotest"):
#def reboot_mysqld(instanceids="[]", reboot_role="[]",operator="autotest"):
	logger_default.info(">>>>>>>> api : reboot_mysqld")
	configclass = configClass()
	web_ip = configclass.web_ip
	web_port = configclass.web_port   
	
	url = "http://"+web_ip+":"+str(web_port)+"/cdb2/fun_logic/cgi-bin/public_api_20/reboot_mysqld.cgi"
	params_json = {}
	params_json['instanceid'] = instance_id 
	params_json['reboot_role'] = reboot_role 
	params_json['operator'] = operator 
	data = "data=%s" % json.dumps(params_json)
	headers = {"Content-Type": "application/x-www-form-urlencoded"} 
	r = requests.post(url=url, data=data, headers=headers)
	reboot_mysqld_return = json.loads(r.text)
	#logger_default.info(reboot_mysqld_return)
	logger_default.info(r.text)
	# logger_default.info(reboot_mysqld_return)
	if reboot_mysqld_return['errno'] != 0 :
		# logger_default.info reboot_mysqld_return
		return 0, reboot_mysqld_return
	logger_default.info(">>>>>>>> api : query_reboot_mysqld")
	time.sleep(2)	

	for inst in instance_id.split('|'):	
		(status, reboot_mysqld_query_return) = query_reboot_mysqld(work_id=reboot_mysqld_return['workid'], instance_id=inst)
		return reboot_mysqld_query_return["errno"], reboot_mysqld_query_return
	pass
