from django.shortcuts import render
from warmupproj.users.models import User
import json


def handleLogin(request, *args, **kwargs):
    if request.method == 'POST':


        req = json.loads(request.body)
        username = req['username']
        password = req['password']
        path = request.path 


        if path == "/users/login" :
            try:
                u = User.objects.get(username = user)
            except User.DoesNotExist:
                u = None
        
            if u == None: 
                return User.ERR_BAD_CREDENTIALS

            if u.password != password:
                return User.ERR_BAD_CREDENTIALS

            u.count += 1
            return u.count
        if path == "users/add" :
            try:
                u = User.objects.get(username = user)
            except User.DoesNotExist:
                u = None
           
            if u != None:
                return Users.ERR_USER_EXISTS

            def valid_username(username):
                return username != "" and len(username) <= Users.MAX_USERNAME_LENGTH

            def valid_password(password):
                return len(password) <= Users.MAX_PASSWORD_LENGTH
            
            if not valid_username(username):
                return Users.ERR_BAD_USERNAME
            if not valid_password(password):
                return Users.ERR_BAD_PASSWORD
            
            u = User.object.create(username=username, password=password)
            u.save()
            assert u.count == 1
            return u.count


