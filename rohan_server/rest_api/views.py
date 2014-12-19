from django.shortcuts import render
from django.views import generic
import pdb
import json

from django.http import HttpResponse

import rohan_model.users

from rohan_model import images
from rohan_model import users
from rohan_model import lists
from rohan_model import tasks

from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def test(request):
    print "in test"
    # print request.body
    
    jObj = json.loads(request.body)
    print b
    print b["b"]
    # if request.is_ajax():
    #   print "is ajax"
    #   if request.method == 'POST':
    #       print 'Raw Data: "%s"' % request.body
    return HttpResponse(json.dumps(request.body))
@csrf_exempt
def register(request):

    jObj = json.loads(request.body)
    id_ = jObj['id']
    firstName = jObj['firstName']
    lastName = jObj['lastName']
    email = jObj['email']
    pushToken = jObj['pushToken']

    # Return true/false
    return HttpResponse(json.dumps(rohan_model.users.register(id_, firstName, lastName, email, pushToken)))

@csrf_exempt
def login1(request):
    print "in loging"
    # email = request.GET['email']
    jObj = json.loads(request.body)

    
    token = rohan_model.users.login(jObj['email'])

    # print ans
    # pdb.set_trace()
    # ans   = login("diamant.alon@gmail.com")

    # pdb.set_trace()

    # Return the token
    return HttpResponse(json.dumps(token))


@csrf_exempt
def set_image(request):
    print "set_image"

    jObj = json.loads(request.body)

    id = jObj['id']
    image = jObj['image']

    ret = images.set(id, image)

    return HttpResponse(json.dumps(ret))

@csrf_exempt
def get_image(request):
    print "set_image"

    jObj = json.loads(request.body)

    id = jObj['id']


    image = images.set(id)

    ret = {
        "id": id,
        "image": image
    }

    return HttpResponse(json.dumps(ret))



@csrf_exempt
def login_s(request):

    return  HttpResponse("ok")

@csrf_exempt
def task_list_S(request):

    '''

    if request.is_ajax():
        if request.method == 'POST':
            print 'Raw Data: "%s"' % request.body

    # email = request.POST['email']
    # [,]
     ["FE:AA:C5:AC:15:AA","DB:AC:08:7C:0B:62","FE:E2:C5:AC:15:69','FE:E2:C5:FF:FF:FF']
    #retList = ['FE:AA:C5:AC:15:AA','DB:AC:08:7C:0B:62','FE:E2:C5:AC:15:69','FE:E2:C5:FF:FF:FF']
    t1 = [["uuid",'FE:AA:C5:AC:15:AA'], ["state",0]]
    t2 = [["uuid",'FE:AA:C5:AC:15:AA'], ["state",0]]
    t3 = [["uuid",'DB:AC:08:7C:0B:62'],["state",1], ["task_list_name",'Hezi List']]
    # t4 = [[uuid,'FE:E2:C5:AC:15:69'],[state=2], ["task_list_name",'Open_Admind_List'], ["is_admin",1],["task_list",[[["task_id",23232], ["task_price",500], ["task_description",'Taking a big coffee'] , ["task_state",2] ] ] ] ] 
    # t5 = [uuid='FE:E2:C5:FF:FF:FF',state=2,task_list_name='OpenList_Normal', is_admin=0,task_list=[[task_id=23232, task_price=500, task_description='Taking a big coffee' , task_state=0 ]]
    # t6 = [task_id=23232, task_price=1000, task_description='NOT YOUR TASK' , task_state=1 }
    retList = [t1 ,t2 ,t3 ]
    '''
    jObj = json.loads(request.body)
    print jObj
    # pdb.set_trace()
    beacons=[]
    for jo in jObj:
        beacons.append(jo)


    beacons = [beaconId.replace(":","") for beaconId in beacons]
    token = "alon"
    
    # beacons = [ "123", "4567", "8123" ]

    myLists = []
    for beaconId in beacons:
        print "Handling beacon %s" % beaconId
        if lists.exists(beaconId, accessToken=token):
            print "Appending beaocn list to results"
            myLists.append(lists.get(beaconId, accessToken=token))
    # pdb.set_trace()

    print "Beacons list: %s" % str(myLists)
    # Replace the task IDs array with a tasks array
    for currentList in myLists:
        realTasks = []
        if 'tasks' in currentList:
            for currentTask in currentList['tasks']:
                atask = tasks.get(currentTask, accessToken=token)
                if 'creationTime' in atask:
                    del atask['creationTime']
                if 'acceptedTime' in atask:
                    del atask['acceptedTime']
                if 'finishedTime' in atask:
                    del atask['finishedTime']
                realTasks.append(atask)
        currentList['tasks'] = realTasks

    return HttpResponse(json.dumps(myLists))

@csrf_exempt
def task_accept_s(request):

    # task_id, token
    '''
    a=1
    # pdb.set_trace()
    a += 1
    if (a %2) == 0:
    retList = ["ok",""]
    return HttpResponse(json.dumps(retList))
    else:
    retList = ["error","taken"]
    return HttpResponse(json.dumps(retList))
    '''
    jObj = json.loads(request.body)
    print jObj

    task_id = jObj["task_id"]
    token = jObj["in_token"]
    # token = "alon"

    result = tasks.accept(task_id, token, accessToken=token)

    return HttpResponse(json.dumps(result))
@csrf_exempt
def task_rejet_S(request):

    jObj = json.loads(request.body)
    print jObj

    task_id = jObj["task_id"]
    token = jObj["in_token"]
    # token = "alon"
    # task_id = None
    # token = ""

    result = tasks.cancel(task_id, token, accessToken=token)


    # task_id, token
    return HttpResponse(json.dumps(result))
@csrf_exempt
def task_finish_s(request):
    # task_id, token

    jObj = json.loads(request.body)
    print jObj

    task_id = jObj["task_id"]
    token = jObj["in_token"]
    # token = "alon"
    imageUrl = jObj["image_url"]


    # task_id = None
    # token = ""
    # imageUrl = ""

    result = tasks.finish(task_id, token, imageUrl, accessToken=token)
    return HttpResponse(json.dumps(result))


@csrf_exempt
def task_validate_S(request):
    # task_id, approved,

    jObj = json.loads(request.body)
    print jObj

    task_id = jObj["task_id"]
    token = jObj["in_token"]
    # token = "alon"
    # task_id = None
    # token = ""
    print "task_id=%s token=%s " % (task_id,token)
    result = tasks.verify(task_id, accessToken=token)

    return HttpResponse(json.dumps(result))
@csrf_exempt
def task_new_S(request):

    jObj = json.loads(request.body)
    print jObj

    task_id = jObj["task_id"]
    token = jObj["in_token"]
    task_name = jObj["task_name"]
    task_description = jObj["task_name"]
    task_points =  jObj["task_points"]
    listId =  jObj["list_id"]
    # token = ""
    # task_id = ""
    # task_name = ""
    # task_description = ""
    # task_points = 500
    # listId = ""

    result = tasks.new(task_id, task_name, task_description, task_points, listId, accessToken=token)

    return HttpResponse(json.dumps(result))

@csrf_exempt
def task_accept(request):
    # What is the difference between task_accept and task_accept_s?
    task_id = request.POST['task']


