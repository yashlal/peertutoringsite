from django import template

register = template.Library()

@register.filter
def get_index(list, item):
    i = list.index(item)
    return i

@register.filter
def get_val(list, index):
    index = int(index)
    return list[index]
