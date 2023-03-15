from django.contrib import admin
from .models import register_new, login_new, contacting_new, predict,collect_new
# Register your models here.

admin.site.register(register_new)
admin.site.register(login_new)
admin.site.register(contacting_new)
admin.site.register(predict)
admin.site.register(collect_new)