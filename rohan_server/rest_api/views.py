from django.shortcuts import render
from django.views import generic
import pdb
import json

from django.http import HttpResponse

import rohan_model.users

def test(request):
	print "in test"
	return render(request, 'rest_api/postJson.html')

def register(request):
	id_ = request.GET['id']
	firstName = request.GET['firstName']
	lastName = request.GET['lastName']
	email = request.GET['email']
	pushToken = request.GET['pushToken']
	
	return HttpResponse(json.dumps(rohan_model.users.register(id_, firstName, lastName, email, pushToken)))

def login1(request):
	print "in loging"
	email = request.GET['email']
	pdb.set_trace()
	ans = rohan_model.users.login(email)

	# print ans
	# pdb.set_trace()
	# ans   = login("diamant.alon@gmail.com")

	# pdb.set_trace()
	return HttpResponse(json.dumps(ans))

def login_s(request):

	return  HttpResponse("ok")

def task_list_S(request):
	print "in tasklists"
	if request.is_ajax():
		print "is ajax"
		# if request.method == 'POST':
		# 	print 'Raw Data: "%s"' % request.body
	# email = request.POST['email']
	# [,]
	 
	#retList = ['FE:AA:C5:AC:15:AA','DB:AC:08:7C:0B:62','FE:E2:C5:AC:15:69','FE:E2:C5:FF:FF:FF']
	t1 = [["uuid",'FE:AA:C5:AC:15:AA'], ["state",0]]
	t2 = [["uuid",'FE:AA:C5:AC:15:AA'], ["state",0]]
	t3 = [["uuid",'DB:AC:08:7C:0B:62'],["state",1], ["task_list_name",'Hezi List']]
	# t4 = [[uuid,'FE:E2:C5:AC:15:69'],[state=2], ["task_list_name",'Open_Admind_List'], ["is_admin",1],["task_list",[[["task_id",23232], ["task_price",500], ["task_description",'Taking a big coffee'] , ["task_state",2] ] ] ] ] 
	# t5 = [uuid='FE:E2:C5:FF:FF:FF',state=2,task_list_name='OpenList_Normal', is_admin=0,task_list=[[task_id=23232, task_price=500, task_description='Taking a big coffee' , task_state=0 ]]
	# t6 = [task_id=23232, task_price=1000, task_description='NOT YOUR TASK' , task_state=1 }
	retList = [t1 ,t2 ,t3 ]

	return HttpResponse(json.dumps(retList))


def task_accept_s(request):
	# task_id, token
	a=1
	# pdb.set_trace()
	a += 1
	if (a %2) == 0:
		retList = ["ok",""]
		return HttpResponse(json.dumps(retList))
	else: 
		retList = ["error","taken"]
		return HttpResponse(json.dumps(retList))

def task_rejet_S(request):
	# task_id, token
	return HttpResponse("ok")

def task_finish_s(request):
	# task_id, token
	return HttpResponse("ok")

def task_validate_S(request):
	# task_id, approved,
	return HttpResponse("ok")

def task_new_S(request):

	return HttpResponse("ok")


def task_accept(request):
	task_id = request.POST['task']


