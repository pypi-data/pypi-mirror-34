import json
from django.template import Library

register = Library()


def dumpjson(object):
    return json.dumps(object)


register.filter('dumpjson', dumpjson)
