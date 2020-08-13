from django.test import TestCase

# Create your tests here.

def list_test():
    l = [(1,"a"), (2,"a")]

    new_list = [list(elem) for elem in l]

    new_list_changed = [[val-1, data] for val,data in l]

    final_tuple_list = [tuple(elem) for elem in new_list_changed]

    print(new_list_changed)

list_test()

# TEST User
# TESTSTUD
# iamatester
