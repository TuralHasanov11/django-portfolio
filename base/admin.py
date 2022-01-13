from django.contrib import admin
from .models import *

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'created_at', 'updated_at')
    search_fields = ('name','url')
    ordering = ('name','url')
    filter_horizontal = ()


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'created_at', 'updated_at')
    search_fields = ('name','icon')
    ordering = ('name','icon')
    filter_horizontal = ()


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('company', 'position', 'date_from', 'date_to', 'created_at', 'updated_at')
    search_fields = ('company', 'position', 'date_from', 'date_to')
    ordering = ('company', 'position', 'date_from', 'date_to')
    filter_horizontal = ()


class ProjectTechnologyAdmin(admin.ModelAdmin):
    list_display = ('project', 'skill')
    search_fields = ('project', 'skill')
    ordering = ('project', 'skill')
    filter_horizontal = ()

admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(ProjectTechnology, ProjectTechnologyAdmin)
