from django.contrib import admin
from . import models
from my_app.models import *
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin


admin.site.register(Category, DraggableMPTTAdmin)
# admin.site.register(Item)
# admin.site.register(Post)
admin.site.register(Tutorial)
admin.site.register(Article)
admin.site.register(Service)
# admin.site.register(Rabbithole)
# admin.site.register(Like)
# admin.site.register(Dislike)
# admin.site.register(SavetoProfile)
# admin.site.register(UserInfo)


