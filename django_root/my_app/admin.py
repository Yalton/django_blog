from django.contrib import admin
from . import models
from my_app.models import *
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin


admin.site.register(Category, DraggableMPTTAdmin)
admin.site.register(Blogpost)
admin.site.register(Comment)
admin.site.register(Message)
# admin.site.register(Rabbithole)
# admin.site.register(Like)
# admin.site.register(Dislike)
# admin.site.register(SavetoProfile)
# admin.site.register(UserInfo)


