from django import template

register = template.Library()

def rep(value,arg):
    return value.replace(arg,'') #cuts out all values of arg from the string

register.filter('rep',rep)

#using decorators

# from django import template
# register = template.Library()

# @register.filter(name='rep')
# def rep(value,arg):
#     return value.replace(arg,'') #cuts out all values of arg from the string