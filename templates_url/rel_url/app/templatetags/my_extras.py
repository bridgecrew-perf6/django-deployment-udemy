from django import template

register = template.Library()

@register.filter(name='cutter')
def cutter(value,arg):
    """
    This cuts out all the "arg" from the value
    """
    string = value.replace(arg,"")
    return string

#register.filter('cutter',cutter)
