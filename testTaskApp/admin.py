from django.contrib import admin
from .models import *

admin.site.register(Employee)
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Comments)
admin.site.register(PrComments)