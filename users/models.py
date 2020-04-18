from django.db.models import Model
from django.db.models import IntegerField, CharField, BooleanField
from django.db.models import DateField, TimeField, DateTimeField
from django.db.models import ForeignKey, OneToOneField
from django.contrib.postgres.fields import ArrayField
from django.db.models import CASCADE
from django.contrib.auth.models import User
import datetime
from django.utils.translation import gettext as _


# patient class
class customer(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    name = CharField(max_length=50, blank=True)


class store(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    name = CharField(max_length=50, blank=True)
    category = CharField(max_length=50, blank=True)



class store_info(Model):
    store_id = ForeignKey(store, on_delete=CASCADE)
    location = CharField(max_length=50, blank=True)
    count = CharField(max_length=50, blank=True)

class store_news(Model):
    store_id = ForeignKey(store, on_delete=CASCADE)
    news =  CharField(max_length=100, blank=True)
    time_of_post = DateTimeField(auto_now=True)

# Create your models here.
