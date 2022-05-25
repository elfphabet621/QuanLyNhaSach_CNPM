from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Person

def customer_profile(sender, instance, created, **kwargs):
    if created:
        newid = len(Person.objects.filter(chuc_vu='khách hàng'))+1
        if int(newid) <= 9:
            newid = '0'+ str(newid)

        Person.objects.create(
            id='kh_0' + newid,
            ho_ten= instance.username,
            email= instance.email,
            chuc_vu='khách hàng',
            user=instance
        )

        print('Customer created')

post_save.connect(customer_profile, sender=User)