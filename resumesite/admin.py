from django.contrib import admin
from . models import Name, About, Resume, Summary, Education, Skills, Experience

# Register your models here.

admin.site.register(Name)
admin.site.register(About)
admin.site.register(Resume)

admin.site.register(Summary)
admin.site.register(Education)
admin.site.register(Experience)

class ResumeAdmin(admin.ModelAdmin):
	list_display = ['id','description']

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
	list_display = ['about_skil', 'title', 'percentage']
	list_filter = ('about_skil', 'title', 'percentage')
