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

@register.filter
def modified_range(list):
    true_range = range(1, len(list)-1)
    return true_range


@register.filter
def minus(integer):
    integer = int(integer)
    integer = integer - 1
    return integer

@register.filter
def fixed_choices(list_input):
    try:
        list_input.remove(('', '---------'))
    except ValueError:
        pass

    mutable_list = [list(elem) for elem in list_input]
    changed_list = [[val-1, data] for val,data in mutable_list]
    tuple_output = [tuple(elem) for elem in changed_list]

    return tuple_output

@register.filter
def plus(int):
    i = int(int)
    i += 1
    return i
