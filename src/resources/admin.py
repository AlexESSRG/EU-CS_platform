from django.contrib import admin
from .models import Resource, ResourceGroup, ResourcesGrouped, Category, FeaturedResources, SavedResources
# Register your models here.

class ResourcesGroupedAdmin(admin.ModelAdmin):
    list_filter = ('group','resource',)
    ordering = ('-group',)


class CategoryGroupedAdmin(admin.ModelAdmin):
    list_filter = ('text','parent',)
    ordering = ('-parent',)
    
admin.site.register(Resource)
admin.site.register(Category, CategoryGroupedAdmin)
admin.site.register(ResourceGroup)
admin.site.register(ResourcesGrouped, ResourcesGroupedAdmin)
admin.site.register(FeaturedResources)
admin.site.register(SavedResources)
