from django.contrib import admin
from .models import Learner, User,Teacher, Learner, AdminUser,Class, Subject


admin.site.register(Subject)
admin.site.register(Class)
admin.site.register(AdminUser)
admin.site.register(Learner)
admin.site.register(User)
admin.site.register(Teacher)