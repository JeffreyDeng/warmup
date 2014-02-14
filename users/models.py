from django.db import models

class User(models.Model):


    ## The success return code
    SUCCESS               =   1

    ## Cannot find the user/password pair in the database (for login only)
    ERR_BAD_CREDENTIALS   =  -1

    ## trying to add a user that already exists (for add only)
    ERR_USER_EXISTS       =  -2

    ## invalid user name (empty or longer than MAX_USERNAME_LENGTH) (for add, or login)
    ERR_BAD_USERNAME      =  -3

    ## invalid password name (longer than MAX_PASSWORD_LENGTH) (for add)
    ERR_BAD_PASSWORD      =  -4


    ## The maximum length of user name
    MAX_USERNAME_LENGTH = 128

    ## The maximum length of the passwords
    MAX_PASSWORD_LENGTH = 128
    
	username = models.CharField(max_length = MAX_USERNAME_LENGTH, primary_key = True)
	password = models.CharField(max_length = MAX_PASSWORD_LENGTH)
	count = models.IntegerField(default = 1)

    