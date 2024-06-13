from django.contrib import admin
from.models import Profiles,Result
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin # type: ignore
# Register your models here.
class UserAdmin(UserAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ['password','date_joined','last_login']
        else:
            return []
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('slug',)
    list_display= ['user','phone','role','join_date']
    list_filter=['role','join_date',]
    search_fields=['user__username',]
class ResultAdmin(admin.ModelAdmin):
    list_display= ['user','quiqexamreqsult','fullexamreqsult','Resultss']
    list_filter=['user','quiqexamreqsult','fullexamreqsult',]
    search_fields=['user__username','quiqexamreqsult','fullexamreqsult',]
admin.site.unregister(User)
admin.site.register(User,UserAdmin)
admin.site.register(Profiles,ProfileAdmin)
admin.site.register(Result,ResultAdmin)