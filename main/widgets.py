from django import forms
from django.utils.safestring import mark_safe


class DropDownWidget(forms.widgets.CheckboxSelectMultiple):

    template_name = "main/dropdown_template.html"

    def __init__(self, object_list=[], attrs=None, groupby_list=[]):

        self.groupby_list = groupby_list
        self.object_list = object_list

        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['groupby_list'] = self.groupby_list
        context['widget']['choices']  = list(self.choices)
        context['widget']['list_of_choices'] = [el for el in self.choices]
        context['widget']['object_list'] = self.object_list
        return context

    def render(self, name, value, attrs=None, renderer=None):
        """Render the widget as an HTML string."""
        context = self.get_context(name, value, attrs)
        return self._render(self.template_name, context, renderer)

    def _render(self, template_name, context, renderer=None):
        if renderer is None:
            renderer = get_default_renderer()
        return mark_safe(renderer.render(template_name, context))


class DropDownWidgetSingle(forms.widgets.Select):
    template_name = "main/dropdown_single_template.html"

    def __init__(self, object_list=[], attrs=None, groupby_list=[]):

        self.groupby_list = groupby_list
        self.object_list = object_list

        super().__init__(attrs)

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget']['groupby_list'] = self.groupby_list
        context['widget']['choices']  = self.choices
        context['widget']['list_of_choices'] = [el for el in self.choices]
        context['widget']['object_list'] = self.object_list
        return context

    def render(self, name, value, attrs=None, renderer=None):
        """Render the widget as an HTML string."""
        context = self.get_context(name, value, attrs)
        return self._render(self.template_name, context, renderer)

    def _render(self, template_name, context, renderer=None):
        if renderer is None:
            renderer = get_default_renderer()
        return mark_safe(renderer.render(template_name, context))
