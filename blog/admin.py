from django.contrib import admin

# Register your models here.
from .models import IndexCounts,IndexHero,IndexSection,IndexWhysection,Courses,Trainers,Testimonials

class BlogAdmin(admin.ModelAdmin):
    list_display=("title","is_home",)
    list_editable=("is_home",)
    search_fields=("title","description","name",)

class BlogAdminTrainer(admin.ModelAdmin):
    list_display=("name","is_home",)
    list_editable=("is_home",)
    search_fields=("name","description",)





admin.site.register(Courses,BlogAdmin)
admin.site.register(Trainers,BlogAdminTrainer)
admin.site.register(IndexCounts)
admin.site.register(IndexHero)
admin.site.register(IndexSection)
admin.site.register(IndexWhysection)
admin.site.register(Testimonials)
