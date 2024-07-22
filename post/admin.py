from django.contrib import admin
from .models import Post



class Postadmin(admin.ModelAdmin):
    list_display = ('title','discription','created_at')
    search_fields = ('title',)
    list_filter = ('active',)


admin.site.register(Post,Postadmin)
