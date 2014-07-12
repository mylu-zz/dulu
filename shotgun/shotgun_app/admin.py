from django.contrib import admin

# Register your models here.
from shotgun_app.models import Users
from shotgun_app.models import Events
from shotgun_app.models import Attending
from shotgun_app.models import Friends

admin.site.register(Users)
admin.site.register(Events)
admin.site.register(Attending)
admin.site.register(Friends)
