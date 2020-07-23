from django.contrib import admin
from .models import Request, User, Category, Tutor, Student, Subject

# Register your models here.
class RequestAdmin(admin.ModelAdmin):
    #fields = ['subject', 'grade_level', 'dt', 'content']
    fieldsets = [
    ("Heading", {'fields': ['subject', 'category', 'author', 'grade_level', 'dt']}),
    ('Body', {'fields': ['content']}),
    ]

admin.site.register(Request, RequestAdmin)

admin.site.register(Category)

admin.site.register(Subject)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_student', 'is_tutor')
    list_filter = ('is_staff', 'is_superuser', 'is_student', 'is_tutor')

class TutorAdmin(admin.ModelAdmin):
    fields = ['user', 'subjects']
    list_display = ['get_username']

class StudentAdmin(admin.ModelAdmin):
    fields = ['user']
    list_display = ['get_username']

admin.site.register(User, UserAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Student, StudentAdmin)
