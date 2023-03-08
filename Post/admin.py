from django.contrib import admin
from .models import About,Post,Postcads,Category,Subscribe,Contact

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_date']
    list_filter = ['created_date']
    search_fields = ['title']

class PotcastAdmin(admin.ModelAdmin):
    list_display = ['title','created_date']
    list_filter = ['created_date']
    search_fields = ['title']

class AboutAdmin(admin.ModelAdmin):
    list_display = ['title']

class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['email']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['created_date','name','subject']
    list_filter = ['created_date']
    search_fields = ['name','subject']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Postcads,PotcastAdmin)
admin.site.register(About,AboutAdmin)
admin.site.register(Subscribe,SubscribeAdmin)
admin.site.register(Contact,ContactAdmin)
