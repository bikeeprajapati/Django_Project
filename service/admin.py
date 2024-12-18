from django.contrib import admin
from service.models import Features

class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('Features_Icon','Features_Title','Features_Description')
    
admin.site.register(Features,FeaturesAdmin)

# Register your models here.
