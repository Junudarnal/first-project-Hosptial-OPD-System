from django.contrib import admin

# Register your models here.
from user.models import User,Profile
admin.site.register([User,Profile])

