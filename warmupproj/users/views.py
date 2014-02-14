from django.shortcuts import render
from warmupproj.users.models import User
from django.http import HttpResponse
import json


def handleLogin(request, *args, **kwargs):
    response = {}
    
    if request.method == 'POST':
        req = json.loads(request.body)
        username = req['user']
        password = req['password']
        path = request.path 

        if path == "/users/login" :
            if User.objects.filter(user__exact=username):
                print "helloworld"
                # u = User.objects.filter(user=username, password=password)[0]
                # if u.password == password:
                #     u.count += 1
                #     u.save()
                #     response['count'] = u.count
                # else:
                #     err_code = User.ERR_BAD_CREDENTIALS
            else:
                return User.ERR_BAD_CREDENTIALS
            
            response['err_code'] = err_code

            # return HttpResponse(json.dumps(response), content_type='application/json')

        if path == "users/add":

            if len(username) > User.MAX_USERNAME_LENGTH:
                err_code = User.ERR_BAD_USERNAME
            if len(password) > User.MAX_PASSWORD_LENGTH:
                err_code = User.ERR_BAD_PASSWORD

            u = User.object.create(user=username, password=password)
            u.save()
            response['err_code'] = err_code
            response['count'] = u.count
            
    return HttpResponse(json.dumps(response), content_type='application/json')


