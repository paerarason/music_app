from django.contrib import admin
from .models import Email,Email_Folder_conn,Music,Music_Lover,Folder_repo
# Register your models here.
admin.site.register(Email)
admin.site.register(Email_Folder_conn)
admin.site.register(Music)
admin.site.register(Music_Lover)
admin.site.register(Folder_repo)
