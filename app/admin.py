from django.contrib import admin

# Register your models here.
from app.models import Author, JobApp, Location, Skills

class JobAdmin(admin.ModelAdmin):
    list_display = ('__str__','title','date', 'salary',)
    list_filter = ('date', 'salary')
    search_fields = ('title','description', )
    search_help_text = 'Enter your search above'
    # fields = ('title', 'description', 'salary', )
    # exclude = ('title')
    fieldsets = (('Basic Information', {
        'fields': ('title', 'description',)
    }),
    ('More Information', {
        # 'classes': ('collapse',),
        'fields': ('salary', 'expiry', 'slug',)
    }))

admin.site.register(JobApp)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)
