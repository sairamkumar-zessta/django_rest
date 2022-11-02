from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User 
from django.dispatch import receiver 
from django.db.models.signals import pre_init, post_init, pre_save, post_save, pre_delete, post_delete
from django.core.signals import request_started, request_fineshed, got_request_exception
#authentication signals

#user_logged_in receiver_function
@receiver(user_logged_in, sender=User)
def login_success (sender, request, user, **kwargs):
    print("-------------------------")
    print("....Logged-in Signal....") 
    print("Sender:", sender)
    print("Request:", request)
    print("User:",user) 
    print("Password:",user.password) 
    print(f'kwargs: {kwargs}')
# user_logged_in.connect(login_success, sender=User) #manual connect Route 

#user_logged_out receiver_function
@receiver(user_logged_out, sender=User)
def log_out (sender, request, user, **kwargs):
    print("-------------------------")
    print("....Logged-out Signal....") 
    print("Sender:", sender)
    print("Request:", request)
    print("User:",user) 
    print("Password:",user.password) 
    print(f'kwargs: {kwargs}')
# user_logged_out.connect(log_out, sender=User) #manual connect Route

#user_login_failed receiver_function
@receiver(user_login_failed)
def login_failed (sender, request, credentials, **kwargs):
    print("-------------------------")
    print("....Login-Failed Signal....") 
    print("Sender:", sender)
    print("Request:", request)
    print("Credentials:",credentials) 
    print(f'kwargs: {kwargs}')
# user_login_failed.connect(login_failed) #manual connect Route 

#model signals

#pre_save receiver_function
@receiver(pre_save, sender=User)
def at_begining_save(sender, instance, **kwargs):
    print("-------------------------")
    print("....Pre-save Signal....") 
    print("Sender:", sender)
    print("Instance:", instance) 
    print(f'kwargs: {kwargs}') 

#post_save receiver_function
@receiver(post_save, sender=User)
def at_endining_save(sender, instance, created, **kwargs):
    if created:
        print("-------------------------")
        print("....Post-save Signal....") 
        print("New Record")
        print("Sender:", sender)
        print("Instance:", instance) 
        print("Created:", created)
        print(f'kwargs: {kwargs}') 
    else:
        print("-------------------------")
        print("....Post-save Signal....") 
        print("Update")
        print("Sender:", sender)
        print("Created:", created)
        print("Instance:", instance) 
        print(f'kwargs: {kwargs}')

#pre_delete receiver_function
@receiver(pre_delete, sender=User)
def at_begining_delete(sender, instance, **kwargs):
    print("-------------------------")
    print("....Pre-delete Signal....") 
    print("Sender:", sender)
    print("Instance:", instance) 
    print(f'kwargs: {kwargs}') 

#post_delete receiver_function
@receiver(post_delete, sender=User)
def at_endining_save(sender, instance, **kwargs):
    print("-------------------------")
    print("....Post-delete Signal....") 
    print("Sender:", sender)
    print("Instance:", instance) 
    print(f'kwargs: {kwargs}') 


#pre_init receiver_function
@receiver(pre_init, sender=User)
def at_begining_init(sender, *args, **kwargs):
    print("-------------------------")
    print("....Pre-init Signal....") 
    print("Sender:", sender)
    print(f'Args: {args}') 
    print(f'kwargs: {kwargs}') 

#post_init receiver_function
@receiver(post_init, sender=User)
def at_endining_init(sender, *args, **kwargs):
    print("-------------------------")
    print("....Post-init Signal....") 
    print("Sender:", sender)
    print(f'Args: {args}') 
    print(f'kwargs: {kwargs}')  


