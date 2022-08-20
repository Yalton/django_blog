from django.contrib import admin
from . import models
from my_app.models import *
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin
from  embed_video.admin  import  AdminVideoMixin



class  tutorialAdmin(AdminVideoMixin, admin.ModelAdmin):
	pass




admin.site.register(Category, DraggableMPTTAdmin)
# admin.site.register(Item)
# admin.site.register(Post)
admin.site.register(Article)
admin.site.register(Service)
admin.site.register(Tutorial, tutorialAdmin)
admin.site.register(TutorialField)
admin.site.register(TutorialFieldContent)
admin.site.register(TutorialFieldContentMedia)
# admin.site.register(Rabbithole)
# admin.site.register(Like)
# admin.site.register(Dislike)
# admin.site.register(SavetoProfile)
# admin.site.register(UserInfo)


