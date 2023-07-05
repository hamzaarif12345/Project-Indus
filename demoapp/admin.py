from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Todo1)


admin.site.register(Message)
#admin.site.register(message_create)


admin.site.register(MyModel2)
admin.site.register(MyModel3)
