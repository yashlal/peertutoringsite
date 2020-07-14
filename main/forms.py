from django import forms
from .models import IntegerRangeField, Request, Category, Tutor, Student
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction


class HelpForm(forms.ModelForm):
    class Meta:
        model = Request
        fields = ('subject', 'category', 'grade_level', 'content')
        widgets = {'content': forms.Textarea(), 'category': forms.RadioSelect(choices=Category.objects.all())}
        help_texts = {
        'subject': "Class for the help required",
        'grade_level': 'Grade level between 1 and 12',
        'content': 'Describe the content with which you need help',
        'category': 'Pick a category for the subject'
        }
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.label_suffix = ""

class TutorCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    subjects = forms.ModelMultipleChoiceField(queryset=Category.objects.all(), widget=forms.CheckboxSelectMultiple, required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", 'subjects')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_tutor = True
        user.save()
        tutor = Tutor.objects.create(user=user)
        tutor.subjects.add(*self.cleaned_data.get('subjects'))
        return user


class StudentCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_student = True
        user.save()
        tutor = Student.objects.create(user=user)
        return user
