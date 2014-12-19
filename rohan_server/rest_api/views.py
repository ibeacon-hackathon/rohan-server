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

    ret = { "result": "error"}
    try:
        ret = json.loads(request.body)
        ret = json.dumps({"result": ret})
    except:
        pass

    return HttpResponse(ret, content_type="application/json")

@csrf_exempt
def register(request):

    ret = { "result": "error"}
    try:
        jObj = json.loads(request.body)
        id_ = jObj['id']
        firstName = jObj['firstName']
        lastName = jObj['lastName']
        email = jObj['email']
        pushToken = jObj['pushToken']
        ret = rohan_model.users.register(id_, firstName, lastName, email, pushToken)
        ret = json.dumps({"result": ret})
    except:
        pass

    # Return true/false
    return HttpResponse(ret, content_type="application/json")

@csrf_exempt
def login1(request):

    ret = { "result": "error"}
    try:
        jObj = json.loads(request.body)

        token = rohan_model.users.login(jObj['email'])

        ret = json.dumps({"authToken": token})
    except:
        pass

    # Return the token
    return HttpResponse(ret, content_type="application/json")


@csrf_exempt
def set_image(request):

    ret = { "result": "error"}
    try:
        jObj = json.loads(request.body)

        id = jObj['id']
        image = jObj['image']

        ret = images.set(id, image)
        ret = json.dumps({"result": ret})
    except:
        pass

    return HttpResponse(ret, content_type="application/json")

@csrf_exempt
def get_image(request):

    ret = { "result": "error"}
    try:
        jObj = json.loads(request.body)

        id = jObj['id']


        image = images.get(id)

        ret = {
            "id": id,
            "image": image
        }

        ret = json.dumps(ret)
    except:
        pass

    return HttpResponse(ret, content_type="application/json")



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

    ret = { "result": "error"}
    try:
        jObj = json.loads(request.body)

        token = 'alon' # default, remove this
        if 'authToken' in jObj:
            token = jObj['authToken']
        beacons = []
        for jo in jObj['beacons']:
            beacons.append(jo)

        beacons = [beaconId.replace(":","") for beaconId in beacons]

        # beacons = [ "123", "4567", "8123" ]

        myLists = []
        for beaconId in beacons:
            if lists.exists(beaconId, accessToken=token):
                myLists.append(lists.get(beaconId, accessToken=token))

        # Replace the task IDs array with a tasks array
        for currentList in myLists:
            realTasks = []

            id = currentList['id']
            currentList['id'] = "%s:%s:%s:%s:%s:%s" % (id[0:2], id[2:4], id[4:6], id[6:8], id[8:10], id[10:12])

            if 'tasks' in currentList:
                for currentTask in currentList['tasks']:
                    atask = tasks.get(currentTask, accessToken=token)

                    # Get rid of datetimes
                    if 'creationTime' in atask and atask['creationTime']:
                        atask['creationTime'] = atask['creationTime'].isoformat(' ')
                    if 'acceptedTime' in atask and atask['acceptedTime']:
                        atask['acceptedTime'] = atask['acceptedTime'].isoformat(' ')
                    if 'finishedTime' in atask and atask['finishedTime']:
                        atask['finishedTime'] = atask['finishedTime'].isoformat(' ')

                    atask["list"] = "%s:%s:%s:%s:%s:%s" % (id[0:2], id[2:4], id[4:6], id[6:8], id[8:10], id[10:12])
                    realTasks.append(atask)
            currentList['tasks'] = realTasks

        ret = myLists

        ret = {"result": ret}

        ret = json.dumps(ret)
    except:
        pass

    return HttpResponse(ret, content_type="application/json")

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
    ret = { "result": "error"}
    try:
        print "Got body: %s" % request.body

        jObj = json.loads(request.body)
        print jObj

        task_id = jObj["taskId"]
        token = jObj["authToken"]
        # token = "alon"

        result = tasks.accept(task_id, token, accessToken=token)

        ret = result
        ret = json.dumps({"result": ret})
    except:
        pass

    return HttpResponse(ret, content_type="application/json")

@csrf_exempt
def task_rejet_S(request):

    ret = { "result": "error"}
    try:
        jObj = json.loads(request.body)
        print jObj

        task_id = jObj["taskId"]
        token = jObj["authToken"]
        # token = "alon"
        # task_id = None
        # token = ""

        result = tasks.cancel(task_id, token, accessToken=token)

        ret = result

        ret = json.dumps({"result": ret})
    except:
        pass

    return HttpResponse(ret, content_type="application/json")

@csrf_exempt
def task_finish_s(request):
    # task_id, token

    ret = { "result": "error"}
    try:
        jObj = json.loads(request.body)
        print jObj

        task_id = jObj["taskId"]
        token = jObj["authToken"]
        # token = "alon"
        imageUrl = jObj["imageUrl"]


        # task_id = None
        # token = ""
        # imageUrl = ""

        result = tasks.finish(task_id, token, imageUrl, accessToken=token)

        ret = result
        ret = json.dumps({"result": ret})
    except:
        pass

    return HttpResponse(ret, content_type="application/json")

@csrf_exempt
def task_validate_S(request):
    # task_id, approved,

    ret = { "result": "error"}
    try:
        jObj = json.loads(request.body)
        print jObj

        task_id = jObj["taskId"]
        token = jObj["authToken"]
        # token = "alon"
        # task_id = None
        # token = ""
        print "task_id=%s token=%s " % (task_id,token)
        result = tasks.verify(task_id, accessToken=token)
        ret = result

        ret = json.dumps({"result": ret})
    except:
        pass

    return HttpResponse(ret, content_type="application/json")

@csrf_exempt
def task_new_S(request):

    ret = { "result": "error"}
    try:
        jObj = json.loads(request.body)
        print jObj

        task_id = jObj["taskId"]
        token = jObj["authToken"]
        task_name = jObj["taskName"]
        task_description = jObj["taskDescription"]
        task_points =  int(jObj["taskPoints"])
        listId =  jObj["listId"].replace(":","")
        # token = ""
        # task_id = ""
        # task_name = ""
        # task_description = ""
        # task_points = 500
        # listId = ""

        result = tasks.new(task_id, task_name, task_description, task_points, listId, accessToken=token)

        ret = result
        ret = json.dumps({"result": ret})
    except:
        pass

    return HttpResponse(ret, content_type="application/json")


