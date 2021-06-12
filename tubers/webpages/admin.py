from django.contrib import admin
from .models import Slider , Team
from django.utils.html import format_html
# Register your models here.


class TeamAdmin(admin.ModelAdmin):


    def my_photo(self , objects):
        return format_html('<img src={} width=40>'.format(objects.photo.url))


    list_display = ('id' , 'my_photo' , 'first_name' , 'role' , 'create_data') # how you want to list on the admin panel
    list_display_links = ('first_name' , )  # make column a clickable
    search_fields = ('first_name', )  # activate the search key
    list_filter = ('role',) # add filter option

admin.site.register(Slider)
admin.site.register(Team , TeamAdmin)

