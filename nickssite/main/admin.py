from django.contrib import admin
from .models import Review, Categorie, Team
from tinymce.widgets import TinyMCE
from django.db import models


class ReviewAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["review_title", "review_date"]}),
        ("Content", {"fields": ["review_content"]}),
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


class CategorieAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["category_title", "category_date"]}),
        ("Content", {"fields": ["category_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }


class TeamAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/date", {'fields': ["team_title", "team_date"]}),
        ("Content", {"fields": ["team_content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

# Register your models here.
admin.site.register(Review, ReviewAdmin)
admin.site.register(Categorie, CategorieAdmin)
admin.site.register(Team, TeamAdmin)