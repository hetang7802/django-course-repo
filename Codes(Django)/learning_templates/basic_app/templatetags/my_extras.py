# this is for creating custorm template fileters
from django import template

register=template.library()

# below is the use of decorators
@register.filter(name='cut')

def cutfunc(value,arg):
    """
    this cuts out all values of arg from the string
    """
    return value.replace(arg,'')

#below line can be used if we did not use decorators
#register.filter('cut',cutfunc)
