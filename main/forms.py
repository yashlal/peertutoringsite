from django import forms
from .models import IntegerRangeField, Request, Category, Tutor, Student, Subject
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.db import transaction, models
from .widgets import DropDownWidget, DropDownWidgetSingle


class SubjectSelectField(forms.ModelMultipleChoiceField):
    widget = DropDownWidget

    def __init__(self, queryset, groupby_list, object_list, *args, **kwargs):

        super().__init__(queryset=queryset, *args, **kwargs)

        self.groupby_list = groupby_list
        self.object_list = object_list
        self.widget.choices = list(self.choices)
        self.widget.groupby_list = self.groupby_list
        self.widget.object_list = self.object_list


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
    subjects = SubjectSelectField(queryset=Subject.objects.all(), groupby_list=Category.objects.all(), object_list=Subject.objects.all())

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2", "subjects")

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_tutor = True
        user.save()
        tutor = Tutor.objects.create(user=user)

        if self.cleaned_data.get('subjects'):
            for el in self.cleaned_data.get('subjects'):
                tutor.subjects.add(el)
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
        student = Student.objects.create(user=user)
        return user

class TestForm(forms.Form):
    subject = SubjectSelectField(queryset=Subject.objects.all(), groupby_list=Category.objects.all(), object_list=Subject.objects.all(), widget=DropDownWidgetSingle)
