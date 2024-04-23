from .models import Drinks
from .models import User

from django.contrib import admin

#admin.site.register(Drinks)
admin.site.site_header="Customer Record Management"

admin.site.register(User)
